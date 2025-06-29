# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = "product.template"

    # manuf_ok = fields.Boolean()

    # @api.model
    # def _search_get_detail(self, website, order, options):
    #     res = super()._search_get_detail(website, order, options)
    #     print("++++++res++++++ddd+",res)
    #     # 5/0
    #     if res and res['fetch_fields']:
    #         res['fetch_fields'].append('product_variant_count')
    #     if res and res['mapping']:
    #         res['mapping'].update({'VariantCount': {'name': 'product_variant_count', 'type': 'html'}})
    #     return res
