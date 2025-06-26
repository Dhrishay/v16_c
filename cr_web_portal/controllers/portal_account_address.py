# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import tools, _
import json
import base64
from odoo import http
from odoo.http import request
import functools
from odoo.modules import get_resource_path
import odoo
from odoo.http import request, Response
import io
from odoo.tools.mimetypes import guess_mimetype
import base64
from odoo.tools.image import image_data_uri
import json
from odoo.exceptions import UserError, ValidationError, AccessError

from markupsafe import escape
from psycopg2 import IntegrityError
from werkzeug.exceptions import BadRequest
class PortalAccountAddress(http.Controller):

    @http.route(['/my/shipping_address/edit', '/my/shipping_address/edit/<int:partner_id>'], type='http', auth="user", website=True)
    def partner_shipping_address_edit(self, partner_id=False, **kwargs):
        partner = request.env['res.partner'].browse(partner_id)
        if partner:
            return request.render("cr_web_portal.portal_my_shipping_edit", {
                'partner': partner,
                'option': 'edit'
            })
        else:
            return request.render("cr_web_portal.portal_my_shipping_edit", {
                'partner': request.env.user.partner_id,
                'option': 'create'
            })

    # @http.route(['/shipping_address/thankyou'], type='http', auth="user", website=True)
    # def edit_your_shipping_address(self, **post):
    #     partner_id = int(post['id'])
    #     partner = request.env['res.partner'].sudo().search([('id','=',int(partner_id))])
    #     shipping_address = request.env['res.partner'].sudo().search([('id', '=', partner_id), ('type', '=', 'delivery')], limit=1)
    #
    #     partner_country_id = 0
    #     if post['selected_phone_country_id'] and post['phone']:
    #         partner_country_id = request.env['res.country'].sudo().browse(int(post['selected_phone_country_id']))
    #         del post['selected_phone_country_id']
    #         new_phone = '+' + str(partner_country_id.phone_code) + ' ' + post['phone']
    #         post.update({'phone': new_phone})
    #     partner_mobile_country_id = 0
    #     if post['selected_mobile_country_id'] and post['mobile']:
    #         partner_mobile_country_id = request.env['res.country'].sudo().browse(int(post['selected_mobile_country_id']))
    #         del post['selected_mobile_country_id']
    #         new_phone = '+' + str(partner_mobile_country_id.phone_code) + ' ' + post['mobile']
    #         post.update({'mobile': new_phone})
    #
    #
    #     update_data = {
    #         'name': post['name'],
    #         'city': post['city'],
    #         'street': post['street'],
    #         'street2': post['street2'],
    #         'phone': post['phone'],
    #         'zip': post['zip'],
    #         'mobile': post['mobile'],
    #         'email': post['email'],
    #         'company_name': post['company_name'],
    #         'vat': post['vat'],
    #         'state_id': int(post['state_id']),
    #         'country_id': int(post['country_id']),
    #     }
    #
    #     country = request.env['res.country'].sudo().browse(int(post['country_id']))
    #     if shipping_address:
    #         if shipping_address._run_vat_test(post['vat'], country, shipping_address.is_company) is False:
    #             partner_label = _("partner [%s]", shipping_address.name)
    #             msg = shipping_address.sudo()._build_vat_error_message(country and country.code.lower() or None, post['vat'],partner_label)
    #             return request.render('cr_web_portal.portal_my_shipping_edit', {
    #                 'partner': partner,
    #                 'option': 'edit',
    #                 'error_message': msg,
    #                 'value': update_data,
    #                 'partner_country_id': partner_country_id,
    #                 'partner_mobile_country_id': partner_mobile_country_id,
    #             })
    #         else:
    #             shipping_address.update(update_data)
    #     else:
    #         try:
    #             if shipping_address._run_vat_test(post['vat'], country, shipping_address.is_company) is False:
    #                 partner_label = _("partner [%s]", shipping_address.name)
    #                 msg = shipping_address.sudo()._build_vat_error_message(country and country.code.lower() or None,
    #                                                                       post['vat'], partner_label)
    #                 return request.render('cr_web_portal.portal_my_shipping_edit', {
    #                     'partner': partner,
    #                     'option': 'edit',
    #                     'error_message': msg,
    #                     'value': update_data,
    #                     'partner_country_id': partner_country_id,
    #                     'partner_mobile_country_id': partner_mobile_country_id,
    #                 })
    #             else:
    #                 parent_partner = request.env['res.partner'].sudo().browse(partner_id)
    #                 if parent_partner:
    #                     parent_partner.child_ids.create({
    #                         'type': 'delivery',
    #                         'parent_id': parent_partner.id,
    #                         **update_data
    #                     })
    #         except Exception as error:
    #             return request.render('cr_web_portal.portal_my_shipping_edit', {
    #                 'partner': partner,
    #                 'option': 'edit',
    #                 'error_message': error,
    #                 'value': update_data,
    #                 'partner_country_id':partner_country_id,
    #                 'partner_mobile_country_id':partner_mobile_country_id,
    #             })
    #     return request.redirect("/my/account")

    @http.route(['/shipping_address/delete/<int:sh_id>'], type='http', auth="user", website=True)
    def partner_shipping_address_delete(self, sh_id=False, **kwargs):
        partner = request.env['res.partner'].sudo().browse(sh_id)
        try:
            with http.request.env.cr.savepoint():
                if partner.unlink():
                    return request.redirect('/my/account')
        except:
            return request.redirect('/error_page/shipping')

    @http.route(['/error_page/shipping'], type='http', auth="user", website=True)
    def error_shipping_address(self, **post):
        return request.render("cr_web_portal.error_page", {'address': 'shipping'})

    # @http.route(['/billing_address/thankyou'], type='http', auth="public", website=True)
    # def edit_your_billing_address(self, **post):
    #     partner_id = int(post['id'])
    #     partner = request.env['res.partner'].sudo().search([('id', '=', int(partner_id))])
    #     billing_address = request.env['res.partner'].sudo().search([('id', '=', partner_id), ('type', '=', 'invoice')],limit=1)
    #
    #     partner_country_id = 0
    #     if post['selected_phone_country_id'] and post['phone']:
    #         partner_country_id = request.env['res.country'].sudo().browse(int(post['selected_phone_country_id']))
    #         del post['selected_phone_country_id']
    #         new_phone = '+' + str(partner_country_id.phone_code) + ' ' + post['phone']
    #         post.update({'phone': new_phone})
    #     partner_mobile_country_id = 0
    #     if post['selected_mobile_country_id'] and post['mobile']:
    #         partner_mobile_country_id = request.env['res.country'].sudo().browse(
    #             int(post['selected_mobile_country_id']))
    #         del post['selected_mobile_country_id']
    #         new_phone = '+' + str(partner_mobile_country_id.phone_code) + ' ' + post['mobile']
    #         post.update({'mobile': new_phone})
    #
    #     update_data = {
    #         'name': post['name'],
    #         'city': post['city'],
    #         'street': post['street'],
    #         'street2': post['street2'],
    #         'phone': post['phone'],
    #         'mobile': post['mobile'],
    #         'zip': post['zip'],
    #         'email': post['email'],
    #         'company_name': post['company_name'],
    #         'vat': post['vat'],
    #         'state_id': int(post['state_id']),
    #         'country_id': int(post['country_id']),
    #     }
    #     country = request.env['res.country'].sudo().browse(int(post['country_id']))
    #     if billing_address:
    #         if billing_address._run_vat_test(post['vat'], country, billing_address.is_company) is False:
    #             partner_label = _("partner [%s]", billing_address.name)
    #             msg = billing_address.sudo()._build_vat_error_message(country and country.code.lower() or None, post['vat'],partner_label)
    #             return request.render('cr_web_portal.portal_my_billing_edit', {
    #                 'partner': partner,
    #                 'option': 'edit',
    #                 'error_message': msg,
    #                 'value': update_data,
    #                 'partner_country_id': partner_country_id,
    #                 'partner_mobile_country_id': partner_mobile_country_id,
    #             })
    #         else:
    #             billing_address.update(update_data)
    #     else:
    #         try:
    #             if billing_address._run_vat_test(post['vat'], country, billing_address.is_company) is False:
    #                 partner_label = _("partner [%s]", billing_address.name)
    #                 msg = billing_address.sudo()._build_vat_error_message(country and country.code.lower() or None,
    #                                                                       post['vat'], partner_label)
    #                 return request.render('cr_web_portal.portal_my_billing_edit', {
    #                     'partner': partner,
    #                     'option': 'edit',
    #                     'error_message': msg,
    #                     'value': update_data,
    #                     'partner_country_id': partner_country_id,
    #                     'partner_mobile_country_id': partner_mobile_country_id,
    #                 })
    #             else:
    #                 parent_partner = request.env['res.partner'].sudo().browse(partner_id)
    #                 if parent_partner:
    #                     parent_partner.child_ids.create({
    #                         'type': 'invoice',
    #                         'parent_id': parent_partner.id,
    #                         **update_data
    #                     })
    #         except Exception as error:
    #             return request.render('cr_web_portal.portal_my_billing_edit', {
    #                 'partner': partner,
    #                 'option': 'edit',
    #                 'error_message': error,
    #                 'value': update_data,
    #                 'partner_country_id': partner_country_id,
    #                 'partner_mobile_country_id': partner_mobile_country_id,
    #             })
    #
    #     return request.redirect('/my/account')

    @http.route(['/my/billing_address/edit', '/my/billing_address/edit/<int:bl_id>'], type='http', auth="public",
                website=True)
    def partner_billing_address_edit(self, bl_id=False, **kwargs):
        partner = request.env['res.partner'].browse(bl_id)
        if partner:
            return request.render("cr_web_portal.portal_my_billing_edit", {
                'partner': partner,
                'option': 'edit'
            })
        else:
            return request.render("cr_web_portal.portal_my_billing_edit", {
                'partner': request.env.user.partner_id,
                'option': 'create'
            })

    @http.route(['/billing_address/delete/<int:bl_id>'], type='http', auth="public", website=True)
    def partner_billing_address_delete(self, bl_id=False, **kwargs):
        partner = request.env['res.partner'].browse(bl_id)
        try:
            with request.env.cr.savepoint():
                partner.unlink()
                return request.redirect('/my/account')
        except:
            return request.redirect('/error_page/billing')

    @http.route(['/error_page/billing'], type='http', auth="public", website=True)
    def error_billing_address(self, **post):
        return request.render("cr_web_portal.error_page", {'address': 'billing'})