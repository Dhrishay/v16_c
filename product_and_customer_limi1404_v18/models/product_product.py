# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import convert, SQL


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def pos_load_data(self, pos_session_id=False,offset=0, limit=None):
        print("\n\n\npos_load_data------------product-------------------------")
        if pos_session_id:
            response = {}
            pos_session_id = self.env['pos.session'].sudo().browse(pos_session_id)
            print("pos_session_id---------------------------------------------",pos_session_id)
            pos_config_id = pos_session_id.config_id
            print("pos_config_id-----------------------",pos_config_id)
            fields = set(self._load_pos_data_fields(pos_config_id.id))
            print("fields-------------------------",fields)
            taxes = self.env['account.tax'].search(self.env['account.tax']._check_company_domain(pos_config_id.company_id.id))
            print("taxes-----------------------------",taxes)
            product_fields = taxes._eval_taxes_computation_prepare_product_fields()
            print("product_fields-----------------------------",product_fields)
            fields = list(fields.union(product_fields))
            print("fields-----------------------------",fields)

            products = pos_config_id.with_context(display_default_code=False).get_products_loading_in_background(fields, offset, limit)
            print("products---------------------------------------",products)

            self._process_pos_ui_product_product(products, pos_config_id)
            response['product.product'] = {'data': products, 'fields': fields}
            print("response['product.product']-------------------------",response['product.product'])

            self.env['pos.session'].sudo()._load_pos_data_relations('product.product', response)
            print("response-----------------------------",response)

            return response
        else: return False