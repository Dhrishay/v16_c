# -*- encoding: utf-8 -*-
from odoo import models, fields, api,_

class MrpBom(models.Model):
    _inherit = "mrp.bom"

    engineering_code = fields.Char(string='Part Number', related='product_tmpl_id.engineering_code')
