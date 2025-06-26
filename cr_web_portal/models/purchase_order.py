# -*- coding: utf-8 -*-
from odoo.http import request
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


import random

from odoo.fields import Command

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def get_orderline_product(self):
        order_lines = self.order_line.filtered(lambda x:  not x.display_type)
        return [so_line.product_id.name for so_line in order_lines] if order_lines else False

    def get_orederline_product_qty(self):
        order_lines = self.order_line.filtered(lambda x:  not x.display_type)
        return sum([int(line.product_qty) for line in order_lines]) if order_lines else False