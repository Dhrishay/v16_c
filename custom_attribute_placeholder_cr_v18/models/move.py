# -*- coding: utf-8 -*-

from odoo import api, fields, models, Command, _
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError
# from odoo.tools import float_compare, float_is_zero, date_utils, email_split, email_re, html_escape, is_html_empty
from odoo.tools.misc import formatLang, format_date, get_lang
from odoo.osv import expression

from datetime import date, timedelta
from collections import defaultdict
from contextlib import contextmanager
from itertools import zip_longest
from hashlib import sha256
from json import dumps

import ast
import json
import re
import warnings

MAX_HASH_VERSION = 2


def calc_check_digits(number):
    """Calculate the extra digits that should be appended to the number to make it a valid number.
    Source: python-stdnum iso7064.mod_97_10.calc_check_digits
    """
    number_base10 = ''.join(str(int(x, 36)) for x in number)
    checksum = int(number_base10) % 97
    return '%02d' % ((98 - 100 * checksum) % 97)

PAYMENT_STATE_SELECTION = [
        ('not_paid', 'Not Paid'),
        ('in_payment', 'In Payment'),
        ('paid', 'Paid'),
        ('partial', 'Partially Paid'),
        ('reversed', 'Reversed'),
        ('invoicing_legacy', 'Invoicing App Legacy'),
]
class AccountMove(models.Model):
    _inherit = "account.move.line"

    is_office_tax = fields.Boolean("is office tax")

class AccountMove(models.Model):
    _inherit = "account.move"

    total_office_cost = fields.Float("office cost")
    total_office_cost_tax = fields.Float("office cost")

    # for send email template attachment
    def _get_mail_template(self):
        office_cost_feature = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.office_cost') or False

        if office_cost_feature:
            return (
                'account.email_template_edi_credit_note'
                if all(move.move_type == 'out_refund' for move in self)
                else 'custom_attribute_placeholder_cr.email_template_edi_invoice'
            )
        else:
            return (
                'account.email_template_edi_credit_note'
                if all(move.move_type == 'out_refund' for move in self)
                else 'account.email_template_edi_invoice'
            )
    # changed
    @api.depends(
        'line_ids.matched_debit_ids.debit_move_id.move_id.origin_payment_id.is_matched',
        'line_ids.matched_debit_ids.debit_move_id.move_id.line_ids.amount_residual',
        'line_ids.matched_debit_ids.debit_move_id.move_id.line_ids.amount_residual_currency',
        'line_ids.matched_credit_ids.credit_move_id.move_id.origin_payment_id.is_matched',
        'line_ids.matched_credit_ids.credit_move_id.move_id.line_ids.amount_residual',
        'line_ids.matched_credit_ids.credit_move_id.move_id.line_ids.amount_residual_currency',
        'line_ids.balance',
        'line_ids.currency_id',
        'line_ids.amount_currency',
        'line_ids.amount_residual',
        'line_ids.amount_residual_currency',
        'line_ids.payment_id.state',
        'line_ids.full_reconcile_id',
        'state')
    def _compute_amount(self):
        office_cost_feature = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.office_cost') or False

        cost_percentage = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.percentage') or False

        max_amount = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.max_amount') or False

        cost_percent = float(cost_percentage)
        maximum_amount = float(max_amount)

        in_invoices = self.filtered(lambda m: m.move_type == 'in_invoice')
        out_invoices = self.filtered(lambda m: m.move_type == 'out_invoice')
        entries = self.filtered(lambda m: m.move_type == 'entry')
        reversed_mapping = defaultdict(lambda: self.env['account.move'])
        if in_invoices or out_invoices or entries:
            for reverse_move in self.env['account.move'].search([
                ('state', '=', 'posted'),
                '|', '|',
                '&', ('reversed_entry_id', 'in', in_invoices.ids), ('move_type', '=', 'in_refund'),
                '&', ('reversed_entry_id', 'in', out_invoices.ids), ('move_type', '=', 'out_refund'),
                '&', ('reversed_entry_id', 'in', entries.ids), ('move_type', '=', 'entry'),
            ]):
                reversed_mapping[reverse_move.reversed_entry_id] += reverse_move

        caba_mapping = defaultdict(lambda: self.env['account.move'])
        caba_company_ids = self.company_id.filtered(lambda c: c.tax_exigibility)
        if caba_company_ids:
            reverse_moves_ids = [move.id for moves in reversed_mapping.values() for move in moves]
            for caba_move in self.env['account.move'].search([
                ('tax_cash_basis_origin_move_id', 'in', self.ids + reverse_moves_ids),
                ('state', '=', 'posted'),
                ('move_type', '=', 'entry'),
                ('company_id', 'in', caba_company_ids.ids)
            ]):
                caba_mapping[caba_move.tax_cash_basis_origin_move_id] += caba_move

        for move in self:
            if move.payment_state == 'invoicing_legacy':
                # invoicing_legacy state is set via SQL when setting setting field
                # invoicing_switch_threshold (defined in account_accountant).
                # The only way of going out of this state is through this setting,
                # so we don't recompute it here.
                move.payment_state = move.payment_state
                continue

            total_untaxed = 0.0
            total_untaxed_currency = 0.0
            total_tax = 0.0
            total_tax_currency = 0.0
            total_to_pay = 0.0
            total_residual = 0.0
            total_residual_currency = 0.0
            total = 0.0
            total_currency = 0.0
            currencies = move._get_lines_onchange_currency().currency_id

            for line in move.line_ids:
                if move._payment_state_matters():
                    # === Invoices ===

                    if not line.exclude_from_invoice_tab:
                        # Untaxed amount.
                        total_untaxed += line.balance
                        total_untaxed_currency += line.amount_currency
                        total += line.balance
                        total_currency += line.amount_currency
                    elif line.tax_line_id:
                        # Tax amount.
                        total_tax += line.balance
                        total_tax_currency += line.amount_currency
                        total += line.balance
                        total_currency += line.amount_currency
                    elif line.account_id.user_type_id.type in ('receivable', 'payable'):
                        # Residual amount.
                        total_to_pay += line.balance
                        total_residual += line.amount_residual
                        total_residual_currency += line.amount_residual_currency
                else:
                    # === Miscellaneous journal entry ===
                    if line.debit:
                        total += line.balance
                        total_currency += line.amount_currency

            if move.move_type == 'entry' or move.is_outbound():
                sign = 1
            else:
                sign = -1
            move.amount_untaxed = sign * (total_untaxed_currency if len(currencies) == 1 else total_untaxed)
            move.amount_tax = sign * (total_tax_currency if len(currencies) == 1 else total_tax)
            move.amount_total = sign * (total_currency if len(currencies) == 1 else total)

            extra_amount = 0
            office_total_tax = 0
            if office_cost_feature and cost_percentage:
                amount_cost_perc = move.amount_untaxed * cost_percent / 100
                if maximum_amount > 0:
                    extra_amount = maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc
                else:
                    extra_amount = amount_cost_perc
            total_amount_move = (sign * (total_currency if len(currencies) == 1 else total)) + extra_amount
            move.amount_total = total_amount_move



            move.amount_residual = -sign * (total_residual_currency if len(currencies) == 1 else total_residual)
            move.amount_untaxed_signed = -total_untaxed
            move.amount_tax_signed = -total_tax
            move.amount_total_signed = abs(total) if move.move_type == 'entry' else -total
            move.amount_residual_signed = total_residual
            move.amount_total_in_currency_signed = abs(move.amount_total) if move.move_type == 'entry' else -(
                        sign * move.amount_total)

            currency = currencies if len(currencies) == 1 else move.company_id.currency_id

            # Compute 'payment_state'.
            new_pmt_state = 'not_paid' if move.move_type != 'entry' else False

            if move._payment_state_matters() and move.state == 'posted':
                if currency.is_zero(move.amount_residual):
                    reconciled_payments = move._get_reconciled_payments()
                    if not reconciled_payments or all(payment.is_matched for payment in reconciled_payments):
                        new_pmt_state = 'paid'
                    else:
                        new_pmt_state = move._get_invoice_in_payment_state()
                elif currency.compare_amounts(total_to_pay, total_residual) != 0:
                    new_pmt_state = 'partial'

            if new_pmt_state == 'paid' and move.move_type in ('in_invoice', 'out_invoice', 'entry'):
                reverse_moves = reversed_mapping[move]
                caba_moves = caba_mapping[move]
                for reverse_move in reverse_moves:
                    caba_moves |= caba_mapping[reverse_move]

                # We only set 'reversed' state in cas of 1 to 1 full reconciliation with a reverse entry; otherwise, we use the regular 'paid' state
                # We ignore potentials cash basis moves reconciled because the transition account of the tax is reconcilable
                reverse_moves_full_recs = reverse_moves.mapped('line_ids.full_reconcile_id')
                if reverse_moves_full_recs.mapped('reconciled_line_ids.move_id').filtered(lambda x: x not in (
                        caba_moves + reverse_moves + reverse_moves_full_recs.mapped('exchange_move_id'))) == move:
                    new_pmt_state = 'reversed'

            move.payment_state = new_pmt_state


    @api.model

    def _get_tax_totals(self, partner, tax_lines_data, amount_total, amount_untaxed, currency):
        """ Compute the tax totals for the provided data.

        :param partner:        The partner to compute totals for
        :param tax_lines_data: All the data about the base and tax lines as a list of dictionaries.
                               Each dictionary represents an amount that needs to be added to either a tax base or amount.
                               A tax amount looks like:
                                   {
                                       'line_key':             unique identifier,
                                       'tax_amount':           the amount computed for this tax
                                       'tax':                  the account.tax object this tax line was made from
                                   }
                               For base amounts:
                                   {
                                       'line_key':             unique identifier,
                                       'base_amount':          the amount to add to the base of the tax
                                       'tax':                  the tax basing itself on this amount
                                       'tax_affecting_base':   (optional key) the tax whose tax line is having the impact
                                                               denoted by 'base_amount' on the base of the tax, in case of taxes
                                                               affecting the base of subsequent ones.
                                   }
        :param amount_total:   Total amount, with taxes.
        :param amount_untaxed: Total amount without taxes.
        :param currency:       The currency in which the amounts are computed.

        :return: A dictionary in the following form:
            {
                'amount_total':                              The total amount to be displayed on the document, including every total types.
                'amount_untaxed':                            The untaxed amount to be displayed on the document.
                'formatted_amount_total':                    Same as amount_total, but as a string formatted accordingly with partner's locale.
                'formatted_amount_untaxed':                  Same as amount_untaxed, but as a string formatted accordingly with partner's locale.
                'allow_tax_edition':                         True if the user should have the ability to manually edit the tax amounts by group
                                                             to fix rounding errors.
                'groups_by_subtotals':                       A dictionary formed liked {'subtotal': groups_data}
                                                             Where total_type is a subtotal name defined on a tax group, or the default one: 'Untaxed Amount'.
                                                             And groups_data is a list of dict in the following form:
                                                                {
                                                                    'tax_group_name':                  The name of the tax groups this total is made for.
                                                                    'tax_group_amount':                The total tax amount in this tax group.
                                                                    'tax_group_base_amount':           The base amount for this tax group.
                                                                    'formatted_tax_group_amount':      Same as tax_group_amount, but as a string
                                                                                                       formatted accordingly with partner's locale.
                                                                    'formatted_tax_group_base_amount': Same as tax_group_base_amount, but as a string
                                                                                                       formatted accordingly with partner's locale.
                                                                    'tax_group_id':                    The id of the tax group corresponding to this dict.
                                                                    'group_key':                       A unique key identifying this total dict,
                                                                }
                'subtotals':                                 A list of dictionaries in the following form, one for each subtotal in groups_by_subtotals' keys
                                                                {
                                                                    'name':                            The name of the subtotal
                                                                    'amount':                          The total amount for this subtotal, summing all
                                                                                                       the tax groups belonging to preceding subtotals and the base amount
                                                                    'formatted_amount':                Same as amount, but as a string
                                                                                                       formatted accordingly with partner's locale.
                                                                }
            }
        """
        self.total_office_cost = 0.0
        self.total_office_cost_tax = 0.0
        office_cost_feature = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.office_cost') or False

        cost_percentage = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.percentage') or False

        max_amount = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.max_amount') or False

        cost_percent = float(cost_percentage)
        maximum_amount = float(max_amount)
        cost_amount = 0
        total_tax = 0
        if office_cost_feature and cost_percentage:
            cost_amount = (amount_untaxed * cost_percent / 100)
            if maximum_amount > 0:
                if cost_amount > maximum_amount:
                    cost_amount = maximum_amount
                    self.total_office_cost  = maximum_amount
                else:
                    self.total_office_cost = cost_amount
            else:
                self.total_office_cost = cost_amount

        account_tax = self.env['account.tax']

        grouped_taxes = defaultdict(lambda: defaultdict(lambda: {'base_amount': 0.0, 'tax_amount': 0.0, 'base_line_keys': set()}))
        subtotal_priorities = {}
        office_tax_ids = []
        # for line_data in tax_lines_data:
        #     if 'base_amount' not in line_data:
        #         tax = line_data['tax']
        #         if tax.id not in office_tax_ids:
        #             office_cost_amount = tax.compute_all(cost_amount)
        #             office_tax_ids.append(tax.id)
        #             for line_tax in office_cost_amount:
        #                 if 'taxes' in line_tax:
        #                     for line in office_cost_amount['taxes']:
        #                         line_data['tax_amount'] = line_data['tax_amount'] + line['amount']
                                # if not self.total_office_cost_tax:
                                #     total_tax = total_tax + line['amount']
                                # self.total_office_cost_tax += self.total_office_cost_tax + line['amount']



        for line_data in tax_lines_data:
            tax_group = line_data['tax'].tax_group_id

            # Update subtotals priorities
            if tax_group.preceding_subtotal:
                subtotal_title = tax_group.preceding_subtotal
                new_priority = tax_group.sequence
            else:
                # When needed, the default subtotal is always the most prioritary
                subtotal_title = "Untaxed Amount"
                new_priority = 0

            if subtotal_title not in subtotal_priorities or new_priority < subtotal_priorities[subtotal_title]:
                subtotal_priorities[subtotal_title] = new_priority

            # Update tax data
            tax_group_vals = grouped_taxes[subtotal_title][tax_group]

            if 'base_amount' in line_data:
                # Base line
                if tax_group == line_data.get('tax_affecting_base', account_tax).tax_group_id:
                    # In case the base has a tax_line_id belonging to the same group as the base tax,
                    # the base for the group will be computed by the base tax's original line (the one with tax_ids and no tax_line_id)
                    continue

                if line_data['line_key'] not in tax_group_vals['base_line_keys']:
                    # If the base line hasn't been taken into account yet, at its amount to the base total.
                    tax_group_vals['base_line_keys'].add(line_data['line_key'])
                    tax_group_vals['base_amount'] += line_data['base_amount']

            else:
                # Tax line
                tax_group_vals['tax_amount'] += line_data['tax_amount']

        # Compute groups_by_subtotal
        groups_by_subtotal = {}
        for subtotal_title, groups in grouped_taxes.items():
            groups_vals = [{
                'tax_group_name': group.name,
                'tax_group_amount': amounts['tax_amount'],
                'tax_group_base_amount': amounts['base_amount'],
                'formatted_tax_group_amount': formatLang(self.env, amounts['tax_amount'], currency_obj=currency),
                'formatted_tax_group_base_amount': formatLang(self.env,
                                                              amounts['base_amount'] if office_cost_feature else
                                                              amounts['base_amount'], currency_obj=currency),
                'tax_group_id': group.id,
                'group_key': '%s-%s' % (subtotal_title, group.id),
            } for group, amounts in sorted(groups.items(), key=lambda l: l[0].sequence)]

            groups_by_subtotal[subtotal_title] = groups_vals

        # Compute subtotals
        subtotals_list = [] # List, so that we preserve their order
        previous_subtotals_tax_amount = 0
        for subtotal_title in sorted((sub for sub in subtotal_priorities), key=lambda x: subtotal_priorities[x]):
            subtotal_value = amount_untaxed + previous_subtotals_tax_amount
            subtotals_list.append({
                'name': subtotal_title,
                'amount': subtotal_value,
                'formatted_amount': formatLang(self.env, subtotal_value, currency_obj=currency),
            })

            subtotal_tax_amount = sum(group_val['tax_group_amount'] for group_val in groups_by_subtotal[subtotal_title])
            previous_subtotals_tax_amount += subtotal_tax_amount

        formated_percentage = int(cost_percent) if cost_percent.is_integer() else cost_percent
        office_cost_string = "Office Cost " + str(formated_percentage) + '%'

        if office_cost_feature and cost_percentage:
            if 'Untaxed Amount' in groups_by_subtotal:
                # groups_by_subtotal['Untaxed Amount'][0]['formatted_tax_group_base_amount'] = formatLang(self.env, amount_untaxed + cost_amount, currency_obj=currency)
                groups_by_subtotal['Untaxed Amount'].append({
                    "tax_group_name": office_cost_string,
                    "tax_group_amount": cost_amount,
                    "tax_group_base_amount": cost_amount,
                    "formatted_tax_group_amount": formatLang(self.env, cost_amount,
                                                             currency_obj=currency),
                    'formatted_tax_group_base_amount': formatLang(self.env, amount_untaxed, currency_obj=currency),
                })
        if groups_by_subtotal:
            groups_by_subtotal.get('Untaxed Amount').reverse()
        # Assign json-formatted result to the field
        # self.amount_total = self.amount_total + self.total_office_cost_tax
        if office_cost_feature and cost_percentage:
            if 'Untaxed Amount' not in groups_by_subtotal:

                return {
                    'amount_total': amount_total ,
                    'office_cost_string': office_cost_string,
                    'formatted_office_cost':formatLang(self.env, cost_amount,
                                                                     currency_obj=currency),
                    'amount_untaxed': amount_untaxed,
                    'formatted_amount_total': formatLang(self.env, amount_total, currency_obj=currency),
                    'formatted_amount_untaxed': formatLang(self.env, amount_untaxed, currency_obj=currency),
                    'groups_by_subtotal': groups_by_subtotal,
                    'subtotals': subtotals_list,
                    'allow_tax_edition': False,
                }
            else:
                return {
                    'amount_total': amount_total,
                    'amount_untaxed': amount_untaxed,
                    'formatted_amount_total': formatLang(self.env, amount_total, currency_obj=currency),
                    'formatted_amount_untaxed': formatLang(self.env, amount_untaxed, currency_obj=currency),
                    'groups_by_subtotal': groups_by_subtotal,
                    'subtotals': subtotals_list,
                    'allow_tax_edition': False,
                }
        else:
            return {
                'amount_total': amount_total,
                'amount_untaxed': amount_untaxed,
                'formatted_amount_total': formatLang(self.env, amount_total, currency_obj=currency),
                'formatted_amount_untaxed': formatLang(self.env, amount_untaxed, currency_obj=currency),
                'groups_by_subtotal': groups_by_subtotal,
                'subtotals': subtotals_list,
                'allow_tax_edition': False,
            }

    def _recompute_tax_lines(self, recompute_tax_base_amount=False, tax_rep_lines_to_recompute=None):
        """ Compute the dynamic tax lines of the journal entry.

        :param recompute_tax_base_amount: Flag forcing only the recomputation of the `tax_base_amount` field.
        """
        self.ensure_one()
        in_draft_mode = self != self._origin

        def _serialize_tax_grouping_key(grouping_dict):
            ''' Serialize the dictionary values to be used in the taxes_map.
            :param grouping_dict: The values returned by '_get_tax_grouping_key_from_tax_line' or '_get_tax_grouping_key_from_base_line'.
            :return: A string representing the values.
            '''
            return '-'.join(str(v) for v in grouping_dict.values())

        def _compute_base_line_taxes(base_line):
            ''' Compute taxes amounts both in company currency / foreign currency as the ratio between
            amount_currency & balance could not be the same as the expected currency rate.
            The 'amount_currency' value will be set on compute_all(...)['taxes'] in multi-currency.
            :param base_line:   The account.move.line owning the taxes.
            :return:            The result of the compute_all method.
            '''
            move = base_line.move_id

            if move.is_invoice(include_receipts=True):
                handle_price_include = True
                sign = -1 if move.is_inbound() else 1
                quantity = base_line.quantity
                is_refund = move.move_type in ('out_refund', 'in_refund')
                price_unit_wo_discount = sign * base_line.price_unit * (1 - (base_line.discount / 100.0))
            else:
                handle_price_include = False
                quantity = 1.0
                tax_type = base_line.tax_ids[0].type_tax_use if base_line.tax_ids else None
                is_refund = (tax_type == 'sale' and base_line.debit) or (tax_type == 'purchase' and base_line.credit)
                price_unit_wo_discount = base_line.amount_currency

            return base_line.tax_ids._origin.with_context(force_sign=move._get_tax_force_sign()).compute_all(
                price_unit_wo_discount,
                currency=base_line.currency_id,
                quantity=quantity,
                product=base_line.product_id,
                partner=base_line.partner_id,
                is_refund=is_refund,
                handle_price_include=handle_price_include,
                include_caba_tags=move.always_tax_exigible,
            )

        taxes_map = {}

        # ==== Add tax lines ====
        to_remove = self.env['account.move.line']
        for line in self.line_ids.filtered('tax_repartition_line_id'):
            grouping_dict = self._get_tax_grouping_key_from_tax_line(line)
            grouping_key = _serialize_tax_grouping_key(grouping_dict)
            if grouping_key in taxes_map:
                # A line with the same key does already exist, we only need one
                # to modify it; we have to drop this one.
                to_remove += line
            else:
                taxes_map[grouping_key] = {
                    'tax_line': line,
                    'amount': 0.0,
                    'tax_base_amount': 0.0,
                    'grouping_dict': False,
                }
        if not recompute_tax_base_amount:
            self.line_ids -= to_remove

        # ==== Mount base lines ====
        for line in self.line_ids.filtered(lambda line: not line.tax_repartition_line_id and not line.is_office_tax):
            # Don't call compute_all if there is no tax.
            if not line.tax_ids:
                if not recompute_tax_base_amount:
                    line.tax_tag_ids = [(5, 0, 0)]
                continue

            compute_all_vals = _compute_base_line_taxes(line)

            # Assign tags on base line
            if not recompute_tax_base_amount:
                line.tax_tag_ids = compute_all_vals['base_tags'] or [(5, 0, 0)]

            for tax_vals in compute_all_vals['taxes']:
                grouping_dict = self._get_tax_grouping_key_from_base_line(line, tax_vals)
                grouping_key = _serialize_tax_grouping_key(grouping_dict)

                tax_repartition_line = self.env['account.tax.repartition.line'].browse(tax_vals['tax_repartition_line_id'])
                tax = tax_repartition_line.invoice_tax_id or tax_repartition_line.refund_tax_id

                taxes_map_entry = taxes_map.setdefault(grouping_key, {
                    'tax_line': None,
                    'amount': 0.0,
                    'tax_base_amount': 0.0,
                    'grouping_dict': False,
                })
                # ////////////////////////////custom code//////////////////////////////////////////////////////////
                office_cost_feature = self.env['ir.config_parameter'].sudo().get_param(
                    'custom_attribute_placeholder_cr.office_cost') or False

                cost_percentage = self.env['ir.config_parameter'].sudo().get_param(
                    'custom_attribute_placeholder_cr.percentage') or False

                max_amount = self.env['ir.config_parameter'].sudo().get_param(
                    'custom_attribute_placeholder_cr.max_amount') or False
                cost_percent = float(cost_percentage)
                maximum_amount = float(max_amount)
                add_amount = 0
                counter = len(self.line_ids.filtered(lambda line: not line.tax_repartition_line_id
                                                                  and not line.is_office_tax and not line.exclude_from_invoice_tab))
                max_flag = False
                if office_cost_feature and cost_percentage:
                    amount_cost_perc = line.price_subtotal * tax[0].amount / 100
                    if amount_cost_perc > maximum_amount and maximum_amount > 0:
                        max_flag = True
                    if maximum_amount > 0:
                        extra_amount = maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc
                    else:
                        extra_amount = amount_cost_perc

                    if extra_amount > 0:
                        if max_flag:
                            add_amount = (extra_amount / counter) * cost_percent / 100
                        else:
                            add_amount = extra_amount * cost_percent / 100
                # ////////////////////////////custom code//////////////////////////////////////////////////////////
                taxes_map_entry['amount'] += tax_vals['amount'] + (-add_amount) if tax_vals['amount'] < 0 else add_amount
                taxes_map_entry['tax_base_amount'] += self._get_base_amount_to_display(tax_vals['base'], tax_repartition_line, tax_vals['group'])
                taxes_map_entry['grouping_dict'] = grouping_dict

        # ==== Pre-process taxes_map ====
        taxes_map = self._preprocess_taxes_map(taxes_map)

        # ==== Process taxes_map ====
        for taxes_map_entry in taxes_map.values():
            # The tax line is no longer used in any base lines, drop it.
            if taxes_map_entry['tax_line'] and not taxes_map_entry['grouping_dict']:
                if not recompute_tax_base_amount:
                    self.line_ids -= taxes_map_entry['tax_line']
                continue

            currency = self.env['res.currency'].browse(taxes_map_entry['grouping_dict']['currency_id'])

            # Don't create tax lines with zero balance.
            if currency.is_zero(taxes_map_entry['amount']):
                if taxes_map_entry['tax_line'] and not recompute_tax_base_amount:
                    self.line_ids -= taxes_map_entry['tax_line']
                continue

            # tax_base_amount field is expressed using the company currency.
            tax_base_amount = currency._convert(taxes_map_entry['tax_base_amount'], self.company_currency_id, self.company_id, self.date or fields.Date.context_today(self))

            # Recompute only the tax_base_amount.
            if recompute_tax_base_amount:
                if taxes_map_entry['tax_line']:
                    taxes_map_entry['tax_line'].tax_base_amount = tax_base_amount
                continue

            balance = currency._convert(
                taxes_map_entry['amount'],
                self.company_currency_id,
                self.company_id,
                self.date or fields.Date.context_today(self),
            )
            amount_currency = currency.round(taxes_map_entry['amount'])
            sign = -1 if self.is_inbound() else 1
            to_write_on_line = {
                'amount_currency': amount_currency,
                'currency_id': taxes_map_entry['grouping_dict']['currency_id'],
                'debit': balance > 0.0 and balance or 0.0,
                'credit': balance < 0.0 and -balance or 0.0,
                'tax_base_amount': tax_base_amount,
                'price_total': sign * amount_currency,
                'price_subtotal': sign * amount_currency,
            }

            if taxes_map_entry['tax_line']:
                # Update an existing tax line.
                if tax_rep_lines_to_recompute and taxes_map_entry['tax_line'].tax_repartition_line_id not in tax_rep_lines_to_recompute:
                    continue

                taxes_map_entry['tax_line'].update(to_write_on_line)
            else:
                # Create a new tax line.
                create_method = in_draft_mode and self.env['account.move.line'].new or self.env['account.move.line'].create
                tax_repartition_line_id = taxes_map_entry['grouping_dict']['tax_repartition_line_id']
                tax_repartition_line = self.env['account.tax.repartition.line'].browse(tax_repartition_line_id)

                if tax_rep_lines_to_recompute and tax_repartition_line not in tax_rep_lines_to_recompute:
                    continue

                tax = tax_repartition_line.invoice_tax_id or tax_repartition_line.refund_tax_id
                taxes_map_entry['tax_line'] = create_method({
                    **to_write_on_line,
                    'name': tax.name,
                    'move_id': self.id,
                    'company_id': self.company_id.id,
                    'company_currency_id': self.company_currency_id.id,
                    'tax_base_amount': tax_base_amount,
                    'exclude_from_invoice_tab': True,
                    **taxes_map_entry['grouping_dict'],
                })

            if in_draft_mode:
                taxes_map_entry['tax_line'].update(taxes_map_entry['tax_line']._get_fields_onchange_balance(force_computation=True))


    def _recompute_dynamic_lines(self, recompute_all_taxes=False, recompute_tax_base_amount=False):
        ''' Recompute all lines that depend on others.

        For example, tax lines depends on base lines (lines having tax_ids set). This is also the case of cash rounding
        lines that depend on base lines or tax lines depending on the cash rounding strategy. When a payment term is set,
        this method will auto-balance the move with payment term lines.

        :param recompute_all_taxes: Force the computation of taxes. If set to False, the computation will be done
                                    or not depending on the field 'recompute_tax_line' in lines.
        '''
        for invoice in self:
            # Dispatch lines and pre-compute some aggregated values like taxes.
            expected_tax_rep_lines = set()
            current_tax_rep_lines = set()
            inv_recompute_all_taxes = recompute_all_taxes
            has_taxes = False
            for line in invoice.line_ids:
                if line.recompute_tax_line:
                    inv_recompute_all_taxes = True
                    line.recompute_tax_line = False
                if line.tax_repartition_line_id:
                    current_tax_rep_lines.add(line.tax_repartition_line_id._origin)
                elif line.tax_ids:
                    has_taxes = True
                    if invoice.is_invoice(include_receipts=True):
                        is_refund = invoice.move_type in ('out_refund', 'in_refund')
                    else:
                        tax_type = line.tax_ids[0].type_tax_use
                        is_refund = (tax_type == 'sale' and line.debit) or (tax_type == 'purchase' and line.credit)
                    # taxes = line.tax_ids._origin.flatten_taxes_hierarchy().filtered(
                    #     lambda tax: (
                    #             tax.amount_type == 'fixed' and not invoice.company_id.currency_id.is_zero(tax.amount)
                    #             or not float_is_zero(tax.amount, precision_digits=4)
                    #     )
                    # )
            #         if is_refund:
            #             tax_rep_lines = taxes.refund_repartition_line_ids._origin.filtered(
            #                 lambda x: x.repartition_type == "tax")
            #         else:
            #             tax_rep_lines = taxes.invoice_repartition_line_ids._origin.filtered(
            #                 lambda x: x.repartition_type == "tax")
            #         for tax_rep_line in tax_rep_lines:
            #             expected_tax_rep_lines.add(tax_rep_line)
            # delta_tax_rep_lines = expected_tax_rep_lines - current_tax_rep_lines
            # //////////////////////////////////////////////////  CUSTOM CODE   ////////////////////////////////////////////////
            taxed_total = sum(self.invoice_line_ids.filtered(lambda l: l.tax_ids).mapped('price_unit'))
            # without_taxed_total = sum(self.invoice_line_ids.filtered(lambda l: not l.tax_ids).mapped('price_unit'))
            # if not (taxed_total > 0 and len(self.invoice_line_ids) > 0):
            office_cost_feature = self.env['ir.config_parameter'].sudo().get_param(
                'custom_attribute_placeholder_cr.office_cost') or False

            cost_percentage = self.env['ir.config_parameter'].sudo().get_param(
                'custom_attribute_placeholder_cr.percentage') or False

            max_amount = self.env['ir.config_parameter'].sudo().get_param(
                'custom_attribute_placeholder_cr.max_amount') or False
            cost_percent = float(cost_percentage)
            maximum_amount = float(max_amount)
            extra_amount = 0
            office_total_tax = 0
            tax_ids = []

            if office_cost_feature and cost_percentage:
                amount_cost_perc = self.amount_untaxed * cost_percent / 100
                if maximum_amount > 0:
                    extra_amount = maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc
                else:
                    extra_amount = amount_cost_perc
            currency = self.currency_id
            in_draft_mode = self != self._origin
            sign = -1 if self.is_inbound() else 1

            office_tax_ids = []
            tax_rec = invoice.invoice_line_ids.filtered(lambda l: l.tax_ids).mapped('tax_ids')
            total_tax = 0
            account_id = False

            journal = self.journal_id
            account_id = journal.default_account_id
            # if tax_rec:
            #     extra_amount = total_tax
            balance = currency._convert(
                sign * extra_amount,
                self.company_currency_id,
                self.company_id,
                self.date or fields.Date.context_today(self),
            )
            amount_currency = currency.round(extra_amount)

            if office_cost_feature and cost_percentage:
                selected_tax = self.env['account.tax'].sudo().search([('type_tax_use', 'in', [self.invoice_filter_type_domain])])
                expence_account = self.env.ref('l10n_generic_coa.1_expense')
                if not self.invoice_filter_type_domain:
                    if self._context and self._context.get('active_id', False):
                        acc = self.browse(self._context.get('active_id'))
                        selected_tax = self.env['account.tax'].sudo().search(
                            [('type_tax_use', 'in', [acc[0].invoice_filter_type_domain])])

                repart_line = False
                if selected_tax:
                    repart_line = selected_tax[0].invoice_repartition_line_ids._origin.filtered(lambda x: x.repartition_type == "tax")

                # sign = 1 if self.move_type in ['out_invoice', 'in_refund'] else -1

                to_write_on_line = {
                    'amount_currency': amount_currency,
                    'currency_id': currency.id,
                    'debit': balance > 0.0 and balance or 0.0,
                    'credit': balance < 0.0 and -balance or 0.0,
                    'tax_base_amount': extra_amount,
                    'price_total': sign * amount_currency,
                    'price_subtotal': sign * amount_currency,
                    'exclude_from_invoice_tab': True,
                    'partner_id': self.partner_id.id
                    # 'tax_ids': [(6, 0, tax_rec[0].ids)],
                    # 'amount': extra_amount,
                    # 'grouping_dict': False,
                }
                if selected_tax and repart_line:
                    to_write_on_line.update({'account_id': repart_line.account_id.id})
                if selected_tax and not repart_line.account_id:
                    to_write_on_line.update({'account_id': expence_account.id})
                if tax_rec:
                    to_write_on_line.update({'tax_ids': [(6, 0, tax_rec[0].ids)]})
                create_method_custom = in_draft_mode and self.env['account.move.line'].new or self.env[
                    'account.move.line'].create
                is_office_tax_added = invoice.line_ids.filtered(lambda x: x.name == 'Office Cost')
                invoice.line_ids -= is_office_tax_added

                if self.state and self.state in ['draft']:
                    if selected_tax and repart_line:
                        to_write_on_line.update({'account_id': repart_line.account_id.id})
                    if selected_tax and not repart_line.account_id:
                        to_write_on_line.update({'account_id': expence_account.id})
                    create_method_custom({
                        **to_write_on_line,
                        'name': 'Office Cost',
                        'is_office_tax': True,
                        'move_id': self.id,
                        'partner_id': self.partner_id.id,
                        'company_id': self.company_id.id,
                        'company_currency_id': self.company_currency_id.id,
                        'exclude_from_invoice_tab': True,
                    })

            # //////////////////////////////////////////////////  CUSTOM CODE   ////////////////////////////////////////////////
            # Compute taxes.
            # if has_taxes or current_tax_rep_lines:
            #     if inv_recompute_all_taxes:
            #         invoice._recompute_tax_lines()
            #     elif recompute_tax_base_amount:
            #         invoice._recompute_tax_lines(recompute_tax_base_amount=True)
            #     elif delta_tax_rep_lines and not self._context.get('move_reverse_cancel'):
            #         invoice._recompute_tax_lines(tax_rep_lines_to_recompute=delta_tax_rep_lines)

            if invoice.is_invoice(include_receipts=True):

                # Compute cash rounding.
                invoice._recompute_cash_rounding_lines()

                # Compute payment terms.
                invoice._recompute_payment_terms_lines()

                # Only synchronize one2many in onchange.
                if invoice != invoice._origin:
                    invoice.invoice_line_ids = invoice.line_ids.filtered(lambda line: not line.exclude_from_invoice_tab)
