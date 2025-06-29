# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleCloseReasonWizard(models.TransientModel):
    _name = "sale.close.reason.wizard"
    _description = 'Sale Close Reason Wizard'

    close_reason_id = fields.Many2one("sale.close.reason", string="Cancellation Reason")

    def set_close(self):
        self.ensure_one()
        sale_order = self.env['sale.order'].browse(self.env.context.get('active_id'))
        sale_order.sale_close_reason_id = self.close_reason_id
        sale_order._action_cancel()
