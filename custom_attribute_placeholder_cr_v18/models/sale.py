# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, _
import json
from odoo.tools.misc import formatLang


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    cost = fields.Float("Cost")
    sale_tax = fields.Float("Sale tax")

    def _find_mail_template(self, force_confirmation_template=False):
        print("\n\n\n_find_mail_template---------------------------------------------")
        self.ensure_one()
        office_cost_feature = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.office_cost') or False

        template_id = False

        if force_confirmation_template or (self.state == 'sale' and not self.env.context.get('proforma', False)):
            if office_cost_feature:
                template_id = int(self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.default_confirmation_template_custom'))
            else:
                template_id = int(self.env['ir.config_parameter'].sudo().get_param('sale.default_confirmation_template'))
            template_id = self.env['mail.template'].search([('id', '=', template_id)]).id
            if not template_id:
                if office_cost_feature:
                    template_id = self.env['ir.model.data']._xmlid_to_res_id('custom_attribute_placeholder_cr.mail_template_sale_confirmation_custom', raise_if_not_found=False)
                else:
                    template_id = self.env['ir.model.data']._xmlid_to_res_id('sale.mail_template_sale_confirmation', raise_if_not_found=False)
        if not template_id:
            if office_cost_feature:
                template_id = self.env['ir.model.data']._xmlid_to_res_id('custom_attribute_placeholder_cr.email_template_edi_sale_custom', raise_if_not_found=False)
            else:
                template_id = self.env['ir.model.data']._xmlid_to_res_id('sale.email_template_edi_sale', raise_if_not_found=False)

        return template_id

    # done
    @api.depends('order_line.price_total')
    def _compute_amounts(self):
        print("\n\n\n_compute_amounts----------------1st--------------------------")
        """
        Compute the total amounts of the SO.
        """
        office_cost_feature = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.office_cost') or False

        cost_percentage = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.percentage') or False

        max_amount = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.max_amount') or False

        cost_percent = float(cost_percentage)
        maximum_amount = float(max_amount)

        extra_amount = 0
        for order in self:
            office_total_tax = 0
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            t = 0
            if office_cost_feature and cost_percentage:
                tax_ids = []
                t = 0
                max_amount = False
                counter = len(order.order_line)
                for line in order.order_line:
                    amount_cost_perc = line.price_subtotal * cost_percent / 100
                    if amount_cost_perc > maximum_amount and maximum_amount > 0:
                        max_amount = True
                    if maximum_amount > 0:
                        extra_amount = maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc
                    else:
                        extra_amount = amount_cost_perc
                    if max_amount and t == 0:
                        t += extra_amount
                    elif max_amount:
                        t = extra_amount
                    else:
                        t += extra_amount
                    if line.tax_id:
                        for each_tax in line.tax_id:
                            if max_amount:
                                office_cost_amount = each_tax.compute_all((extra_amount / counter))
                            else:
                                office_cost_amount = each_tax.compute_all(extra_amount)
                            for line_tax in office_cost_amount:
                                if 'taxes' in line_tax:
                                    for line in office_cost_amount['taxes']:
                                        office_total_tax = office_total_tax + line['amount']
            self.sale_tax = office_total_tax
            order.update({
                'amount_untaxed': amount_untaxed ,
                'amount_tax': amount_tax + office_total_tax,
                'amount_total': amount_untaxed + amount_tax +  t + office_total_tax,
            })

    # @api.depends_context('lang')
    # @api.depends('order_line.tax_id', 'order_line.price_unit', 'amount_total', 'amount_untaxed')
    # def _compute_tax_totals_json(self):
    #     print("\n\n\n_compute_tax_totals_json----------------------------------------")
    #     total_amt = 0
    #
    #     def compute_taxes(order_line):
    #         print("\n\n\ncompute_taxes------------------------------------------------")
    #         self.sale_tax = 0
    #         price = order_line.price_unit * (1 - (order_line.discount or 0.0) / 100.0)
    #         order = order_line.order_id
    #         res = order_line.tax_id._origin.compute_all(price, order.currency_id, order_line.product_uom_qty,
    #                                                      product=order_line.product_id,
    #                                                      partner=order.partner_shipping_id)
    #         office_cost_feature = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.office_cost') or False
    #
    #         cost_percentage = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.percentage') or False
    #
    #         max_amount = self.env['ir.config_parameter'].sudo().get_param(
    #             'custom_attribute_placeholder_cr.max_amount') or False
    #         cost_percent = float(cost_percentage)
    #         maximum_amount = float(max_amount)
    #         add_amount = 0
    #         max_amt = False
    #         counter = len(order.order_line)
    #         if office_cost_feature and cost_percentage:
    #             amount_cost_perc = order_line.price_subtotal * cost_percent / 100
    #             if amount_cost_perc > maximum_amount and maximum_amount > 0:
    #                 max_amt = True
    #             if maximum_amount > 0:
    #                 extra_amount = maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc
    #             else:
    #                 extra_amount = amount_cost_perc
    #             total_amt = extra_amount
    #             if extra_amount > 0:
    #                 if max_amt:
    #                     add_amount = (extra_amount/counter) * cost_percent / 100
    #                 else:
    #                     add_amount = extra_amount * cost_percent / 100
    #                 total_amt += add_amount
    #
    #         if res and res.get('taxes'):
    #             res['taxes'][0]['amount'] += add_amount
    #         return res
    #
    #     account_move = self.env['account.move']
    #     for order in self:
    #         tax_lines_data = account_move._prepare_tax_lines_data_for_totals_from_object(order.order_line,
    #                                                                                      compute_taxes)
    #         tax_totals = account_move.with_context(sale_mode=True)._get_tax_totals(order.partner_id, tax_lines_data, order.amount_total,
    #                                                   order.amount_untaxed, order.currency_id)
    #         order.tax_totals_json = json.dumps(tax_totals)



    @api.depends_context('lang')
    @api.depends('order_line.price_subtotal', 'currency_id', 'company_id')
    def _compute_tax_totals(self):
        print("\n\n\n_compute_tax_totals------------customize-----------------------")
        AccountTax = self.env['account.tax']

        for order in self:
            order_lines = order.order_line.filtered(lambda x: not x.display_type)
            base_lines = [line._prepare_base_line_for_taxes_computation() for line in order_lines]

            AccountTax._add_tax_details_in_base_lines(base_lines, order.company_id)
            AccountTax._round_base_lines_tax_details(base_lines, order.company_id)

            # total_office_cost =  + sum(item.get('office_cost', 0.0) for item in base_lines)
            # print("total_office_cost----------------------------------------",total_office_cost)

            order.tax_totals = AccountTax._get_tax_totals_summary(
                base_lines=base_lines,
                currency=order.currency_id or order.company_id.currency_id,
                company=order.company_id,
            )

            order.tax_totals['total_amount_currency'] = order.tax_totals['total_amount_currency'] + order.tax_totals['office_cost']
