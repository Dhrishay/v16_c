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
        # print("\n\n\n_find_mail_template---------------------------------------------")
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

    @api.depends('order_line.price_total')
    def _amount_all(self):
        # print("\n\n\n_amount_all----------------customized--------------------------")
        """
        Compute the total amounts of the SO.
        """
        office_cost_feature = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.office_cost') or False
        # print("office_cost_feature-----------------------------",office_cost_feature)

        cost_percentage = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.percentage') or False
        # print("cost_percentage-----------------------------", cost_percentage)

        max_amount = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.max_amount') or False
        # print("max_amount-----------------------------", max_amount)

        cost_percent = float(cost_percentage)
        # print("cost_percent-----------------------------", cost_percent)
        maximum_amount = float(max_amount)
        # print("maximum_amount-----------------------------", maximum_amount)


        extra_amount = 0
        for order in self:
            # print("order-------------------",order)
            office_total_tax = 0
            # print("office_total_tax-------------------",office_total_tax)
            amount_untaxed = amount_tax = 0.0
            # print("amount_untaxed-------------------",amount_untaxed)
            for line in order.order_line:
                # print("line------------------------------",line)
                amount_untaxed += line.price_subtotal
                # print("amount_untaxed------------------------------",amount_untaxed)
                amount_tax += line.price_tax
                # print("amount_tax------------------------------",amount_tax)
            t = 0
            if office_cost_feature and cost_percentage:
                # print("if ********************************")

                tax_ids = []
                t = 0
                max_amount = False
                counter = len(order.order_line)
                # print("counter-------------------------",counter)
                for line in order.order_line:
                    # print("lin------------------------",line)
                    amount_cost_perc = line.price_subtotal * cost_percent / 100
                    # print("line.price_subtotal-------------------------------",line.price_subtotal)
                    # print("cost_percent-------------------------------",cost_percent)
                    # print("amount_cost_perc-------------------------------",amount_cost_perc)
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
                    # print("extra-------------amount---------------",extra_amount)
                    if line.tax_id:
                        # print("if3333333333333333333")
                        for each_tax in line.tax_id:
                            # print("each_tax---------------------------",each_tax)
                            if max_amount:
                                office_cost_amount = each_tax.compute_all((extra_amount / counter))
                                # print("office_cost_amount-------------111--------------------", office_cost_amount)
                            else:
                                office_cost_amount = each_tax.compute_all(extra_amount)
                                # print("office_cost_amount-------------2222--------------------", office_cost_amount)
                            for line_tax in office_cost_amount:
                                # print("for *******************")
                                # print("line_tax---------------------------", line_tax)
                                if 'taxes' in line_tax:
                                    for line in office_cost_amount['taxes']:
                                        office_total_tax = office_total_tax + line['amount']
                                        # print("office_total_tax----------------------------", office_total_tax)
            self.sale_tax = office_total_tax
            # print("self.sale_tax-----------------------------------",self.sale_tax)
            order.update({
                'amount_untaxed': amount_untaxed ,
                'amount_tax': amount_tax + office_total_tax,
                'amount_total': amount_untaxed + amount_tax +  t + office_total_tax,
            })
            # print("amount_untaxed--------------------------------------",amount_untaxed)
            # print("amount_tax--------------------------------------",amount_tax + office_total_tax)
            # print("amount_tax--------------------------------------",amount_tax + office_total_tax)
            # print("amount_total--------------------------------------",amount_untaxed + amount_tax +  t + office_total_tax)

    @api.depends_context('lang')
    @api.depends('order_line.tax_id', 'order_line.price_unit', 'amount_total', 'amount_untaxed')
    def _compute_tax_totals_json(self):
        print("\n\n\n_compute_tax_totals_json-----------1st-----------------------------")
        total_amt = 0

        def compute_taxes(order_line):
            print("\n\n\ncompute_taxes-----------------1st-------------------------------")
            print("order_line------------------------------------------------",order_line)
            self.sale_tax = 0
            price = order_line.price_unit * (1 - (order_line.discount or 0.0) / 100.0)
            order = order_line.order_id
            res = order_line.tax_id._origin.compute_all(price, order.currency_id, order_line.product_uom_qty,
                                                         product=order_line.product_id,
                                                         partner=order.partner_shipping_id)
            office_cost_feature = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.office_cost') or False

            cost_percentage = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.percentage') or False

            max_amount = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.max_amount') or False
            cost_percent = float(cost_percentage)
            maximum_amount = float(max_amount)
            add_amount = 0
            max_amt = False
            counter = len(order.order_line)
            # print("counter---------------------------------",counter)
            if office_cost_feature and cost_percentage:
                amount_cost_perc = order_line.price_subtotal * cost_percent / 100
                # print("amount_cost_perc---------------------------------",amount_cost_perc)
                if amount_cost_perc > maximum_amount and maximum_amount > 0:
                    # print("if 11111111111111111111")
                    max_amt = True
                    # print("max_amt---------------------------",max_amt)
                if maximum_amount > 0:
                    # print("if 2222222222222222222")
                    extra_amount = maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc
                    # print("extra_amount---------------------------", extra_amount)
                else:
                    # print("else -----------------------")
                    extra_amount = amount_cost_perc
                total_amt = extra_amount
                # print("total_amt-----------------------------------------",total_amt)
                if extra_amount > 0:
                    # print("\nif ***********************")
                    if max_amt:
                        # print("if 2222211111111")
                        add_amount = (extra_amount/counter) * cost_percent / 100
                        # print("add_amount------------------------------",add_amount)
                    else:
                        # print("else 22222222222")
                        add_amount = extra_amount * cost_percent / 100
                        # print("add_amount--------------add----------------", add_amount)
                    total_amt += add_amount
                    # print("total_amt-------------------??>>>>>--total---------",total_amt)

            if res and res.get('taxes'):
                # print("if final ****************************")
                # print("res----------------************------------",res)
                res['taxes'][0]['amount'] += add_amount
                # print("res['taxes'][0]['amount']-----------------------------",res['taxes'][0]['amount'])
            return res

        account_move = self.env['account.move']
        for order in self:
            tax_lines_data = account_move._prepare_tax_lines_data_for_totals_from_object(order.order_line, compute_taxes)
            # print("order.order_line---------------------------------------",order.order_line)
            # print("compute_taxes---------------------------------------",compute_taxes)
            # print("tax_lines_data---------------------------------------",tax_lines_data)
            tax_totals = account_move.with_context(sale_mode=True)._get_tax_totals(order.partner_id, tax_lines_data, order.amount_total, order.amount_untaxed, order.currency_id)
            # print("tax_totals---------------------------------------",tax_totals)
            order.tax_totals_json = json.dumps(tax_totals)