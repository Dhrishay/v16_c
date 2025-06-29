# -*- coding: utf-8 -*-
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_proforma_downloaded = fields.Boolean(copy=False)

    def action_is_proforma_downloaded(self):
        return 1