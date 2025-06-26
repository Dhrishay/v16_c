# -*- coding: utf-8 -*-
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

import base64
import json
import math
import re

from werkzeug import urls

from odoo import http, tools, _, SUPERUSER_ID, fields
from odoo.exceptions import AccessDenied, AccessError, MissingError, UserError, ValidationError
from odoo.http import content_disposition, Controller, request, route
from odoo.tools import consteq


class CustomerPortalPasswordPolicy(CustomerPortal):

    MANDATORY_BILLING_FIELDS = ["name", "mobile", "email","phone", "street", "city_id", "country_id","vat","company_name"]
    OPTIONAL_BILLING_FIELDS = ["zipcode", "state_id"]
    def details_form_validate(self, data, partner_creation=False):
        error = dict()
        error_message = []
        # Validation
        for field_name in self.MANDATORY_BILLING_FIELDS:
            if not data.get(field_name):
                if field_name == 'vat' or field_name == 'company_name':
                    if request.env.user.partner_id.company_type != 'person':
                        error[field_name] = 'missing'
                else:
                    error[field_name] = 'missing'

        # email validation
        if data.get('email') and not tools.single_email_re.match(data.get('email')):
            error["email"] = 'error'
            error_message.append(_('Invalid Email! Please enter a valid email address.'))

        # vat validation
        partner = request.env.user.partner_id
        if data.get("vat") and partner and partner.vat != data.get("vat"):
            # Check the VAT if it is the public user too.
            if partner_creation:
                if hasattr(partner, "check_vat"):
                    if data.get("country_id"):
                        data["vat"] = request.env["res.partner"].fix_eu_vat_number(int(data.get("country_id")),
                                                                                   data.get("vat"))
                    partner_dummy = partner.new({
                        'vat': data['vat'],
                        'country_id': (int(data['country_id'])
                                       if data.get('country_id') else False),
                    })
                    try:
                        partner_dummy.check_vat()
                    except ValidationError as e:
                        error["vat"] = 'error'
                        error_message.append(e.args[0])
            else:
                error_message.append(
                    _('Changing VAT number is not allowed once document(s) have been issued for your account. Please contact us directly for this operation.'))

        # error message for empty required fields
        if [err for err in error.values() if err == 'missing']:
            error_message.append(_('Some required fields are empty.'))
        unknown = [k for k in data if k not in self.MANDATORY_BILLING_FIELDS + self.OPTIONAL_BILLING_FIELDS]
        if unknown:
            error['common'] = 'Unknown field'
            error_message.append("Unknown field '%s'" % ','.join(unknown))
        return error, error_message


    @http.route()
    def account(self, redirect=None, **post):
        # Condition for redirecting my account to billing / shipping address for showing user errors
        if 'error_data' in dict(request.session).keys():
            error_data = dict(request.session['error_data']) if request.session.get('error_data') else {}
            del request.session['error_data']
            if 'is_shipping_address' in error_data.keys():
                del error_data['is_shipping_address']
                partner = request.env['res.partner'].sudo().browse(error_data['partner'])
                partner_country_id = request.env['res.country'].sudo().browse(error_data['partner_country_id'])
                partner_mobile_country_id = request.env['res.country'].sudo().browse(error_data['partner_mobile_country_id'])
                return request.render('cr_web_portal.portal_my_shipping_edit', {
                    'partner': partner,
                    'option': error_data['option'],
                    'error_message': error_data['error_message'],
                    'value': error_data['value'],
                    'partner_country_id': partner_country_id ,
                    'partner_mobile_country_id': partner_mobile_country_id,
                })

            if 'is_billing_address' in error_data.keys():
                del error_data['is_billing_address']
                partner = request.env['res.partner'].sudo().browse(error_data['partner'])
                partner_country_id = request.env['res.country'].sudo().browse(error_data['partner_country_id'])
                partner_mobile_country_id = request.env['res.country'].sudo().browse(error_data['partner_mobile_country_id'])
                return request.render('cr_web_portal.portal_my_billing_edit', {
                    'partner': partner,
                    'option': error_data['option'],
                    'error_message': error_data['error_message'],
                    'value': error_data['value'],
                    'partner_country_id': partner_country_id ,
                    'partner_mobile_country_id': partner_mobile_country_id,
                })

        industry_id = request.env.user.partner_id.industry_main_category.id if request.env.user.partner_id.industry_main_category else 0
        sub_category_id = request.env.user.partner_id.industry_sub_category.id if request.env.user.partner_id.industry_sub_category else 0

        if 'image_1920' in post:
            image_1920 = post.get('image_1920')
            if image_1920:
                image_1920 = image_1920.read()
                image_1920 = base64.b64encode(image_1920)
                request.env.user.partner_id.sudo().write({
                    'image_1920': image_1920
                })
            post.pop('image_1920')
        if 'clear_avatar' in post:
            request.env.user.partner_id.sudo().write({
                'image_1920': False
            })
            post.pop('clear_avatar')

        check = all(e in list(post.keys()) for e in ['industry_id','sub_category_id','registration_type','mobile','phone','selected_phone_country_id','selected_mobile_country_id'])
        if check:
            industry_id = post['industry_id']
            sub_category_id = post['sub_category_id']
            registration_type = post['registration_type']
            mobile = post['mobile']
            phone = post['phone']
            selected_phone_country_id = post['selected_phone_country_id']
            selected_mobile_country_id = post['selected_mobile_country_id']

            if selected_phone_country_id:
                partner_country_id = request.env['res.country'].sudo().browse(int(selected_phone_country_id))
                new_phone = '+' + str(partner_country_id.phone_code) + ' ' + phone
                post.update({'phone': new_phone})

            if selected_mobile_country_id:
                partner_country_id = request.env['res.country'].sudo().browse(int(selected_mobile_country_id))
                new_mobile = '+' + str(partner_country_id.phone_code) + ' ' + mobile
                mobile = new_mobile
                post.update({'mobile': new_mobile})


            del post['industry_id']
            del post['sub_category_id']
            del post['registration_type']
            del post['selected_phone_country_id']
            del post['selected_mobile_country_id']

            partner_id = request.env.user.partner_id.sudo().write({
                'industry_main_category': int(industry_id) if industry_id else False,
                'industry_sub_category': int(sub_category_id) if sub_category_id else False,
                'company_type': registration_type,
                'mobile' : mobile
            })

        industry_segments = request.env['industry.segment'].sudo().search([])

        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        values.update({
            'error': {},
            'error_message': [],
        })
        # opt_check = False
        # if post.get('opt_check') and post.get('opt_check') == 'on':
        #     opt_check = True
        #     del post['opt_check']


        if post and request.httprequest.method == 'POST':
            if post.get('mailing_contact_id'):
                mailing_contact_id = request.env["mailing.contact"].sudo().search(
                    [('id', '=', int(post.get('mailing_contact_id')))]
                )
                if mailing_contact_id:
                    mail_list = []
                    keys_to_delete = ['mailing_contact_id']

                    # Collect keys to delete
                    for key in list(post.keys()):  # Use list() to avoid runtime errors
                        if key.startswith('opt_check_'):
                            record_id = int(key.replace('opt_check_', ''))
                            mail_list.append(record_id)
                            keys_to_delete.append(key)

                    # Remove collected keys after iteration
                    for key in keys_to_delete:
                        post.pop(key, None)  # Use .pop() to avoid KeyErrors

                    subscribe_list = mailing_contact_id.subscription_list_ids.filtered(lambda x: x.id in mail_list)
                    unsubscribe_list = mailing_contact_id.subscription_list_ids - subscribe_list

                    unsubscribe_list.write({'opt_out': True})
                    subscribe_list.write({'opt_out': False})
            error, error_message = self.details_form_validate(post)
            values.update({'error': error, 'error_message': error_message})
            values.update(post)
            if not error:
                values = {key: post[key] for key in self.MANDATORY_BILLING_FIELDS}
                values.update({key: post[key] for key in self.OPTIONAL_BILLING_FIELDS if key in post})
                for field in set(['country_id', 'state_id']) & set(values.keys()):
                    try:
                        values[field] = int(values[field])
                    except:
                        values[field] = False
                values.update({'zip': values.pop('zipcode', '')})
                if post.get('city_id'):
                    values.update({'city_id': int(post.get('city_id'))})
                # values.update({'opt_out': opt_check})
                self.on_account_update(values, partner)
                partner.sudo().write(values)
                if redirect:
                    return request.redirect(redirect)
                return request.redirect('/my/home')

        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])
        mailing_contact_id = request.env["mailing.contact"].sudo().search([('email', '=', partner.email)], limit=1)
        all_mailing_list = request.env['mailing.list'].sudo().search([('is_publish', '=', True)])
        if mailing_contact_id:
            selected_maling_list = mailing_contact_id.subscription_list_ids.mapped('list_id').ids
            for ml in all_mailing_list:
                if ml.id not in selected_maling_list:
                    mailing_contact_id.subscription_list_ids = [(0,0, {
                        'list_id': ml.id
                    })]
        else:
            contact_vals = {
                "name": partner.name,
                "email": partner.email,
                "list_ids": [(6, 0, all_mailing_list.ids)],
                "company_name": partner.company_id.name or False,
                "country_id": partner.country_id.id or False,
            }
            mailing_contact_id = request.env["mailing.contact"].sudo().create(contact_vals)
        values.update({
            'partner': partner,
            'mailing_list': mailing_contact_id.subscription_list_ids.filtered(lambda x: x.list_id and x.list_id.is_publish) if mailing_contact_id.subscription_list_ids else [],
            'mailing_contact_id': mailing_contact_id.id if mailing_contact_id else False,
            'countries': countries,
            'states': states,
            'has_check_vat': hasattr(request.env['res.partner'], 'check_vat'),
            'partner_can_edit_vat': partner.can_edit_vat(),
            'redirect': redirect,
            'page_name': 'my_details',
            'industry_segments': industry_segments,
            'industry_id': industry_id,
            'sub_category_id': sub_category_id,
        })

        response = request.render("portal.portal_my_details", values)
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Content-Security-Policy'] = "frame-ancestors 'self'"
        return response

    @http.route(['/upload/gst/certificate'], type='http', auth="user", website=True, sitemap=False, csrf=False)
    def upload_gst_file(self, **kw):
        if kw.get('partner_id'):
            partner = request.env['res.partner'].sudo().browse(int(kw['partner_id']))
            partner.write({
                'gst_certificate_filename': kw.get('gst_file').filename,
                'gst_certificate_file': base64.b64encode(kw.get('gst_file').read()),
                'gst_last_update_date': fields.Datetime.now()
            })
        return request.redirect('/my/account')

    @http.route(['/update/mailing-list'], type='http', auth="user", website=True, sitemap=False, csrf=False)
    def update_mailing_list(self, **kw):
        mail_list = []
        if kw.get('mailing_contact_id'):
            mailing_contact_id = request.env["mailing.contact"].sudo().search([('id', '=', int(kw.get('mailing_contact_id')))])
            if mailing_contact_id:
                for key, value in kw.items():
                    if key.startswith('opt_check_'):
                        record_id = int(key.replace('opt_check_', ''))
                        mail_list.append(record_id)

            subscribe_list = mailing_contact_id.subscription_list_ids.filtered(lambda x: x.id in mail_list)
            unsubscribe_list = mailing_contact_id.subscription_list_ids - subscribe_list

            unsubscribe_list.write({'opt_out': True})
            subscribe_list.write({'opt_out': False})
        return request.redirect('/my/account#mailing_lists')