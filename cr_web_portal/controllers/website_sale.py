# -*- coding: utf-8 -*-
import json
import base64
from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.fields import Command
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale, WebsiteSaleForm
from datetime import datetime, timedelta
from odoo.addons.sale.controllers.variant import VariantController
from odoo.exceptions import AccessError, MissingError, ValidationError
from odoo.addons.base.models.ir_qweb_fields import nl2br


class WebsiteSaleShop(WebsiteSale):

    @http.route(['/set_partner_invoice_id'], type='json', auth="public", website=True)
    def filter_state(self, order_id, selected_partner_id, **kw):
        if order_id and selected_partner_id:
            order_id = int(order_id)
            selected_partner_id = int(selected_partner_id)
            sale_order_id = request.env['sale.order'].sudo().search([('id', '=', order_id)])
            sale_order_id.sudo().write({'partner_invoice_id': selected_partner_id});
            return True
        return False

    def _get_mandatory_fields_billing(self, country_id=False):
        """Extend mandatory fields to add new industry main category and sub category fields """
        res = super()._get_mandatory_fields_billing(country_id)
        if request.env.user.partner_id.company_type != 'person':
            res += ["vat"]
        res += ["industry_main_category", "industry_sub_category"]
        return res

    def _get_mandatory_fields_shipping(self, country_id=False):
        """Extend mandatory fields to add new industry main category and sub category fields """
        res = super()._get_mandatory_fields_shipping(country_id)
        if request.env.user.partner_id.company_type != 'person':
            res += ["vat"]
        res += ["industry_main_category", "industry_sub_category"]
        return res


    @http.route(['/shop/extra_info'], type='http', auth="public", website=True, sitemap=False)
    def extra_info(self, **post):
        # Check that this option is activated
        order = request.website.sale_get_order()
        extra_step = request.website.viewref('website_sale.extra_info_option')
        if not extra_step.active or not order.is_customisable:
            return request.redirect("/shop/payment")

        # check that cart is valid
        order = request.website.sale_get_order()
        redirection = self.checkout_redirection(order)
        open_editor = request.params.get('open_editor') == 'true'
        # Do not redirect if it is to edit
        # (the information is transmitted via the "open_editor" parameter in the url)
        if not open_editor and redirection:
            return redirection
        values = {
            'website_sale_order': order,
            'post': post,
            'escape': lambda x: x.replace("'", r"\'"),
            'partner': order.partner_id.id,
            'order': order,
        }
        return request.render("website_sale.extra_info", values)

    @http.route(['/check/order/non-customisable'], type='json', auth='public', methods=['post', 'get'], website=True)
    def check_order_non_customisable(self):
        order_sudo = request.website.sale_get_order()
        if order_sudo and order_sudo.order_line:
            if order_sudo.is_place_inquiry:
                return True
            elif not order_sudo.is_customisable:
                return True
            else:
                return False
        else:
            return False

    @http.route(['/check/cartline'], type='json', auth='public', methods=['post', 'get'], website=True)
    def check_cartline(self,**kwargs):
        order_sudo = request.website.sale_get_order()

        if order_sudo and 'service' in kwargs:
            if not order_sudo.service:
                return False
            service = kwargs['service']
            if order_sudo.service != service:
                return True
        return False

    @http.route(['/check/order/non-customisable/inquiry'], type='json', auth='public', methods=['post', 'get'], website=True)
    def check_order_non_customisable_inquiry(self,is_p_inquiry):
        order_sudo = request.website.sale_get_order()
        if order_sudo and order_sudo.order_line:
            if order_sudo.is_place_inquiry and is_p_inquiry == False:
                return True
            elif is_p_inquiry == True and order_sudo.is_place_inquiry == False:
                return True
            else:
                return False
        else:
            return False

    @http.route(['/check/order/customisable'], type='json', auth='public', methods=['post', 'get'], website=True)
    def check_order_customisable(self):
        order_sudo = request.website.sale_get_order()
        if order_sudo and order_sudo.order_line:
            if order_sudo.is_customisable:
                return True
            else:
                return False
        else:
            return False

    @http.route(['/check/order/customisable/inquiry'], type='json', auth='public', methods=['post', 'get'], website=True)
    def check_order_customisable_inquiry(self):
        order_sudo = request.website.sale_get_order()
        if order_sudo and order_sudo.order_line:
            if order_sudo.is_place_inquiry:
                return True
            else:
                return False
        else:
            return False

    @http.route(['/create/product/variant'], type='json', auth='public', methods=['post', 'get'], website=True)
    def create_product_variant(self):
        # request.session['place_inquiry'] = place_inquiry
        order_sudo = request.website.sale_get_order(force_create=True)
        if order_sudo and not order_sudo.order_line:
            order_sudo.is_customisable = True
        # custom_attribute_id = request.env.ref('cr_web_portal.mech_custom_attribute_1').sudo().id
        # attribute_ids = temp_product.product_tmpl_id.attribute_line_ids.mapped('attribute_id')
        # attribute_value_id = False
        # if custom_attribute_id not in attribute_ids.ids:
        #     attribute_value_id = request.env['product.attribute.value'].sudo().create(
        #         {'name': order_sudo.name, 'attribute_id': custom_attribute_id})
        #     temp_product.product_tmpl_id.attribute_line_ids = [
        #         (0, 0, {'attribute_id': custom_attribute_id, 'value_ids': [(4, attribute_value_id.id)]})]
        # else:
        #     attribute_value_id = request.env['product.attribute.value'].sudo().search([('name', '=', order_sudo.name)],
        #                                                                               limit=1, order='id desc')
        #     if not attribute_value_id:
        #         attribute_value_id = request.env['product.attribute.value'].sudo().create(
        #             {'name': order_sudo.name, 'attribute_id': custom_attribute_id})
        #         custom_attribute_line_id = temp_product.product_tmpl_id.attribute_line_ids.filtered(
        #             lambda x: x.attribute_id.id == custom_attribute_id)
        #         custom_attribute_line_id.value_ids = [(4, attribute_value_id.id)]
        #     else:
        #         custom_attribute_line_id = temp_product.product_tmpl_id.attribute_line_ids.filtered(
        #             lambda x: x.attribute_id.id == custom_attribute_id)
        #         custom_attribute_line_id.value_ids = [(4, attribute_value_id.id)]
        # if attribute_value_id:
        #     product_temp_attr_value_id = request.env['product.template.attribute.value'].search(
        #         [('product_attribute_value_id', '=', attribute_value_id.id),
        #          ('attribute_id', '=', custom_attribute_id)])
        #     if product_temp_attr_value_id:
        #         existing_product_id = request.env['product.product'].sudo().search(
        #             [('product_template_variant_value_ids', 'in', product_temp_attr_value_id.ids)])
        #         if existing_product_id:
        #             return existing_product_id.id
        #         else:
        #             new_product_id = request.env['product.product'].sudo().create({
        #                 'display_name': temp_product.name + order_sudo.name,
        #                 'product_tmpl_id': temp_product.product_tmpl_id.id,
        #                 'sale_ok': True,
        #                 'is_customisable': True,
        #                 'product_template_variant_value_ids': [(6, 0, product_temp_attr_value_id.ids)]
        #             })
        #             new_product_id.is_customisable = True
        #             new_product_id.display_name = temp_product.name + order_sudo.name
        #             return new_product_id.id
        # return False
    @http.route(['/create/product/variant/inquiry'], type='json', auth='public', methods=['post', 'get'], website=True)
    def create_product_variant_place_inquiry(self):
        order_sudo = request.website.sale_get_order(force_create=True)
        if order_sudo and not order_sudo.order_line:
            order_sudo.is_place_inquiry = True
            order_sudo.is_customisable = True


    @http.route(['/make/reorder'], type='http', auth="user", website=True)
    def make_reorder(self, **kw):
        order = request.website.sale_get_order()
        if kw.keys():
            for key, value in kw.items():
                orderline_id = key.split('orderline_qty_')[1]
                if orderline_id:
                    orderline_id = request.env['sale.order.line'].sudo().search([('id','=',int(orderline_id))])
                    if orderline_id and orderline_id.product_id:
                        if order and order.order_line:
                            if not order.is_place_inquiry:
                                order._cart_update(
                                    product_id=int(orderline_id.product_id.id),
                                    add_qty=float(value),
                                )
                        else:
                            request.website.sale_get_order(force_create=1)._cart_update(
                                product_id=int(orderline_id.product_id.id),
                                add_qty=float(1),
                                set_qty=float(value),
                            )
        return request.redirect("/shop/cart")

    @http.route(['/customise_order_confirm/<int:order>'], type='http', auth="user", website=True)
    def customise_order_confirm(self, order, **kw):
        order = request.env['sale.order'].sudo().browse([order])
        custom_attribute_id = request.env.ref('cr_web_portal.mech_custom_attribute').sudo().id
        order.write({'state': 'inquiry'})
        product_id_report = False
        temp =0
        if order.is_customisable and not order.is_place_inquiry:
            for line in order.order_line.filtered(lambda x: not x.is_delivery):
                product_id = line.product_id
                attribute_line_id = product_id.product_template_attribute_value_ids
                categ_id = request.env['product.category'].sudo().search(
                    [('parent_id.name', '=', 'Customer Specific Goods'), ('name', '=', 'Finished')], limit=1)
                uom_id = request.env['uom.uom'].sudo().search([('name', '=', 'NOS')], limit=1)
                new_product_template_id = request.env['product.template'].sudo().create({
                    'name': product_id.name + ' ' + order.name,
                    'sale_ok': True,
                    'purchase_ok': False,
                    'detailed_type': 'product',
                    'is_published': False,
                    'list_price': 0,
                    'categ_id': categ_id.id,
                    'uom_id': uom_id.id,
                    'uom_po_id': uom_id.id,
                    'route_ids': [(6, 0, request.env.ref('mrp.route_warehouse0_manufacture').ids)],
                    'attribute_line_ids': [(0, 0, {
                        'attribute_id': l.attribute_id.id,
                        'value_ids': [(6, 0, l.product_attribute_value_id.ids)]
                    }) for l in attribute_line_id]
                })
                temp+=1
                if len(order.order_line.filtered(lambda x: not x.is_delivery)) > 1:
                    new_attribute_value_id = request.env['product.attribute.value'].sudo().create(
                        {'name': '%s (%s)' % (order.name,temp), 'attribute_id': custom_attribute_id})
                else:
                    new_attribute_value_id = request.env['product.attribute.value'].sudo().create(
                        {'name': order.name, 'attribute_id': custom_attribute_id})
                new_product_template_id.attribute_line_ids = [(0, 0, {
                    'attribute_id': custom_attribute_id,
                    'value_ids': [(4, new_attribute_value_id.id)]
                })]
                new_product_tmpl_attr_value_id = request.env['product.template.attribute.value'].search(
                    [('product_attribute_value_id', '=', new_attribute_value_id.id),
                     ('attribute_id', '=', custom_attribute_id)])
                new_product_template_id.product_variant_ids[0].product_template_attribute_value_ids = [
                    (6, 0, product_id.product_template_attribute_value_ids.ids + new_product_tmpl_attr_value_id.ids)]
                new_product_template_id.product_variant_ids[0].product_template_variant_value_ids = [
                    (6, 0, product_id.product_template_attribute_value_ids.ids + new_product_tmpl_attr_value_id.ids)]
                new_product_template_id.product_variant_ids[0].is_customisable = True
                line.product_template_id = new_product_template_id.id
                line.product_id = new_product_template_id.product_variant_ids[0].id
                new_product_template_id.product_variant_ids[0].default_code = request.env[
                    'ir.sequence'].sudo().next_by_code('product.product')
                new_product_template_id.product_variant_ids[0].source_internal_ref = product_id.default_code

                line.price_unit = 0
                bom_id = product_id.bom_ids.sorted(key=lambda bom: bom.id, reverse=True)
                product_id_report = new_product_template_id.product_variant_ids[0].name
                if bom_id:
                    bom_values = {
                        'product_tmpl_id': new_product_template_id.id,
                        'product_id': new_product_template_id.product_variant_ids[0].id,
                        'product_qty': bom_id[0].product_qty,
                        'type': 'normal',
                        'bom_line_ids': [(0, 0, {
                            'product_id': l.product_id.id,
                            'product_qty': l.product_qty
                        }) for l in bom_id[0].bom_line_ids]
                    }
                    new_bom_id = request.env['mrp.bom'].sudo().create(bom_values)

                attachment = request.env['ir.attachment'].sudo()
                if order.technical_drawing_file:
                    technical_drawing_attachment = attachment.search(
                        [('res_model', '=', 'sale.order'), ('res_field', '=', 'technical_drawing_file'),
                         ('name', '=', order.technical_drawing_file_name)], limit=1)
                    if technical_drawing_attachment:
                        line.product_id.technical_drawing_file = technical_drawing_attachment.datas
                        line.product_id.technical_drawing_file_name = technical_drawing_attachment.name
                if order.uv_printing_file:
                    technical_uv_attachment = attachment.search(
                        [('res_model', '=', 'sale.order'), ('res_field', '=', 'uv_printing_file'),
                         ('name', '=', order.uv_printing_file_name)], limit=1)
                    if technical_uv_attachment:
                        line.product_id.uv_printing_file = technical_uv_attachment.datas
                        line.product_id.uv_printing_file_name = technical_uv_attachment.name
                if order.additional_notes:
                    line.product_id.additional_notes = order.additional_notes

        elif order.is_place_inquiry:
            for line in order.order_line.filtered(lambda x: not x.is_delivery):
                line.product_template_id = line.product_template_id.id
                line.product_id =line.product_template_id.product_variant_ids[0].id
                line.price_unit = 0
                product_id_report = line.product_template_id.product_variant_ids[0].name

        request.session['website_sale_cart_quantity'] = 0

        user = request.env.user
        email_values = {
            'email_to': user.email_formatted,
            'subject': 'We have received your product customisation inquiry %s | Mech Power' % order.name,
        }
        template = request.env.ref('cr_web_portal.inquiry_creation_email', raise_if_not_found=False)
        value = {
            'contact_name': user.name,
            'product_name': product_id_report,
            'addition_note': order.additional_notes,
            'inq_no': order.name
        }
        # 5/0
        if user and template:
            template.with_context(cus_value=value).sudo().send_mail(user.id, force_send=True, email_values=email_values)
        request.session['sale_order_id'] = None
        return request.redirect("/shop/confirmation")

    @http.route(['/create_cart_inquiry'], type='json', auth="public", website=True, csrf=False)
    def create_cart_inquiry_product(self, product_id, qty, **kw):
        if product_id:
            order_sudo = request.website.sale_get_order()
            product_id = request.env['product.product'].sudo().browse([int(product_id)])
            order_sudo.write({
                'order_line': [(0, 0, {
                    'product_id': product_id.id,
                    'name': product_id.name,
                    'product_uom_qty': qty if qty else 1,
                })]
            })
            return True

    @http.route()
    def confirm_order(self, **post):
        order = request.website.sale_get_order()
        redirection = self.checkout_redirection(order) or self.checkout_check_address(order)
        if redirection:
            return redirection
        order.order_line._compute_tax_id()
        self._update_so_external_taxes(order)
        request.session['sale_last_order_id'] = order.id
        request.website.sale_get_order(update_pricelist=True)
        extra_step = request.website.viewref('website_sale.extra_info_option')
        if order and order.is_customisable:
            order.order_line.write({'price_unit': 1})
        if order and not order.is_place_inquiry and extra_step.active:
            return request.redirect("/shop/extra_info")
        return request.redirect("/shop/payment")

class VariantControllerCustom(VariantController):

    @http.route()
    def get_combination_info(self, product_template_id, product_id, combination, add_qty, pricelist_id, **kw):
        res = super().get_combination_info(product_template_id, product_id, combination, add_qty, pricelist_id, **kw)
        if res.get('product_id'):
            temp_product = request.env['product.product'].sudo().browse(int(res.get('product_id')))
        else:
            temp_product = request.env['product.product'].sudo().browse(int(product_id))
        if temp_product:
            res['is_customisable'] = temp_product.is_customisable
            res['sale_delay'] = int(temp_product.sale_delay)
            res['qty_available'] = int(temp_product.qty_available)
            res['is_product_instock_schema'] = 'http://schema.org/InStock' if int(temp_product.qty_available) > 0 else 'http://schema.org/OutOfStock'
        if res and res.get('prevent_zero_price_sale'):
            res['allow_out_of_stock_order'] = True
        if temp_product.product_tmpl_id.attribute_line_ids:
            if 'Metal' in temp_product.product_tmpl_id.attribute_line_ids.mapped('value_ids').mapped('name'):
                res['product_img'] = '/cr_web_portal/static/src/images/mech-custom/tooltip.jpg'
            if 'Plastic' in temp_product.product_tmpl_id.attribute_line_ids.mapped('value_ids').mapped('name'):
                res['product_img'] = '/cr_web_portal/static/src/images/mech-custom/plastic.JPEG'
        return res

    @http.route(['/get_product_quantity'], type='json', auth="public", methods=['POST'], website=True,
                csrf=False)
    def get_product_quantity(self, product_id):
        temp_product = request.env['product.product'].sudo().browse(int(product_id))
        if temp_product:
            return temp_product.qty_available
        else:
            return 0


class WebsiteSaleFormInherit(WebsiteSaleForm):

    @http.route('/website/form/shop.sale.order', type='http', auth="public", methods=['POST'], website=True)
    def website_form_saleorder(self, **kwargs):
        model_record = request.env.ref('sale.model_sale_order')
        order = request.website.sale_get_order()
        data = self.extract_data(model_record, kwargs)
        try:
            data = self.extract_data(model_record, kwargs)
            if data:
                fdm_is_uv_printing = kwargs['fdm_is_uv_printing'] if 'fdm_is_uv_printing' in kwargs else 'No'
                text_additional_notes = kwargs['text_additional_notes'] if 'text_additional_notes' in kwargs else ''
                technical_drawing_document = kwargs['technical_drawing_document[1][0]'] if 'technical_drawing_document[1][0]' in kwargs else False
                uv_printing_document = kwargs['uv_printing_document[2][0]'] if 'uv_printing_document[2][0]' in kwargs else False
                values = {}
                if technical_drawing_document:
                    attachment_value = {
                        'name': technical_drawing_document.filename,
                        'datas': base64.encodebytes(technical_drawing_document.read()),
                        'res_model': model_record.sudo().model,
                        'res_field': 'technical_drawing_file',
                        'res_id': order.id,
                    }
                    attachment_id = request.env['ir.attachment'].sudo().create(attachment_value)
                    values['technical_drawing_file_name'] = technical_drawing_document.filename
                if uv_printing_document:
                    attachment_value = {
                        'name': uv_printing_document.filename,
                        'datas': base64.encodebytes(uv_printing_document.read()),
                        'res_model': model_record.sudo().model,
                        'res_field': 'uv_printing_file',
                        'res_id': order.id,
                    }
                    if fdm_is_uv_printing == 'Yes':
                        attachment_id = request.env['ir.attachment'].sudo().create(attachment_value)
                        values['uv_printing_file_name'] = uv_printing_document.filename

                if fdm_is_uv_printing or text_additional_notes:
                    values.update({'additional_notes': text_additional_notes,
                                 'is_uv_printing': True if fdm_is_uv_printing == 'Yes' else False})
                    order.write(values)


        except ValidationError as e:
            return json.dumps({'error_fields': e.args[0]})

        if data['record']:
            order.write(data['record'])
        return json.dumps({'id': order.id})
