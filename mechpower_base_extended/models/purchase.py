from odoo import models, fields, _
from odoo.tools import format_date
from random import randint


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    purchase_group_ids = fields.Many2many('purchase.group')

class PurchaseGroup(models.Model):
    _name = 'purchase.group'
    _description = 'Purchase Group'
    _rec_name = 'name'

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color', default=_get_default_color)