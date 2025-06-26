# -*- coding: utf-8 -*-
from odoo.http import request
from odoo.addons.website_sale_delivery.controllers.main import WebsiteSaleDelivery

class WebsiteSaleAdvancePayment(WebsiteSaleDelivery):

    def _update_website_sale_delivery_return(self, order, **post):
        Monetary = request.env['ir.qweb.field.monetary']
        carrier_id = int(post['carrier_id'])
        currency = order.currency_id
        if order:
            min = 0.00
            max = 0.00
            advance_payment = 0.00
            if order.payment_term_id:
                for record in order.payment_term_id:
                    percent_ids = record.line_ids.filtered(lambda x: x.value == 'percent')
                    if percent_ids:
                        percentage = percent_ids[0].value_amount
                        payable_amount = ((order.amount_total) * percentage) / 100
                        min =  round(float(payable_amount), 2)
                        max = round(float(order.amount_total), 2)
                        advance_payment = round(float(payable_amount), 2)
                    else:
                        min = round(float(order.amount_total), 2)
                        max = round(float(order.amount_total), 2)
                        advance_payment = round(float(order.amount_total), 2)
            else:
                min = round(float(order.amount_total), 2)
                max = round(float(order.amount_total), 2)
                advance_payment = round(float(order.amount_total), 2)
            return {
                'status': order.delivery_rating_success,
                'error_message': order.delivery_message,
                'carrier_id': carrier_id,
                'is_free_delivery': not bool(order.amount_delivery),
                'new_amount_delivery': Monetary.value_to_html(order.amount_delivery, {'display_currency': currency}),
                'new_amount_untaxed': Monetary.value_to_html(order.amount_untaxed, {'display_currency': currency}),
                'new_amount_tax': Monetary.value_to_html(order.amount_tax, {'display_currency': currency}),
                'new_amount_total': Monetary.value_to_html(order.amount_total, {'display_currency': currency}),
                'new_amount_total_raw': order.amount_total,
                'min':min,
                'max':max,
                'advance_payment':advance_payment,
            }
        return {}