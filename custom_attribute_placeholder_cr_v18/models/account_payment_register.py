# -*- coding: utf-8 -*-
from collections import defaultdict
from lxml import etree

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.tools import float_compare, frozendict


class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    @api.depends('source_amount', 'source_amount_currency', 'source_currency_id', 'company_id', 'currency_id',
                 'payment_date')
    def _compute_amount(self):
        office_cost_feature = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.office_cost') or False

        cost_percentage = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.percentage') or False

        max_amount = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.max_amount') or False

        cost_percent = float(cost_percentage)
        maximum_amount = float(max_amount)
        account_move = self.env['account.move'].browse(self._context.get('active_ids', []))
        amount_untaxed = account_move.amount_untaxed

        for wizard in self:
            if wizard.source_currency_id == wizard.currency_id:
                # Same currency.
                wizard.amount = wizard.source_amount_currency
            elif wizard.currency_id == wizard.company_id.currency_id:
                # Payment expressed on the company's currency.
                wizard.amount = wizard.source_amount
            else:
                # Foreign currency on payment different than the one set on the journal entries.
                amount_payment_currency = wizard.company_id.currency_id._convert(wizard.source_amount,
                                                                                 wizard.currency_id, wizard.company_id,
                                                                                 wizard.payment_date)
                wizard.amount = amount_payment_currency
        if office_cost_feature and cost_percentage:
            amount_cost_perc = amount_untaxed * cost_percent / 100
            wizard.amount = wizard.amount + (
                maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc)
            # wizard.amount = wizard.amount + (
            #     maximum_amount if amount_cost_perc > maximum_amount else account_move.amount_tax * (
            #                 cost_percent / 100)) + (
            #                     maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc)

    @api.depends('amount')
    def _compute_payment_difference(self):
        office_cost_feature = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.office_cost') or False

        cost_percentage = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.percentage') or False

        max_amount = self.env['ir.config_parameter'].sudo().get_param(
            'custom_attribute_placeholder_cr.max_amount') or False

        cost_percent = float(cost_percentage)
        maximum_amount = float(max_amount)
        account_move = self.env['account.move'].browse(self._context.get('active_ids', []))
        amount_untaxed = account_move.amount_untaxed

        for wizard in self:
            if wizard.source_currency_id == wizard.currency_id:
                # Same currency.
                wizard.payment_difference = wizard.source_amount_currency - wizard.amount
            elif wizard.currency_id == wizard.company_id.currency_id:
                # Payment expressed on the company's currency.
                wizard.payment_difference = wizard.source_amount - wizard.amount
            else:
                # Foreign currency on payment different than the one set on the journal entries.
                amount_payment_currency = wizard.company_id.currency_id._convert(wizard.source_amount,
                                                                                 wizard.currency_id, wizard.company_id,
                                                                                 wizard.payment_date)
                wizard.payment_difference = amount_payment_currency - wizard.amount

        if office_cost_feature and cost_percentage:
            amount_cost_perc = amount_untaxed * cost_percent / 100
            wizard.payment_difference = wizard.payment_difference + (
                maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc)
            # wizard.payment_difference = wizard.payment_difference + (
            #     maximum_amount if amount_cost_perc > maximum_amount else account_move.amount_tax * (
            #                 cost_percent / 100)) + (
            #                                 maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc)



