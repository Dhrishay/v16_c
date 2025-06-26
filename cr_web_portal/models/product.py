# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from datetime import datetime, timedelta
from collections import defaultdict
from odoo.addons.http_routing.models.ir_http import slug
from odoo import api, fields, models, tools, _

COLORS = [
    ('black', 'Black'),
    ('blue', 'Blue'),
    ('white', 'White'),
    ('orange', 'Orange'),
    ('yellow', 'Yellow'),
    ('green', 'Green'),
    ('grey', 'Grey'),
    ('red', 'Red'),
    ('natural', 'Natural'),
]


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _search_get_detail(self, website, order, options):
        with_image = options['displayImage']
        with_description = options['displayDescription']
        with_category = options['displayExtraLink']
        with_price = options['displayDetail']
        domains = [website.sale_product_domain()]
        category = options.get('category')
        min_price = options.get('min_price')
        max_price = options.get('max_price')
        attrib_values = options.get('attrib_values')
        if category:
            domains.append([('public_categ_ids', 'in', category)])
        if min_price:
            domains.append([('list_price', '>=', min_price)])
        if max_price:
            domains.append([('list_price', '<=', max_price)])
        if attrib_values:
            attrib = None
            ids = []
            for value in attrib_values:
                if not attrib:
                    attrib = value[0]
                    ids.append(value[1])
                elif value[0] == attrib:
                    ids.append(value[1])
                else:
                    domains.append([('attribute_line_ids.value_ids', 'in', ids)])
                    attrib = value[0]
                    ids = [value[1]]
            if attrib:
                domains.append([('attribute_line_ids.value_ids', 'in', ids)])
        search_fields = ['name', 'default_code', 'product_variant_ids.default_code']
        fetch_fields = ['id', 'name', 'website_url','product_variant_count']
        mapping = {
            'id': {'name': 'id', 'type': 'int', 'match': False},
            'name': {'name': 'name', 'type': 'text', 'match': True},
            'default_code': {'name': 'default_code', 'type': 'text', 'match': True},
            'product_variant_ids.default_code': {'name': 'product_variant_ids.default_code', 'type': 'text', 'match': True},
            'website_url': {'name': 'website_url', 'type': 'text', 'truncate': False},
            'VariantCount':{'name': 'product_variant_count', 'type': 'html'}
        }
        if with_image:
            mapping['image_url'] = {'name': 'image_url', 'type': 'html'}
        if with_description:
            # Internal note is not part of the rendering.
            search_fields.append('description')
            fetch_fields.append('description')
            search_fields.append('description_sale')
            fetch_fields.append('description_sale')
            mapping['description'] = {'name': 'description_sale', 'type': 'text', 'match': True}
        if with_price:
            mapping['detail'] = {'name': 'price', 'type': 'html', 'display_currency': options['display_currency']}
            mapping['detail_strike'] = {'name': 'list_price', 'type': 'html', 'display_currency': options['display_currency']}
        if with_category:
            mapping['extra_link'] = {'name': 'category', 'type': 'html'}
        return {
            'model': 'product.template',
            'base_domain': domains,
            'search_fields': search_fields,
            'fetch_fields': fetch_fields,
            'mapping': mapping,
            'icon': 'fa-shopping-cart',
        }

    def _search_render_results(self, fetch_fields, mapping, icon, limit):
        with_image = 'image_url' in mapping
        with_category = 'extra_link' in mapping
        with_price = 'detail' in mapping
        results_data = super()._search_render_results(fetch_fields, mapping, icon, limit)
        current_website = self.env['website'].get_current_website()
        for product, data in zip(self, results_data):
            categ_ids = product.public_categ_ids.filtered(lambda c: not c.website_id or c.website_id == current_website)
            if with_price:
                combination_info = product._get_combination_info(only_template=True)
                data['price'], list_price = self._search_render_results_prices(
                    mapping, combination_info
                )
                if list_price:
                    data['list_price'] = list_price
            if with_image:
                product_tmpl_id = self.browse(int(data['id']))
                product_variant_id = product_tmpl_id._get_first_possible_variant_id()
                product_id = self.env['product.product'].sudo().browse(int(product_variant_id))
                image = product_id._get_image_holder()
                data['image_url'] = '/web/image/%s/%s/image_1920' % (image._name, image.id)
            if with_category and categ_ids:
                data['category'] = self.env['ir.ui.view'].sudo()._render_template(
                    "website_sale.product_category_extra_link",
                    {'categories': categ_ids, 'slug': slug}
                )
        return results_data

    def _get_sales_prices(self, pricelist):
        pricelist.ensure_one()
        partner_sudo = self.env.user.partner_id

        # Try to fetch geoip based fpos or fallback on partner one
        fpos_id = self.env['website']._get_current_fiscal_position_id(partner_sudo)
        fiscal_position = self.env['account.fiscal.position'].sudo().browse(fpos_id)

        sales_prices = pricelist._get_products_price(self, 1.0)
        show_discount = pricelist.discount_policy == 'without_discount'
        show_strike_price = self.env.user.has_group('website_sale.group_product_price_comparison')

        base_sales_prices = self.price_compute('list_price', currency=pricelist.currency_id)

        res = {}
        for template in self:
            price_reduce = sales_prices[template.id]

            product_taxes = template.sudo().taxes_id.filtered(lambda t: t.company_id == t.env.company)
            taxes = fiscal_position.map_tax(product_taxes)

            template_price_vals = {
                'price_reduce': price_reduce
            }
            base_price = None
            price_list_contains_template = pricelist.currency_id.compare_amounts(price_reduce, base_sales_prices[template.id]) != 0

            if template.compare_list_price and show_strike_price:
                # The base_price becomes the compare list price and the price_reduce becomes the price
                base_price = template.compare_list_price
                if not price_list_contains_template:
                    price_reduce = base_sales_prices[template.id]
                    template_price_vals.update(price_reduce=price_reduce)
                if template.currency_id != pricelist.currency_id:
                    base_price = template.currency_id._convert(
                        base_price,
                        pricelist.currency_id,
                        self.env.company,
                        fields.Datetime.now(),
                        round=False
                    )
            elif show_discount and price_list_contains_template:
                base_price = base_sales_prices[template.id]

            if base_price and base_price != price_reduce:
                if not template.compare_list_price:
                    # Compare_list_price are never tax included
                    base_price = self._price_with_tax_computed(
                        base_price, product_taxes, taxes, self.env.company.id,
                        pricelist, template, partner_sudo,
                    )
                template_price_vals['base_price'] = base_price

            pricelist_ids = self.env['product.pricelist.item'].search([('product_tmpl_id', '=', template.id), ('pricelist_id', '=', pricelist.id), ('fixed_price', '>', 0)])
            if pricelist_ids.mapped('fixed_price'):
                template_price_vals['price_reduce'] = min(pricelist_ids.mapped('fixed_price'))
            template_price_vals['price_reduce'] = self._price_with_tax_computed(
                template_price_vals['price_reduce'], product_taxes, taxes, self.env.company.id,
                pricelist, template, partner_sudo,
            )

            res[template.id] = template_price_vals

        return res


class ProductProduct(models.Model):
    _inherit = 'product.product'

    is_customisable = fields.Boolean('Can be Customize', store=True)
    is_home_page_product = fields.Boolean('Homepage Product', store=True)
    is_mech_product = fields.Boolean('Mech Product', store=True)
    is_ital_product = fields.Boolean('Italtronics Product', store=True)
    product_template_variant_value_ids = fields.Many2many('product.template.attribute.value',
                                                          relation='product_variant_combination',
                                                          domain=[('attribute_line_id.value_count', '>', 0)],
                                                          string="Variant Values", ondelete='restrict')
    source_internal_ref = fields.Char("Source Internal Ref")
    is_enclosure_service = fields.Boolean('Enclosure')
    is_fdm_service = fields.Boolean('FDM')
    is_projection_service = fields.Boolean('Projection')
    is_metal_feb_service = fields.Boolean('Sheet Metal Fabrication')
    is_injection_mold_service = fields.Boolean('Injection Modeling')
    is_cnc_machining_service = fields.Boolean('CNC Machining')
    # enclosure design service questions

    enclosure_design_product_name = fields.Char('Product Name', tracking=True)
    enclosure_design_product_purpose = fields.Text('What is the purpose of the electronic product', tracking=True)
    enclosure_design_product_features = fields.Text('What are the main functionalities and features of the product',
                                                    tracking=True)
    enclosure_design_product_dimensions = fields.Text(
        'What are the dimensions of the electronic components that will be housed inside the enclosure', tracking=True)
    enclosure_design_product_dimensions_length = fields.Text('Product Length', tracking=True)
    enclosure_design_product_dimensions_width = fields.Text('Product Width', tracking=True)
    enclosure_design_product_dimensions_height = fields.Text('Product Height', tracking=True)
    enclosure_design_product_temperatures = fields.Text(
        'What are the maximum and minimum operating temperatures for the product', tracking=True)
    enclosure_design_specific_environmental = fields.Text(
        'Are there any specific environmental conditions the enclosure needs to withstand', tracking=True)
    enclosure_design_product_mounted = fields.Text('How will the enclosure be mounted or installed', tracking=True)
    enclosure_design_product_placed = fields.Text('Where will the enclosure be placed.', tracking=True)
    enclosure_design_product_connectors = fields.Text(
        'Are there any connectors, buttons, displays, or other interfaces that need to be accessible from the outside of the enclosure.',
        tracking=True)
    enclosure_design_product_interact = fields.Text('How will the user interact with the product.', tracking=True)
    enclosure_design_product_materials = fields.Text(
        'Are there any specific materials or material properties preferred for the enclosure.', tracking=True)
    enclosure_design_product_specific_design = fields.Text(
        'Are there any specific design elements, colors, or branding requirements for the enclosure.', tracking=True)
    enclosure_design_product_significant_heat = fields.Text('Does the product generate significant heat.',
                                                            tracking=True)
    enclosure_design_product_specific_ventilation_requirements = fields.Text(
        'Are there any specific ventilation requirements for the enclosure.', tracking=True)
    enclosure_design_product_safety_standards = fields.Text(
        'Are there any safety standards or certifications that the enclosure needs to comply with', tracking=True)
    enclosure_design_product_existing_enclosure_designs = fields.Text(
        'Do you have any existing enclosure designs or samples that can serve as a reference or starting point',
        tracking=True)
    enclosure_design_product_communicater_name = fields.Char('Name', tracking=True)
    enclosure_design_product_communicater_email = fields.Char('Email', tracking=True)
    enclosure_design_product_communicater_phone = fields.Char('Phone Number', tracking=True)
    enclosure_design_product_file = fields.Binary('Files')
    enclosure_design_product_filename = fields.Char()

    def get_fdm_material(self):
        fdm_service_cost = self.env.ref('cr_web_portal.service_cost_fdm')
        if fdm_service_cost and fdm_service_cost.material_ids:
            materials = []
            for rec in fdm_service_cost.material_ids:
                materials.append((rec.name.strip(),rec.name.strip()))
            return materials
        return [
            ('PLA', 'PLA'),
            ('ABS', 'ABS'),
            ('PETG', 'PETG'),
            ('ASA', 'ASA'),
            ('TPU', 'TPU'),
            ('TPE', 'TPE'),
        ]

    def get_fdm_print_quality(self):
        fdm_service_cost = self.env.ref('cr_web_portal.service_cost_fdm')
        if fdm_service_cost and fdm_service_cost.print_quality_ids:
            print_quality_list = []
            for rec in fdm_service_cost.print_quality_ids:
                print_quality_list.append((str(rec.thickness)+' mm', str(rec.thickness)+' mm'))
            return print_quality_list
        return [
            ('0.05 mm', '0.05 mm'),
            ('0.1 mm', '0.1 mm'),
            ('0.15 mm', '0.15 mm'),
            ('0.2 mm', '0.2 mm'),
        ]

    def get_fdm_infill(self):
        fdm_service_cost = self.env.ref('cr_web_portal.service_cost_fdm')
        if fdm_service_cost and fdm_service_cost.infill_ids:
            infill_list = []
            for rec in fdm_service_cost.infill_ids:
                infill_list.append((str(int(rec.percent))+'%', str(int(rec.percent))+'%'))
            return infill_list
        return [
            ('10%', '10%'),
            ('20%', '20%'),
            ('30%', '30%'),
            ('40%', '40%'),
            ('50%', '50%'),
            ('60%', '60%'),
            ('70%', '70%'),
            ('80%', '80%'),
            ('90%', '90%'),
            ('100%', '100%'),
        ]

    def get_uv_printing_side(self):
        sides = self.env['service.number.of.sides'].sudo().search([])
        sides_list = []
        if sides:
            for side in sides:
                sides_list.append((str(side.no_sides),str(side.no_sides)))
            return sides_list
        return []

    # 3d printing (FDM) service questions
    fdm_color = fields.Selection(COLORS, string="Color", tracking=True)
    fdm_product_name = fields.Char('Product Name', tracking=True)
    fdm_quantity = fields.Float('Quantity', tracking=True)
    fdm_material = fields.Selection(get_fdm_material, string='Choose Material', tracking=True)
    fdm_print_quality = fields.Selection(get_fdm_print_quality, string='Print Quality', tracking=True)
    fdm_infill = fields.Selection(get_fdm_infill, string='InFill', tracking=True)
    fdm_technical_drawings = fields.Binary('Upload Technical Drawing')
    fdm_technical_drawings_filename = fields.Char()
    fdm_is_uv_printing = fields.Boolean('UV Printing', tracking=True)
    fdm_uv_printing_file = fields.Binary('UV Printing File')
    fdm_uv_printing_filename = fields.Char()
    fdm_extra_note = fields.Text('Extra Note', tracking=True)
    uv_printing_side = fields.Selection(get_uv_printing_side,string='UV Printing Side')

    def get_projection_materials(self):
        projection_service_cost = self.env.ref('cr_web_portal.service_cost_projection')
        if projection_service_cost and projection_service_cost.material_ids:
            materials = [('Rigid White', 'Rigid White'), ('Rubber-65A BLK', 'Rubber-65A BLK'),
                             ('High Temp 150°C FR Black', 'High Temp 150°C FR Black'),
                             ('Tough 65C Black', 'Tough 65C Black')]
            for rec in projection_service_cost.material_ids:
                materials.append((rec.name.strip(), rec.name.strip()))
            return materials
        return [
            ('PRO-BLK 10', 'PRO-BLK 10'),
            ('Rigid White', 'Rigid White'),
            ('Tough 60C White', 'Tough 60C White'),
            ('Rigid Gray', 'Rigid Gray'),
            ('Rubber-65A BLK', 'Rubber-65A BLK'),
            ('Flex-BLK 20', 'Flex-BLK 20'),
            ('High Temp 150°C FR Black', 'High Temp 150°C FR Black'),
            ('Tough 65C Black', 'Tough 65C Black'),
        ]

    def get_projection_print_quality(self):
        projection_service_cost = self.env.ref('cr_web_portal.service_cost_projection')
        if projection_service_cost and projection_service_cost.print_quality_ids:
            print_quality_list = []
            for rec in projection_service_cost.print_quality_ids:
                print_quality_list.append((str(int(rec.thickness))+' micron', str(int(rec.thickness))+' micron'))
            return print_quality_list

        return [
            ('20 micron', '20 micron'),
            ('30 micron', '30 micron'),
            ('40 micron', '40 micron'),
            ('50 micron', '50 micron'),
        ]

    # 3d printing (Project Printing) service questions
    projection_product_name = fields.Char('Product Name', tracking=True)
    projection_quantity = fields.Float('Quantity', tracking=True)
    projection_material = fields.Selection(get_projection_materials, string='Choose Material', tracking=True)
    projection_print_quality = fields.Selection(get_projection_print_quality, string='Print Quality', tracking=True)
    projection_technical_drawings = fields.Binary('Upload Technical Drawing')
    projection_technical_drawings_filename = fields.Char()
    projection_is_uv_printing = fields.Boolean('UV Printing', tracking=True)
    projection_uv_printing_file = fields.Binary('UV Printing File')
    projection_uv_printing_filename = fields.Char()
    projection_extra_note = fields.Text('Extra Note', tracking=True)

    # Sheet Metal Fabrication service questions

    metal_feb_product_name = fields.Char('Product Name', tracking=True)
    metal_feb_quantity = fields.Float('Quantity', tracking=True)
    metal_feb_material = fields.Selection([
        ('Aluminum 5052', 'Aluminum 5052'),
        ('Stainless steel 304', 'Stainless steel 304'),
        ('Stainless steel 316', 'Stainless steel 316'),
        ('Stainless steel 316L', 'Stainless steel 316L'),
        ('Stainless steel 3012', 'Stainless steel 3012'),
        ('Mild steel (CR)', 'Mild steel (CR)'),
        ('GI regular sprinkle', 'GI regular sprinkle'),
        ('GI zero sprinkle', 'GI zero sprinkle'),
        ('Other', 'Other'),
    ], string='Choose Material', tracking=True)
    metal_feb_material_other = fields.Text('Specified Material', tracking=True)
    metal_feb_thickness = fields.Selection([
        ('0.8 mm', '0.8 mm'),
        ('1 mm', '1 mm'),
        ('1.2 mm', '1.2 mm'),
        ('1.5 mm', '1.5 mm'),
        ('2 mm', '2 mm'),
        ('2.5 mm', '2.5 mm'),
        ('3 mm', '3 mm'),
        ('4 mm', '4 mm'),
        ('Other', 'Other'),
    ], string='Thickness', tracking=True)
    metal_feb_thickness_other = fields.Text('Specified Thickness', tracking=True)
    metal_feb_is_welding = fields.Boolean('Welding', tracking=True)
    metal_feb_surface_finish = fields.Selection([
        ('Powder coated epoxy (Structure)', 'Powder coated epoxy (Structure)'),
        ('Powder coated epoxy (Texture)', 'Powder coated epoxy (Texture)'),
        ('Powder coated epoxy (Matt)', 'Powder coated epoxy (Matt)'),
        ('Powder coated PP (Matt)', 'Powder coated PP (Matt)'),
        ('Powder coated PP (Structure)', 'Powder coated PP (Structure)'),
        ('Powder coated PP (Texture)', 'Powder coated PP (Texture)'),
        ('Anodized', 'Anodized'),
        ('None', 'None'),
        ('Other', 'Other'),
    ], string='Surface finish', tracking=True)
    metal_feb_surface_finish_other = fields.Text('Specified Surface Finish', tracking=True)
    metal_feb_color = fields.Selection([
        ('Light grey (RAL 7035)', 'Light grey (RAL 7035)'),
        ('Jet black (RAL 9005)', 'Jet black (RAL 9005)'),
        ('None', 'None'),
        ('Other', 'Other'),
    ], string='Colour', tracking=True)
    metal_feb_color_other = fields.Text('Specified Metal Feb Color', tracking=True)
    metal_feb_is_uv_printing = fields.Boolean('UV Printing', tracking=True)
    metal_feb_uv_printing_file = fields.Binary('UV Printing File')
    metal_feb_uv_printing_filename = fields.Char()
    metal_feb_technical_drawings = fields.Binary('Upload Technical Drawing')
    metal_feb_technical_drawings_filename = fields.Char()
    metal_feb_extra_note = fields.Text('Extra Note', tracking=True)

    # injection molding service questions

    injection_mold_product_name = fields.Char('Product Name', tracking=True)
    injection_mold_quantity = fields.Float('Quantity', tracking=True)
    injection_mold_material = fields.Selection([('ABS', 'ABS'),
                                                ('Polycarbonate', 'Polycarbonate'),
                                                ('ABS + Polycarbonate', 'ABS + Polycarbonate'),
                                                ('Nylon', 'Nylon'),
                                                ('Polypropylene', 'Polypropylene'),
                                                ('Polyphenylene Ether', 'Polyphenylene Ether'),
                                                ('Polyoxymethylene', 'Polyoxymethylene'),
                                                ('Other', 'Other'),
                                                ], string="Material", tracking=True)
    injection_mold_material_other = fields.Text('Specified Injection Mold Material', tracking=True)
    injection_mold_colour = fields.Selection([('Black', 'Black'),
                                              ('White', 'White'),
                                              ('Other', 'Other'),
                                              ], string="Colour", tracking=True)
    injection_mold_colour_other = fields.Text('Specified Injection Mold Colour Other', tracking=True)
    injection_mold_surface_finish = fields.Text('Surface Finish', tracking=True)
    injection_mold_mold_requirements = fields.Selection([('Mold by Mech Power', 'Mold by Mech Power'),
                                                         ('Mold by customer', 'Mold by customer'),
                                                         ], string="Mold Requirements", tracking=True)
    injection_mold_no_of_cavity = fields.Text('No. of cavity', tracking=True)
    injection_mold_runner = fields.Selection([('Hot', 'Hot'), ('Cold', 'Cold')], string="Runner", tracking=True)
    injection_mold_size_of_the_mold = fields.Text(string="Size of the mold[LxWxH, in mm]", tracking=True)
    injection_mold_size_of_the_mold_length = fields.Text(string="Size of the mold Length]", tracking=True)
    injection_mold_size_of_the_mold_width = fields.Text(string="Size of the mold Width]", tracking=True)
    injection_mold_size_of_the_mold_height = fields.Text(string="Size of the mold Height]", tracking=True)
    injection_mold_size_of_the_article = fields.Text(string="Size of the article", tracking=True)
    injection_mold_weight_of_the_article = fields.Text(string="Weight of the article", tracking=True)
    injection_mold_upload_technical_drawing = fields.Binary(string="Upload Technical Drawing(s)")
    injection_mold_upload_technical_drawing_filename = fields.Char()
    injection_mold_additional_notes = fields.Text(string="Additional notes", tracking=True)

    injection_is_uv_printing = fields.Boolean('UV Printing', tracking=True)
    injection_uv_printing_file = fields.Binary('UV Printing File')
    injection_uv_printing_filename = fields.Char('UV Printing File')

    # CNC Machining service questions

    cnc_machining_product_name = fields.Char('Product Name', tracking=True)
    cnc_machining_quantity = fields.Float('Quantity', tracking=True)
    cnc_machining_material = fields.Text('Material', tracking=True)
    cnc_machining_upload_technical_drawing = fields.Binary(string="Upload Technical Drawing(s)")
    cnc_machining_upload_technical_drawing_filename = fields.Char()
    cnc_machining_additional_notes = fields.Text(string="Additional notes", tracking=True)

    cnc_is_uv_printing = fields.Boolean('UV Printing', tracking=True)
    cnc_uv_printing_file = fields.Binary('UV Printing File')
    cnc_uv_printing_filename = fields.Char('UV Printing File')
    accessory_product_ids = fields.Many2many('product.product', 'product_accessory_product_rel', 'src_id', 'dest_id')
    # glb_image_ids = fields.Many2many('ir.attachment')

    def get_product_rec(self, product_id):
        product_id = self.browse([int(product_id)])
        data = {}
        data['product_id'] = product_id.id
        if product_id.pdf_file:
            data['pdf_file'] = product_id.pdf_file
            data['pdf_file_name'] = product_id.pdf_file_name
        # if product_id.dxf_file:
        #     data['dxf_file'] = product_id.dxf_file
        #     data['dxf_file_name'] = product_id.dxf_file_name
        # if product_id.outsource_pdf_file:
        #     data['outsource_pdf_file'] = product_id.outsource_pdf_file
        #     data['outsource_pdf_file_name'] = product_id.outsource_pdf_file_name
        return data

    def _website_show_quick_add(self):
        website = self.env['website'].get_current_website()
        return self.sale_ok and (not website.prevent_zero_price_sale or self._get_contextual_price())

    def _get_sales_prices(self,pricelist):
        price_reduce = False
        pricelist_ids = self.env['product.pricelist.item'].search(
            [('product_id', '=', self.id), ('pricelist_id', '=', pricelist.id)])
        if pricelist_ids.mapped('fixed_price'):
            price_reduce = min(pricelist_ids.mapped('fixed_price'))
        return price_reduce

    @api.model
    def create(self, vals):
        res = super().create(vals)
        document = self.env['document.history'].sudo()
        data = {}

        if vals.get('fcstd_file', False):
            data['document'] = vals['fcstd_file']
            data['product_id'] = res.id
            data['file_type'] = 'fcstd_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['fcstd_file_name']
        if vals.get('product_step_file', False):
            data['document'] = vals['product_step_file']
            data['product_id'] = res.id
            data['file_type'] = 'product_step_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['product_step_file_name']

        if vals.get('drawing_fcstd_file', False):
            data['document'] = vals['drawing_fcstd_file']
            data['product_id'] = res.id
            data['file_type'] = 'drawing_fcstd_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['drawing_fcstd_file_name']

        if vals.get('pdf_file', False):
            data['document'] = vals['pdf_file']
            data['product_id'] = res.id
            data['file_type'] = 'pdf_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['pdf_file_name']
        if vals.get('doc_file', False):
            data['document'] = vals['doc_file']
            data['product_id'] = res.id
            data['file_type'] = 'doc_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['doc_file_name']

        if vals.get('stl_file', False):
            data['document'] = vals['stl_file']
            data['product_id'] = res.id
            data['file_type'] = 'stl_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['stl_file_name']

        if vals.get('x_studio_customer_drawing_file', False):
            data['document'] = vals['x_studio_customer_drawing_file']
            data['product_id'] = res.id
            data['file_type'] = 'x_studio_customer_drawing_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = 'Customization Form For Database Product (%s)' % doc_id.id

        if vals.get('x_studio_exception_file', False):
            data['document'] = vals['x_studio_exception_file']
            data['product_id'] = res.id
            data['file_type'] = 'x_studio_exception_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['exception_file_name']

        if vals.get('x_studio_exception_reply_file', False):
            data['document'] = vals['x_studio_exception_reply_file']
            data['product_id'] = res.id
            data['file_type'] = 'x_studio_exception_reply_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['exception_reply_file_name']

        if vals.get('technical_drawing_file', False):
            data['document'] = vals['technical_drawing_file']
            data['product_id'] = res.id
            data['file_type'] = 'technical_drawing_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = self.technical_drawing_file_name

        if vals.get('uv_printing_file', False):
            data['document'] = vals['uv_printing_file']
            data['product_id'] = res.id
            data['file_type'] = 'uv_printing_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = self.uv_printing_file_name

        if vals.get('enclosure_design_product_file', False):
            data['document'] = vals['enclosure_design_product_file']
            data['product_template_id'] = res.id
            data['file_type'] = 'enclosure_design_product_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['enclosure_design_product_filename']

        if vals.get('fdm_technical_drawings', False):
            data['document'] = vals['fdm_technical_drawings']
            data['product_template_id'] = res.id
            data['file_type'] = 'fdm_technical_drawings'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['fdm_technical_drawings_filename']

        if vals.get('fdm_uv_printing_file', False):
            data['document'] = vals['fdm_uv_printing_file']
            data['product_template_id'] = res.id
            data['file_type'] = 'fdm_uv_printing_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['fdm_uv_printing_filename']

        if vals.get('projection_technical_drawings', False):
            data['document'] = vals['projection_technical_drawings']
            data['product_template_id'] = res.id
            data['file_type'] = 'projection_technical_drawings'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['projection_technical_drawings_filename']

        if vals.get('projection_uv_printing_file', False):
            data['document'] = vals['projection_uv_printing_file']
            data['product_template_id'] = res.id
            data['file_type'] = 'projection_uv_printing_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['projection_uv_printing_filename']

        if vals.get('metal_feb_uv_printing_file', False):
            data['document'] = vals['metal_feb_uv_printing_file']
            data['product_template_id'] = res.id
            data['file_type'] = 'metal_feb_uv_printing_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['metal_feb_uv_printing_filename']

        if vals.get('metal_feb_technical_drawings', False):
            data['document'] = vals['metal_feb_technical_drawings']
            data['product_template_id'] = res.id
            data['file_type'] = 'metal_feb_technical_drawings'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['metal_feb_technical_drawings_filename']

        if vals.get('injection_mold_upload_technical_drawing', False):
            data['document'] = vals['injection_mold_upload_technical_drawing']
            data['product_template_id'] = res.id
            data['file_type'] = 'injection_mold_upload_technical_drawing'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['injection_mold_upload_technical_drawing_filename']

        if vals.get('injection_uv_printing_file', False):
            data['document'] = vals['injection_uv_printing_file']
            data['product_template_id'] = res.id
            data['file_type'] = 'injection_uv_printing_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['injection_uv_printing_filename']

        if vals.get('cnc_machining_upload_technical_drawing', False):
            data['document'] = vals['cnc_machining_upload_technical_drawing']
            data['product_template_id'] = res.id
            data['file_type'] = 'cnc_machining_upload_technical_drawing'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['cnc_machining_upload_technical_drawing_filename']

        if vals.get('cnc_uv_printing_file', False):
            data['document'] = vals['cnc_uv_printing_file']
            data['product_template_id'] = res.id
            data['file_type'] = 'cnc_uv_printing_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['cnc_uv_printing_filename']
        return res

    def write(self, vals):
        res = super().write(vals)
        document = self.env['document.history'].sudo()
        data = {}

        if vals.get('fcstd_file', False):
            data['document'] = vals['fcstd_file']
            data['product_id'] = self.id
            data['file_type'] = 'fcstd_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = self.fcstd_file_name
        if vals.get('product_step_file', False):
            data['document'] = vals['product_step_file']
            data['product_id'] = self.id
            data['file_type'] = 'product_step_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = self.product_step_file_name
        if vals.get('drawing_fcstd_file', False):
            data['document'] = vals['drawing_fcstd_file']
            data['product_id'] = self.id
            data['file_type'] = 'drawing_fcstd_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = self.drawing_fcstd_file_name
        if vals.get('pdf_file', False):
            data['document'] = vals['pdf_file']
            data['product_id'] = self.id
            data['file_type'] = 'pdf_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = self.pdf_file_name
        if vals.get('doc_file', False):
            data['document'] = vals['doc_file']
            data['product_id'] = self.id
            data['file_type'] = 'doc_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = self.doc_file_name
        if vals.get('stl_file', False):
            data['document'] = vals['stl_file']
            data['product_id'] = self.id
            data['file_type'] = 'stl_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = self.stl_file_name
        if vals.get('x_studio_customer_drawing_file', False):
            data['document'] = vals['x_studio_customer_drawing_file']
            data['product_id'] = self.id
            data['file_type'] = 'x_studio_customer_drawing_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = 'Customization Form For Database Product (%s)' % doc_id.id
        if vals.get('x_studio_exception_file', False):
            data['document'] = vals['x_studio_exception_file']
            data['product_id'] = self.id
            data['file_type'] = 'x_studio_exception_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = self.exception_file_name
        if vals.get('x_studio_exception_reply_file', False):
            data['document'] = vals['x_studio_exception_reply_file']
            data['product_id'] = self.id
            data['file_type'] = 'x_studio_exception_reply_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = self.exception_reply_file_name
        if vals.get('technical_drawing_file', False) and vals.get('technical_drawing_file_name', False):
            data['document'] = vals['technical_drawing_file']
            data['product_id'] = self.id
            data['file_type'] = 'technical_drawing_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['technical_drawing_file_name']
        if vals.get('uv_printing_file', False) and vals.get('uv_printing_file_name', False):
            data['document'] = vals['uv_printing_file']
            data['product_id'] = self.id
            data['file_type'] = 'uv_printing_file'
            data['user_id'] = self.env.user.id
            doc_id = document.create(data)
            doc_id.name = vals['uv_printing_file_name']
        return res

    def _get_images(self):
        self.ensure_one()
        variant_images = list(self.product_variant_image_ids.filtered(lambda x: x.image_1920))
        template_images = list(self.product_tmpl_id.product_template_image_ids.filtered(lambda x: x.image_1920))
        if not variant_images and template_images:
            return template_images
        if not variant_images and not template_images:
            return [self]

        return variant_images + template_images

    def _get_image_holder(self):
        extra_img = self.product_variant_image_ids.filtered(lambda x: x.image_1920)
        return extra_img[0] if extra_img else self


class ProductTemplateAttributeValue(models.Model):
    _inherit = 'product.template.attribute.value'

    def _without_no_variant_attributes(self):
        return self.filtered(lambda ptav: ptav.attribute_id.create_variant != '')


class ProductPublicCategory(models.Model):
    _inherit = 'product.public.category'

    is_publish = fields.Boolean(string="Publish")
    description = fields.Char(string="Description")
    redirect_url = fields.Char(string="Redirect Url")
