# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from random import randint

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression


class ProductAttribute(models.Model):
    _inherit = "product.attribute"

    hide_in_product_detail_page = fields.Boolean(string='Hide in Product Detail Page',default=False)