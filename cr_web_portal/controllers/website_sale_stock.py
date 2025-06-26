# -*- coding: utf-8 -*-

from odoo.addons.website_sale.controllers import main as website_sale_controller
import logging

from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.fields import Command
from odoo.http import request
from odoo.addons.payment.controllers.post_processing import PaymentPostProcessing
from odoo.exceptions import AccessError, MissingError, ValidationError

_logger = logging.getLogger(__name__)


class CustomPaymentPortal(website_sale_controller.PaymentPortal):

    # remove base condition which is if cart_qty > avl_qty then it shows error.
    @http.route()
    def shop_payment_transaction(self, order_id, access_token, **kwargs):
        order = request.website.sale_get_order()
        values = []
        for line in order.order_line:
            if line.product_id.type == 'product' and not line.product_id.allow_out_of_stock_order:
                cart_qty, avl_qty = order._get_cart_and_free_qty(line=line)
                # remove base condition which is if cart_qty > avl_qty then it shows error.


        if values:
            raise ValidationError(' '.join(values))

        try:
            order_sudo = self._document_check_access('sale.order', order_id, access_token)
        except MissingError as error:
            raise error
        except AccessError:
            raise ValidationError(_("The access token is invalid."))

        if order_sudo.state == "cancel":
            raise ValidationError(_("The order has been canceled."))

        kwargs.update({
            'reference_prefix': None,  # Allow the reference to be computed based on the order
            'partner_id': order_sudo.partner_invoice_id.id,
            'sale_order_id': order_id,  # Include the SO to allow Subscriptions to tokenize the tx
        })
        kwargs.pop('custom_create_values', None)  # Don't allow passing arbitrary create values
        if not kwargs.get('amount'):
            kwargs['amount'] = order_sudo.amount_total
        if 'isPartialPayment' in kwargs and kwargs.get('isPartialPayment'):
            amount_dict = order_sudo.get_payable_amount()
            if kwargs.get('amount') and (float(kwargs.get('amount')) < amount_dict.get('min') or float(kwargs.get('amount')) > amount_dict.get('max')):
                raise ValidationError(_("The cart has been updated. Please refresh the page."))
        else:
            if tools.float_compare(kwargs['amount'], order_sudo.amount_total,
                                   precision_rounding=order_sudo.currency_id.rounding):
                raise ValidationError(_("The cart has been updated. Please refresh the page."))

        tx_sudo = self._create_transaction(
            custom_create_values={'sale_order_ids': [Command.set([order_id])]}, **kwargs,
        )

        # Store the new transaction into the transaction list and if there's an old one, we remove
        # it until the day the ecommerce supports multiple orders at the same time.
        last_tx_id = request.session.get('__website_sale_last_tx_id')
        last_tx = request.env['payment.transaction'].browse(last_tx_id).sudo().exists()
        if last_tx:
            PaymentPostProcessing.remove_transactions(last_tx)
        request.session['__website_sale_last_tx_id'] = tx_sudo.id

        self._validate_transaction_for_order(tx_sudo, order_id)

        return tx_sudo._get_processing_values()

