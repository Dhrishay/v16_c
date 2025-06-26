# -*- coding: utf-8 -*-

import logging
from odoo.addons.sale.models.payment_transaction import PaymentTransaction as ExtendPaymentTransaction

_logger = logging.getLogger(__name__)


def _set_pending(self, state_message=None):
    """ Override of `payment` to send the quotations automatically.

    :param str state_message: The reason for which the transaction is set in 'pending' state.
    :return: updated transactions.
    :rtype: `payment.transaction` recordset.
    """
    txs_to_process = super(ExtendPaymentTransaction,self)._set_pending(state_message=state_message)

    for tx in txs_to_process:  # Consider only transactions that are indeed set pending.
        sales_orders = tx.sale_order_ids.filtered(lambda so: so.state in ['draft', 'sent'])
        sales_orders.filtered(
            lambda so: so.state == 'draft'
        ).with_context(tracking_disable=True).action_quotation_sent()

        if tx.provider_id.code == 'custom':
            for so in tx.sale_order_ids:
                so.reference = tx._compute_sale_order_reference(so)
        # send order confirmation mail.
        if tx.provider_id.code == 'custom':
            sales_orders.with_context(website_order = True).action_confirm()
            # pass
            # sales_orders._send_order_confirmation_mail()
        else:
            sales_orders._send_order_confirmation_mail()
    return super(ExtendPaymentTransaction, self)._set_pending(state_message=state_message)


ExtendPaymentTransaction._set_pending = _set_pending