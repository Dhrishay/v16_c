# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, _
import json
from odoo.tools.misc import formatLang


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.model
    def _get_price_total_and_subtotal_model(self, price_unit, quantity, discount, currency, product, partner, taxes, move_type):
        print("\n\n\n_get_price_total_and_subtotal_model-------------------move line----------------------------")
        ''' This method is used to compute 'price_total' & 'price_subtotal'.

        :param price_unit:  The current price unit.
        :param quantity:    The current quantity.
        :param discount:    The current discount.
        :param currency:    The line's currency.
        :param product:     The line's product.
        :param partner:     The line's partner.
        :param taxes:       The applied taxes.
        :param move_type:   The type of the move.
        :return:            A dictionary containing 'price_subtotal' & 'price_total'.

        '''
        # office_cost_feature = self.env['ir.config_parameter'].sudo().get_param(
        #     'custom_attribute_placeholder_cr.office_cost') or False
        #
        # cost_percentage = self.env['ir.config_parameter'].sudo().get_param(
        #     'custom_attribute_placeholder_cr.percentage') or False
        #
        # max_amount = self.env['ir.config_parameter'].sudo().get_param(
        #     'custom_attribute_placeholder_cr.max_amount') or False
        #
        # cost_percent = float(cost_percentage)
        # maximum_amount = float(max_amount)



        res = {}

        # Compute 'price_subtotal'.
        line_discount_price_unit = price_unit * (1 - (discount / 100.0))

        total_lines = len(self.move_id.invoice_line_ids.filtered(lambda line: line.tax_ids))
        subtotal = quantity * line_discount_price_unit

        # cost = line_discount_price_unit * cost_percent / 100
        # if office_cost_feature and cost_percentage:
        #     total_lines = len(self.move_id.invoice_line_ids.filtered(lambda line: not line.recompute_tax_line))
        #     print("total_lines>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..",total_lines)
        #     if cost > maximum_amount and total_lines > 0:
        #         print("line_discount_price_unit>>>>>>>IF>>>>",line_discount_price_unit)
        #         max_amount  = maximum_amount / total_lines
        #         print("max_amount>>>>>>>>>>>>>>.",max_amount)
        #         line_discount_price_unit = line_discount_price_unit + max_amount
        #         print("line_discount_price_unit>>>>>>>>>>>>>>.", line_discount_price_unit)
        #     else:
        #         print("line_discount_price_unit>>>>>>>ELSE>>>>", line_discount_price_unit)
        #         line_discount_price_unit = line_discount_price_unit + cost
        # Compute 'price_total'.
        context_dict = {'total_lines':total_lines, 'force_sign':1}
        if taxes:
            taxes_res = taxes._origin.with_context(context_dict).compute_all(line_discount_price_unit,
                                                                             quantity=quantity, currency=currency,
                                                                             product=product, partner=partner,
                                                                             is_refund=move_type in (
                                                                             'out_refund', 'in_refund'))
            res['price_subtotal'] = taxes_res['total_excluded']
            res['price_total'] = taxes_res['total_included']

        else:
            res['price_total'] = res['price_subtotal'] = subtotal
        # In case of multi currency, round before it's use for computing debit credit
        if currency:
            res = {k: currency.round(v) for k, v in res.items()}
        return res



class AccountMove(models.Model):
    _inherit = "account.move"

    cost = fields.Float("Cost")
    sale_tax = fields.Float("Sale tax")

    def _get_mail_template(self):
        print("\n\n\n_get_mail_template---------------------move----------------------------------")
        return (
            'custom_attribute_placeholder_cr.c'
            if all(move.move_type == 'out_refund' for move in self)
            else 'custom_attribute_placeholder_cr.email_template_edi_invoice'
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
        print("\n\n\n_compute_amount---------------------move--------------------------------------------")

        office_cost_feature = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.office_cost') or False

        cost_percentage = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.percentage') or False

        max_amount = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.max_amount') or False

        cost_percent = float(cost_percentage)
        maximum_amount = float(max_amount)

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
            if office_cost_feature and cost_percentage:
                total_residual_temp = -sign * (total_residual_currency if len(currencies) == 1 else total_residual)
                amount_cost_perc = move.amount_untaxed * cost_percent / 100
                # extra_amount = (maximum_amount if amount_cost_perc > maximum_amount else move.amount_tax * (cost_percent / 100)) + (maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc)
                extra_amount = maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc
                move.amount_total += extra_amount
                if total_residual_temp:
                        move.amount_residual = total_residual_temp + extra_amount
                else:
                    move.amount_residual = 0.00
            else:
                move.amount_residual = -sign * (total_residual_currency if len(currencies) == 1 else total_residual)

            move.amount_untaxed_signed = -total_untaxed + ( extra_amount)
            move.amount_tax_signed = -total_tax
            move.amount_total_signed = abs(total + extra_amount) if move.move_type == 'entry' else -total + ( extra_amount)
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
                reverse_type = move.move_type == 'in_invoice' and 'in_refund' or move.move_type == 'out_invoice' and 'out_refund' or 'entry'
                reverse_moves = self.env['account.move'].search(
                    [('reversed_entry_id', '=', move.id), ('state', '=', 'posted'), ('move_type', '=', reverse_type)])
                caba_moves = self.env['account.move'].search(
                    [('tax_cash_basis_origin_move_id', 'in', move.ids + reverse_moves.ids), ('state', '=', 'posted')])

                # We only set 'reversed' state in cas of 1 to 1 full reconciliation with a reverse entry; otherwise, we use the regular 'paid' state
                # We ignore potentials cash basis moves reconciled because the transition account of the tax is reconcilable
                reverse_moves_full_recs = reverse_moves.mapped('line_ids.full_reconcile_id')
                if reverse_moves_full_recs.mapped('reconciled_line_ids.move_id').filtered(lambda x: x not in (
                        caba_moves + reverse_moves + reverse_moves_full_recs.mapped('exchange_move_id'))) == move:
                    new_pmt_state = 'reversed'

            move.payment_state = new_pmt_state


    def _compute_tax_totals_json(self):
        print("\n\n\n_compute_tax_totals_json----------------move----------------------------------")
        res = super(AccountMove, self)._compute_tax_totals_json()

        office_cost_feature = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.office_cost') or False

        cost_percentage = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.percentage') or False

        max_amount = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.max_amount') or False

        cost_percent = float(cost_percentage)
        maximum_amount = float(max_amount)
        list_dict = []
        if office_cost_feature:

            for rec in self:
                if rec.tax_totals_json:
                    currency = rec.company_id.currency_id
                    tax_totals_json_dict = json.loads(rec.tax_totals_json)
                    amount_total = tax_totals_json_dict['amount_total']
                    amount_untaxed = tax_totals_json_dict['amount_untaxed']
                    amount_cost_perc = tax_totals_json_dict['amount_untaxed'] * cost_percent / 100
                    # final_deducted_amount = False
                    #
                    # if office_cost_feature and cost_percentage:
                    #     amount_cost_perc = tax_totals_json_dict['amount_untaxed'] * cost_percent / 100
                    #
                    #     if amount_cost_perc > maximum_amount:
                    #         final_deducted_amount = tax_totals_json_dict['amount_total'] - maximum_amount
                    #         tax_totals_json_dict['deducted_amount'] = final_deducted_amount
                    #         tax_totals_json_dict['formatted_deducted_amount'] = formatLang(self.env, final_deducted_amount,
                    #                                                                     currency_obj=currency)
                    #     else:
                    #         final_deducted_amount = tax_totals_json_dict['amount_total'] - amount_cost_perc
                    #         tax_totals_json_dict['deducted_amount'] = final_deducted_amount
                    #         tax_totals_json_dict['formatted_deducted_amount'] = formatLang(self.env, final_deducted_amount,
                    #                                                                        currency_obj=currency)

                    if office_cost_feature and cost_percentage:

                        final_deducted_amount = tax_totals_json_dict['amount_total']
                        tax_totals_json_dict['deducted_amount'] = final_deducted_amount
                        tax_totals_json_dict['formatted_deducted_amount'] = formatLang(self.env, final_deducted_amount,
                                                                                       currency_obj=currency)
                        # integer and float formate
                        formated_percentage = int(cost_percent) if cost_percent.is_integer() else cost_percent
                        tax_totals_json_dict['cost_feature'] = True
                        rec.cost = tax_totals_json_dict['amount_untaxed'] + tax_totals_json_dict[
                            'amount_untaxed'] * cost_percent / 100
                        final_cost = tax_totals_json_dict['amount_untaxed'] * cost_percent / 100

                        if final_cost > maximum_amount:
                            final_cost = maximum_amount

                        custom_tax_amount = final_cost + amount_total
                        office_cost_string = "Office Cost " + str(formated_percentage) + '%'
                        if amount_cost_perc > maximum_amount:

                            list_dict = {
                                "tax_group_name": office_cost_string,
                                "tax_group_amount": maximum_amount,
                                "tax_group_base_amount": amount_untaxed,
                                "formatted_tax_group_amount": formatLang(self.env, maximum_amount,
                                                                         currency_obj=currency),
                                "formatted_tax_group_base_amount": tax_totals_json_dict['formatted_amount_untaxed'],
                            }

                            tax_totals_json_dict['groups_by_subtotal1'] = {'Untaxed Amount1': []}
                            tax_totals_json_dict['groups_by_subtotal1']['Untaxed Amount1'].append(list_dict)
                        else:

                            list_dict = {
                                "tax_group_name": office_cost_string,
                                "tax_group_amount": final_cost,
                                "tax_group_base_amount": amount_untaxed,
                                "formatted_tax_group_amount": formatLang(self.env, final_cost,
                                                                         currency_obj=currency),
                                "formatted_tax_group_base_amount": tax_totals_json_dict['formatted_amount_untaxed'],

                            }
                            tax_totals_json_dict['groups_by_subtotal1'] = {'Untaxed Amount1': []}
                            tax_totals_json_dict['groups_by_subtotal1']['Untaxed Amount1'].append(list_dict)

                        # if tax_totals_json_dict.get('groups_by_subtotal', False):
                        #     if tax_totals_json_dict.get('groups_by_subtotal', False).get('Untaxed Amount', False):
                        #         if tax_totals_json_dict.get('groups_by_subtotal', False).get('Untaxed Amount', False)[0].get('tax_group_amount', False):
                        #
                        #             tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0][
                        #                 'formatted_tax_group_base_amount_custom'] = formatLang(self.env, tax_totals_json_dict[
                        #                 'groups_by_subtotal']['Untaxed Amount'][0]['tax_group_amount'],
                        #                                                                        currency_obj=currency)
                        #
                        #             tax = tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0]['tax_group_amount']
                        #
                        #             # TAX GROUP BASE AMOUNT + COST PERCENTAGE
                        #             old_tax_group_base_amount = tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0]['tax_group_base_amount']
                        #
                        #             new_tax_base_amount = old_tax_group_base_amount + (maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc)
                        #
                        #             # tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0]['tax_group_base_amount'] += (maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc)
                        #
                        #             tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0]['formatted_tax_group_base_amount'] = formatLang(self.env, new_tax_base_amount,
                        #                        currency_obj=currency)
                        #
                        #
                        #             # MADE A TAX GROUP BASE AMOUNT FORMAT
                        #             # tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0][
                        #             #     'formatted_tax_group_base_amount'] = formatLang(self.env, tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0]['tax_group_base_amount'],
                        #             #                                                currency_obj=currency)
                        #             total_tax = 0.0
                        #             for taxes in tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount']:
                        #                 if taxes.get('tax_group_amount', False):
                        #                     total_tax += float(taxes.get('tax_group_amount'))
                        #             # FINAL TOTAL CALCULATION
                        #             # tax_totals_json_dict['amount_total'] = amount_untaxed + (maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc) + tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0]['tax_group_amount']
                        #
                        #             tax_totals_json_dict['amount_total'] = amount_untaxed + (maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc) + total_tax
                        #             tax_totals_json_dict['formatted_amount_total'] = formatLang(self.env, tax_totals_json_dict['amount_total'],
                        #                                                             currency_obj=currency)
                        # else:
                        #     tax_totals_json_dict['amount_total'] = custom_tax_amount
                        #     tax_totals_json_dict['formatted_amount_total'] = formatLang(self.env,
                        #                                                                 tax_totals_json_dict['amount_total'],
                        #                                                                 currency_obj=currency)
                        rec.tax_totals_json = json.dumps(tax_totals_json_dict)
                # else:
                #     rec.tax_totals_json = None
        return res


    def _get_reconciled_invoices_partials(self):
        print("\n\n\n_get_reconciled_invoices_partials-----------------------move------------------------------")
        ''' Helper to retrieve the details about reconciled invoices.
        :return A list of tuple (partial, amount, invoice_line).
        '''
        self.ensure_one()
        pay_term_lines = self.line_ids\
            .filtered(lambda line: line.account_internal_type in ('receivable', 'payable'))
        invoice_partials = []
        office_cost_feature = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.office_cost') or False

        cost_percentage = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.percentage') or False

        max_amount = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.max_amount') or False

        cost_percent = float(cost_percentage)
        maximum_amount = float(max_amount)
        extra_amount = 0
        if office_cost_feature and cost_percentage:
            amount_cost_perc = self.amount_untaxed * cost_percent / 100
            # extra_amount = (maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc * (cost_percent / 100)) + (maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc)
            extra_amount = (maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc)



        for partial in pay_term_lines.matched_debit_ids:
            if partial.credit_amount_currency == partial.credit_amount_currency:
                final_amount_credit = partial.credit_amount_currency
            else:
                final_amount_credit = partial.credit_amount_currency
            invoice_partials.append((partial, final_amount_credit, partial.debit_move_id))
        for partial in pay_term_lines.matched_credit_ids:
            if partial.debit_amount_currency == partial.debit_amount_currency:
                final_amount_debit = partial.debit_amount_currency
            else:
                final_amount_debit = partial.debit_amount_currency + extra_amount
            invoice_partials.append((partial, final_amount_debit, partial.credit_move_id))


        return invoice_partials

    def _compute_custom_tax(self):
        print("\n\n\n_compute_custom_tax-------------------------move-----------------------")
        currency = self.env.company.currency_id

        # For the computation of move lines, we could have a negative base value.
        # In this case, compute all with positive values and negate them at the end.

        total_tax = 0.0
        amount_total = 0.0
        amount_untaxed = 0.0

        basic_taxes = {}
        for line in self.invoice_line_ids:
            price_unit = line.price_unit
            quantity = line.quantity
            base = currency.round(price_unit * quantity)
            amount_untaxed += base
            amount_total += base
            sign = 1
            if currency.is_zero(base):
                sign = self._context.get('force_sign', 1)
            elif base < 0:
                sign = -1
            if base < 0:
                base = -base
            for tax in line.tax_ids:
                product = None
                partner = None
                quantity = 1
                total_tax += tax.with_context(force_price_include=False)._compute_amount(
                    base, sign * price_unit, quantity, product, partner, custom=True)
        amount_total = amount_untaxed + total_tax

        basic_taxes['mod_total_tax'] = total_tax
        basic_taxes['mod_total_tax_format'] = formatLang(self.env, total_tax,
                                                         currency_obj=currency)

        basic_taxes['mod_amount_total'] = amount_total

        basic_taxes['mod_amount_total_format'] = formatLang(self.env, amount_total,
                                                            currency_obj=currency)

        basic_taxes['mod_amount_untaxed'] = amount_untaxed

        basic_taxes['mod_amount_untaxed_format'] = formatLang(self.env, amount_untaxed,
                                                              currency_obj=currency)

        ''

        return basic_taxes

    def _recompute_tax_lines(self, recompute_tax_base_amount=False, tax_rep_lines_to_recompute=None):
        print("\n\n\n_recompute_tax_lines-----------------------move---------------------------------")
        """ Compute the dynamic tax lines of the journal entry.

        :param recompute_tax_base_amount: Flag forcing only the recomputation of the `tax_base_amount` field.
        """

        self.ensure_one()
        in_draft_mode = self != self._origin

        def _serialize_tax_grouping_key(grouping_dict):
            print("\n\n\n_serialize_tax_grouping_key------------------move-----------------------------")
            ''' Serialize the dictionary values to be used in the taxes_map.
            :param grouping_dict: The values returned by '_get_tax_grouping_key_from_tax_line' or '_get_tax_grouping_key_from_base_line'.
            :return: A string representing the values.
            '''
            return '-'.join(str(v) for v in grouping_dict.values())

        def _compute_base_line_taxes(base_line):
            print("\n\n\n_compute_base_line_taxes----------------move---------------------------------")
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
            total_lines = len(move.invoice_line_ids.filtered(lambda line: line.tax_ids))
            context_dict = {'total_lines':total_lines,'force_sign':move._get_tax_force_sign()}

            return base_line.tax_ids._origin.with_context(context_dict).compute_all(
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
        for line in self.line_ids.filtered(lambda line: not line.tax_repartition_line_id):
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
                taxes_map_entry['amount'] += tax_vals['amount']
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
