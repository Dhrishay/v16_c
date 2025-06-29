# models/sale_order_line.py

from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    sequence_number = fields.Integer(string='Sequence Number', readonly=True)

    def _compute_sequence_number(self):
        sequence_number = 1
        for line in self:
            line.sequence_number = sequence_number
            sequence_number += 1
