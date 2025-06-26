import logging
from pay_ccavenue import CCAvenue
from odoo import api, models, _
from odoo.exceptions import ValidationError
from odoo.addons.payment import utils as payment_utils
from odoo import api, SUPERUSER_ID
from odoo.tools import format_amount

_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _set_done(self, state_message=None):
        allowed_states = ('draft', 'pending', 'authorized', 'error', 'cancel')  # 'cancel' for Payulatam
        target_state = 'done'
        txs_to_process = self._update_state(allowed_states, target_state, state_message)
        txs_to_process._log_received_message()
        user = self.env.user
        if len(self.sale_order_ids) == 1:
            so_id = self.sale_order_ids
            mail_template = self.env.ref('cr_web_portal.payment_confirmation_mail_template', raise_if_not_found=False)
            if user and mail_template:
                so_id.with_context(so_id=so_id,transaction_id=self,force_send=True).message_post_with_template(mail_template.id,email_layout_xmlid='mail.mail_notification_light')
        return txs_to_process

    def _check_amount_and_confirm_order(self):
        """ Confirm the sales order based on the amount of a transaction.

        Confirm the sales orders only if the transaction amount is equal to the total amount of the
        sales orders. Neither partial payments nor grouped payments (paying multiple sales orders in
        one transaction) are not supported.

        :return: The confirmed sales orders.
        :rtype: a `sale.order` recordset
        """
        confirmed_orders = self.env['sale.order']
        for tx in self:
            # We only support the flow where exactly one quotation is linked to a transaction and
            # vice versa.
            if len(tx.sale_order_ids) == 1:
                quotation = tx.sale_order_ids.filtered(lambda so: so.state in ('draft', 'sent'))
                if quotation and len(quotation.transaction_ids.filtered(
                    lambda tx: tx.state in ('authorized', 'done')  # Only consider confirmed tx
                )) == 1:
                    # Check if the SO is fully paid
                    if quotation.currency_id.compare_amounts(tx.amount, quotation.amount_total) == 0:
                        quotation.with_context(send_email=True, portal_order=True).action_confirm()
                        confirmed_orders |= quotation
                    else:
                        quotation.with_context(send_email=True, portal_order=True).action_confirm()
                        confirmed_orders |= quotation
                        _logger.warning(
                            '<%(provider)s> transaction AMOUNT MISMATCH for order %(so_name)s '
                            '(ID %(so_id)s): expected %(so_amount)s, got %(tx_amount)s', {
                                'provider': tx.provider_code,
                                'so_name': quotation.name,
                                'so_id': quotation.id,
                                'so_amount': format_amount(
                                    quotation.env, quotation.amount_total, quotation.currency_id
                                ),
                                'tx_amount': format_amount(tx.env, tx.amount, tx.currency_id),
                            },
                        )
        return confirmed_orders