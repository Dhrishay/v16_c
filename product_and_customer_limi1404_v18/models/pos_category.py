# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class PosCategory(models.Model):
    _inherit = "pos.category"

    @api.model
    def _load_pos_data_domain(self, data):
        print("\n\n\n_load_pos_data_domain----------------------------------------------")
        print("data------------------------",data.keys())
        config_id = self.env['pos.config'].browse(data['pos.config']['data'][0]['id'])
        print("config_id-------------------------------",config_id)
        # print("data-------------------------------",data)
        # Load categories according to loaded products
        product_catg_ids = []
        for product in data['product.product']['data']:
            product_catg_ids += product['pos_categ_ids']
        # print("config_id.limit_categories-------------------------",config_id.limit_categories)
        # print("config_id.iface_available_categ_ids-------------------------",config_id.iface_available_categ_ids)
        # print("config_id.product_load_background-------------------------",config_id.product_load_background)
        # print("config_id.limited_products_loading-------------------------",config_id.limited_products_loading)
        if config_id.limit_categories and config_id.iface_available_categ_ids and config_id.product_load_background and config_id.limited_products_loading:
            print("if*****************")
            product_catg_ids = config_id._get_available_categories().ids
            print("product_catg_ids---------------------------------",product_catg_ids)
        elif config_id.limit_categories and config_id.iface_available_categ_ids and not config_id.product_load_background and not config_id.limited_products_loading:
            print("else************************")
            category_ids = config_id._get_available_categories().ids
            print("category_ids-----------------------------",category_ids)
            product_catg_ids = list(set(product_catg_ids) & set(category_ids))
            print("product_catg_ids-----------------------------",product_catg_ids)
        a = [('id', 'in', product_catg_ids)]
        print("a--------------------------",a)
        print("product_catg_ids--------------------------",product_catg_ids)
        return [('id', 'in', product_catg_ids)]