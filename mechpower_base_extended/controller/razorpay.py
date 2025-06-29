# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.addons.payment_razorpay.controllers.main import RazorpayController
from odoo import http
from odoo.http import request
import pprint
import logging

_logger = logging.getLogger(__name__)

class CustomRazorpayController(RazorpayController):
    _return_url = '/payment/razorpay/return'

    @http.route(
        _return_url, type='http', auth='public', methods=['GET', 'POST'], csrf=False,
        save_session=False
    )
    def razorpay_return_from_checkout(self, reference, **data):
        """ Process the notification data sent by Razorpay after redirection from checkout.

        :param str reference: The transaction reference embedded in the return URL.
        :param dict data: The notification data.
        """
        if not data and reference:
            tx_sudo = request.env['payment.transaction'].sudo().search([('reference', '=', reference)])
            if tx_sudo:
                tx_sudo._set_canceled()
        _logger.info("Handling redirection from Razorpay with data:\n%s", pprint.pformat(data))
        if all(f'razorpay_{key}' in data for key in ('order_id', 'payment_id', 'signature')):
            # Check the integrity of the notification.
            tx_sudo = request.env['payment.transaction'].sudo()._get_tx_from_notification_data(
                'razorpay', {'description': reference}
            )  # Use the same key as for webhook notifications' data.
            self._verify_notification_signature(data, data.get('razorpay_signature'), tx_sudo)

            # Handle the notification data.
            tx_sudo._handle_notification_data('razorpay', data)
        else:  # The customer cancelled the payment or the payment failed.
            pass  # Don't try to process this case because the payment id was not provided.

        # Redirect the user to the status page.
        return request.redirect('/payment/status')