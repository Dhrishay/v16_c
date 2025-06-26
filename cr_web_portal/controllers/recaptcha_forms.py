# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
_logger = logging.getLogger(__name__)
try:
    from werkzeug.utils import send_file
except ImportError:
    from odoo.tools._vendor.send_file import send_file
import base64
from odoo.exceptions import UserError, ValidationError, AccessError

from werkzeug.exceptions import BadRequest
from odoo.addons.website.controllers.form import WebsiteForm
from odoo.addons.website_sale.controllers.main import WebsiteSale


import json
from werkzeug.exceptions import Forbidden, NotFound
from odoo.http import request
from odoo import fields, http, SUPERUSER_ID, tools, _




class MechPowerContactUs(WebsiteForm):

    def _get_vat_validation_fields(self, data):
        return {
            'vat': data['vat'],
            'country_id': int(data['country_id']) if data.get('country_id') else False,
        }
    def checkout_form_validate(self, mode, all_form_values, data):
        # mode: tuple ('new|edit', 'billing|shipping')
        # all_form_values: all values before preprocess
        # data: values after preprocess
        error = dict()
        error_message = []
        if data.get('partner_id'):
            partner_su = request.env['res.partner'].sudo().browse(int(data['partner_id'])).exists()
            name_change = partner_su and 'name' in data and data['name'] != partner_su.name
            email_change = partner_su and 'email' in data and data['email'] != partner_su.email

            # Prevent changing the billing partner name if invoices have been issued.
            if mode[1] == 'billing' and name_change and not partner_su.can_edit_vat():
                error['name'] = 'error'
                error_message.append(_(
                    "Changing your name is not allowed once documents have been issued for your"
                    " account. Please contact us directly for this operation."
                ))

            # Prevent change the partner name or email if it is an internal user.
            if (name_change or email_change) and not all(partner_su.user_ids.mapped('share')):
                error.update({
                    'name': 'error' if name_change else None,
                    'email': 'error' if email_change else None,
                })
                error_message.append(_(
                    "If you are ordering for an external person, please place your order via the"
                    " backend. If you wish to change your name or email address, please do so in"
                    " the account settings or contact your administrator."
                ))
        # Required fields from form
        required_fields = [f for f in (all_form_values.get('field_required') or '').split(',') if f]

        # Required fields from mandatory field function
        country_id = int(data.get('country_id', False))
        required_fields += mode[1] == 'shipping' and WebsiteSale._get_mandatory_fields_shipping(country_id) or WebsiteSale._get_mandatory_fields_billing(country_id)
        if not data.get('industry_main_category') and mode[1] in ('shipping', 'billing'):
            required_fields.append('industry_id')
        if not data.get('industry_sub_category') and mode[1] in ('shipping', 'billing'):
            required_fields.append('sub_industry_id')
        if not data.get('state_id') and mode[1] in ('shipping', 'billing'):
            required_fields.append('state_id')
        if mode[1] == 'shipping':
            required_fields.append('zip')
        required_fields.remove('city')
        required_fields.append('city_id')
        # error message for empty required fields
        for field_name in required_fields:
            val = data.get(field_name)
            if isinstance(val, str):
                val = val.strip()
            if not val:
                error[field_name] = 'missing'

        # email validation
        if data.get('email') and not tools.single_email_re.match(data.get('email')):
            error["email"] = 'error'
            error_message.append(_('Invalid Email! Please enter a valid email address.'))

        # vat validation
        Partner = request.env['res.partner']
        if data.get("vat") and hasattr(Partner, "check_vat"):
            if country_id:
                data["vat"] = Partner.fix_eu_vat_number(country_id, data.get("vat"))
            partner_dummy = Partner.new(self._get_vat_validation_fields(data))
            try:
                partner_dummy.check_vat()
            except ValidationError as exception:
                error["vat"] = 'error'
                error_message.append(exception.args[0])
        if [err for err in error.values() if err == 'missing']:
            error_message.append(_('Some required fields are empty.'))

        return error, error_message

    def extended_check_vals(self,kwargs):
        kwargs['name'] = '' if 'name' not in kwargs.keys() else kwargs['name']
        kwargs['email'] = '' if 'email' not in kwargs.keys() else kwargs['email']
        kwargs['phone'] = '' if 'phone' not in kwargs.keys() else kwargs['phone']
        kwargs['vat'] = '' if 'vat' not in kwargs.keys() else kwargs['vat']
        kwargs['company_name'] = '' if 'company_name' not in kwargs.keys() else kwargs['company_name']
        kwargs['industry_id'] = '' if 'industry_id' not in kwargs.keys() else kwargs['industry_id']
        kwargs['sub_category_id'] = '' if 'sub_category_id' not in kwargs.keys() else kwargs['sub_category_id']
        kwargs['street'] = '' if 'street' not in kwargs.keys() else kwargs['street']
        kwargs['street2'] = '' if 'street2' not in kwargs.keys() else kwargs['street2']
        kwargs['city_id'] = '' if 'city_id' not in kwargs.keys() else kwargs['city_id']
        kwargs['zip'] = '' if 'zip' not in kwargs.keys() else kwargs['zip']
        kwargs['state_id'] = '' if 'state_id' not in kwargs.keys() else kwargs['state_id']
        kwargs['country_id'] = '' if 'country_id' not in kwargs.keys() else kwargs['country_id']

        return kwargs

    @http.route()
    def website_form(self, model_name, **kwargs):
        csrf_token = request.params.pop('csrf_token', None)

        if kwargs.get('form_name') in ['shipping_address_thankyou','billing_address_thankyou','website_sale_address_form']:
            model_name = 'res.partner'

        if kwargs.get('form_name') == 'contactus':
            model_name = 'crm.lead'

        if kwargs.get('form_name') == 'service_request':
            model_name = 'crm.lead'

        if kwargs.get('form_name') == 'sign_up_form':
            model_name = 'res.partner'

        if kwargs.get('form_name') in ['create_fdm_product','create_projection_product','create_enclosure_design','create_metal_fab_product','create_cnc_product','create_injection_molding_product']:
            model_name = 'sale.order'

        if request.session.uid and not request.validate_csrf(csrf_token):
            raise BadRequest('Session expired (invalid CSRF token)')

        try:
            with ((request.env.cr.savepoint())):
                if 1==1:
                # if request.env['ir.http']._verify_request_recaptcha_token('website_form'):
                    kwargs = dict(request.params)
                    kwargs.pop('model_name')
                    if kwargs.get('form_name') == 'website_sale_address_form':
                        kwargs.pop('form_name')
                        Partner = request.env['res.partner'].with_context(show_address=1).sudo()
                        order = request.website.sale_get_order()

                        industry_id = kwargs.get('industry_id', False)
                        sub_category_id = kwargs.get('sub_category_id', False)
                        city_id = kwargs.get('city_id', False)
                        selected_phone_country_id = kwargs.get('selected_phone_country_id', False)
                        phone = kwargs.get('phone', False)
                        new_billing_partner_id = 'new_billing_partner_id' in kwargs.keys()

                        if new_billing_partner_id:
                            del kwargs['new_billing_partner_id']
                        if selected_phone_country_id and phone:
                            partner_country_id = request.env['res.country'].sudo().browse(
                                int(selected_phone_country_id))
                            new_phone = '+' + str(partner_country_id.phone_code) + ' ' + kwargs.get('phone', '')
                            kwargs.update({'phone': new_phone})
                            del kwargs['selected_phone_country_id']

                        if industry_id and sub_category_id:
                            kwargs['industry_main_category'] = int(industry_id)
                            kwargs['industry_sub_category'] = int(sub_category_id)
                        if city_id:
                            kwargs['city_id'] = int(city_id)

                        redirection = ''
                        if not order or order.state != 'draft':
                            request.session['sale_order_id'] = None
                            request.session['sale_transaction_id'] = None
                            redirection = '/shop'

                        if order and not order.order_line:
                            redirection = '/shop/cart'

                        if request.website.is_public_user() and request.website.account_on_checkout == 'mandatory':
                            redirection = '/web/login?redirect=/shop/checkout'

                        tx = request.env.context.get('website_sale_transaction')
                        if tx and tx.state != 'draft':
                            redirection = '/shop/payment/confirmation/%s' % order.id
                        if redirection:
                            request.session['checkout_redirection'] = redirection
                            return json.dumps({'id': int(kwargs.get('partner_id', -1))})

                        mode = (False, False)
                        can_edit_vat = False
                        values, errors = {}, {}
                        partner_id = int(kwargs.get('partner_id', -1))

                        current_partner_id = request.env['res.partner'].sudo().search([('id', '=', partner_id)])

                        # IF PUBLIC ORDER
                        if order.partner_id.id == request.website.user_id.sudo().partner_id.id:
                            mode = ('new', 'billing')
                            can_edit_vat = True
                        # IF ORDER LINKED TO A PARTNER
                        else:
                            if partner_id > 0:
                                if current_partner_id.type == 'invoice' and partner_id in order.partner_id.child_ids.ids:
                                    mode = ('edit', 'billing')
                                    can_edit_vat = order.partner_id.can_edit_vat()
                                elif partner_id == order.partner_id.id:
                                    mode = ('edit', 'billing')
                                    can_edit_vat = order.partner_id.can_edit_vat()
                                else:
                                    shippings = Partner.search(
                                        [('id', 'child_of', order.partner_id.commercial_partner_id.ids)])
                                    if new_billing_partner_id:
                                        mode = ('new', 'billing')
                                        can_edit_vat = True
                                    elif order.partner_id.commercial_partner_id.id == partner_id:
                                        mode = ('new', 'shipping')
                                        partner_id = -1
                                    elif partner_id in shippings.mapped('id'):
                                        mode = ('edit', 'shipping')
                                    else:
                                        request.session['forbidden_error'] = True
                                        return json.dumps({'id': 1})
                                if mode and partner_id != -1:
                                    values = Partner.browse(partner_id)
                            elif partner_id == -1:
                                if new_billing_partner_id:
                                    mode = ('new', 'billing')
                                    can_edit_vat = True
                                    kwargs['parent_id'] = request.env.user.partner_id.id
                                    kwargs['type'] = 'invoice'
                                else:
                                    mode = ('new', 'shipping')
                            else:
                                request.session['checkout_redirection'] = True
                                return json.dumps({'id': 1})

                        # IF POSTED
                        if 'submitted' in kwargs and request.httprequest.method == "POST":
                            kwargs = self.extended_check_vals(kwargs)
                            pre_values = WebsiteSale.values_preprocess(WebsiteSale, kwargs)
                            errors, error_msg = self.checkout_form_validate(mode, kwargs, pre_values)
                            post, errors, error_msg = WebsiteSale.values_postprocess(WebsiteSale,order, mode, pre_values, errors, error_msg)

                            if errors:
                                errors['error_message'] = error_msg
                                values = kwargs
                            else:
                                if industry_id and sub_category_id:
                                    post['industry_main_category'] = int(industry_id)
                                    post['industry_sub_category'] = int(sub_category_id)
                                if city_id:
                                    post['city_id'] = int(city_id)
                                if new_billing_partner_id and mode[1] == 'billing':
                                    post['parent_id'] = request.env.user.partner_id.id
                                    post['type'] = 'invoice'

                                partner_id = WebsiteSale._checkout_form_save(WebsiteSale,mode, post, kwargs)
                                # We need to validate _checkout_form_save return, because when partner_id not in shippings
                                # it returns Forbidden() instead the partner_id
                                if isinstance(partner_id, Forbidden):
                                    request.session['return_partner_id'] = partner_id
                                    return json.dumps({'id': partner_id})
                                fpos_before = order.fiscal_position_id
                                if mode[1] == 'billing':
                                    if not order.partner_id:
                                        order.partner_id = partner_id
                                    # This is the *only* thing that the front end user will see/edit anyway when choosing billing address
                                    order.partner_invoice_id = partner_id

                                    if not kwargs.get('use_same'):
                                        kwargs['callback'] = kwargs.get('callback') or \
                                                         (not order.only_services and (
                                                                 mode[
                                                                     0] == 'edit' and '/shop/checkout' or '/shop/address'))
                                    # We need to update the pricelist(by the one selected by the customer), because onchange_partner reset it
                                    # We only need to update the pricelist when it is not redirected to /confirm_order
                                    if kwargs.get('callback', False) != '/shop/confirm_order':
                                        request.website.sale_get_order(update_pricelist=True)
                                elif mode[1] == 'shipping':
                                    order.partner_shipping_id = partner_id

                                if order.fiscal_position_id != fpos_before:
                                    order._recompute_taxes()

                                # TDE FIXME: don't ever do this
                                # -> TDE: you are the guy that did what we should never do in commit e6f038a
                                # order.message_partner_ids = [(4, partner_id), (3, request.website.partner_id.id)]
                                if not errors:
                                    request.session['without_error_redirect'] = kwargs.get('callback') or '/shop/confirm_order'
                                    return json.dumps({'id': 1})
                        render_values = {
                            'website_sale_order': order.id if order else -1,
                            'partner_id': partner_id,
                            'mode': mode,
                            'checkout': values,
                            'can_edit_vat': can_edit_vat,
                            'error': errors,
                            'callback': kwargs.get('callback'),
                            'only_services': order and order.only_services,
                            'account_on_checkout': request.website.account_on_checkout,
                            'is_public_user': request.website.is_public_user()
                        }
                        request.session['redirect_to_address'] = {'kwargs':kwargs, 'render_values':render_values}
                        return json.dumps({'id': 1})

                    if kwargs.get('form_name') == 'shipping_address_thankyou':
                        kwargs.pop('form_name')

                        name = kwargs['name'] if 'name' in kwargs.keys() else ''
                        city_id = kwargs['city_id'] if 'city_id' in kwargs.keys() else ''
                        street = kwargs['street'] if 'street' in kwargs.keys() else ''
                        street2 = kwargs['street2'] if 'street2' in kwargs.keys() else ''
                        zip = kwargs['zip'] if 'zip' in kwargs.keys() else ''
                        email = kwargs['email'] if 'email' in kwargs.keys() else ''
                        company_name = kwargs['company_name'] if 'company_name' in kwargs.keys() else ''
                        vat = kwargs['vat'] if 'vat' in kwargs.keys() else ''
                        state_id = int(kwargs['state_id']) if 'state_id' in kwargs.keys() else False
                        country_id = int(kwargs['country_id']) if 'country_id' in kwargs.keys() else False

                        partner_id = int(kwargs['id']) if 'id' in kwargs.keys() else -1
                        partner = request.env['res.partner'].sudo().search([('id', '=', int(partner_id))])
                        shipping_address = request.env['res.partner'].sudo().search(
                            [('id', '=', partner_id), ('type', '=', 'delivery')], limit=1)

                        selected_phone_country_id = kwargs['selected_phone_country_id'] if 'selected_phone_country_id' in kwargs.keys() else False
                        phone = kwargs['phone'] if 'phone' in kwargs.keys() else False
                        partner_country_id = 0
                        if selected_phone_country_id and phone:
                            partner_country_id = request.env['res.country'].sudo().browse(int(selected_phone_country_id))
                            del kwargs['selected_phone_country_id']
                            phone = '+' + str(partner_country_id.phone_code) + ' ' + phone


                        selected_mobile_country_id = kwargs['selected_mobile_country_id'] if 'selected_mobile_country_id' in kwargs.keys() else False
                        mobile = kwargs['mobile'] if 'mobile' in kwargs.keys() else False
                        partner_mobile_country_id = 0
                        if selected_mobile_country_id and mobile:
                            partner_mobile_country_id = request.env['res.country'].sudo().browse(int(selected_mobile_country_id))
                            del kwargs['selected_mobile_country_id']
                            mobile = '+' + str(partner_mobile_country_id.phone_code) + ' ' + mobile
                        if city_id:
                            new_city_id = request.env['res.city'].sudo().browse(int(city_id))
                        update_data = {
                            'name': name,
                            'city_id': int(new_city_id) if new_city_id else False,
                            'city': new_city_id.name if new_city_id else False,
                            'street': street,
                            'street2': street2,
                            'phone': phone if phone else '',
                            'zip': zip,
                            'mobile': mobile if mobile else '',
                            'email': email,
                            'company_name': company_name,
                            'vat': vat,
                            'state_id': state_id,
                            'country_id': country_id,
                        }
                        country = request.env['res.country'].sudo().browse(country_id if country_id else -1)
                        if shipping_address:
                            if vat and shipping_address._run_vat_test(vat, country,
                                                              shipping_address.is_company) is False:
                                partner_label = _("partner [%s]", shipping_address.name)
                                msg = shipping_address.sudo()._build_vat_error_message(
                                    country and country.code.lower() or None, vat, partner_label)
                                request.session['error_data'] = {
                                    'is_shipping_address': True,
                                    'partner': partner.id if partner else -1,
                                    'option': 'edit',
                                    'error_message': msg,
                                    'value': update_data,
                                    'partner_country_id': partner_country_id.id if partner_country_id else -1,
                                    'partner_mobile_country_id': partner_mobile_country_id.id if partner_mobile_country_id else -1,
                                }
                                return json.dumps({'id': partner_id})
                            else:
                                shipping_address.update(update_data)
                        else:
                            try:
                                if vat and shipping_address._run_vat_test(vat, country, shipping_address.is_company) is False:
                                    partner_label = _("partner [%s]", shipping_address.name)
                                    msg = shipping_address.sudo()._build_vat_error_message(country and country.code.lower() or None,vat, partner_label)
                                    request.session['error_data'] = {
                                        'is_shipping_address': True,
                                        'partner': partner.id if partner else -1,
                                        'option': 'edit',
                                        'error_message': msg,
                                        'value': update_data,
                                        'partner_country_id': partner_country_id.id if partner_country_id else -1,
                                        'partner_mobile_country_id': partner_mobile_country_id.id if partner_mobile_country_id else -1,
                                    }
                                    return json.dumps({'id': partner_id})
                                else:
                                    parent_partner = request.env['res.partner'].sudo().browse(partner_id)
                                    if parent_partner:
                                        parent_partner.child_ids.create({
                                            'type': 'delivery',
                                            'parent_id': parent_partner.id,
                                            **update_data
                                        })
                            except Exception as error:
                                request.session['error_data'] = {
                                    'is_shipping_address' : True,
                                    'partner': partner.id if partner else -1,
                                    'option': 'edit',
                                    'error_message': error,
                                    'value': update_data,
                                    'partner_country_id': partner_country_id.id if partner_country_id else -1,
                                    'partner_mobile_country_id':  partner_mobile_country_id.id if partner_mobile_country_id else -1,
                                }
                                return json.dumps({'id': partner_id})
                        return json.dumps({'id': partner_id})

                    if kwargs.get('form_name') == 'billing_address_thankyou':
                        kwargs.pop('form_name')

                        name = kwargs['name'] if 'name' in kwargs.keys() else ''
                        city_id = kwargs['city_id'] if 'city_id' in kwargs.keys() else ''
                        street = kwargs['street'] if 'street' in kwargs.keys() else ''
                        street2 = kwargs['street2'] if 'street2' in kwargs.keys() else ''
                        zip = kwargs['zip'] if 'zip' in kwargs.keys() else ''
                        email = kwargs['email'] if 'email' in kwargs.keys() else ''
                        company_name = kwargs['company_name'] if 'company_name' in kwargs.keys() else ''
                        vat = kwargs['vat'] if 'vat' in kwargs.keys() else ''
                        state_id = int(kwargs['state_id']) if 'state_id' in kwargs.keys() else False
                        country_id = int(kwargs['country_id']) if 'country_id' in kwargs.keys() else False

                        partner_id = int(kwargs['id']) if 'id' in kwargs.keys() else -1
                        partner = request.env['res.partner'].sudo().search([('id', '=', int(partner_id))])
                        billing_address = request.env['res.partner'].sudo().search(
                            [('id', '=', partner_id), ('type', '=', 'invoice')], limit=1)

                        selected_phone_country_id = kwargs['selected_phone_country_id'] if 'selected_phone_country_id' in kwargs.keys() else False
                        phone = kwargs['phone'] if 'phone' in kwargs.keys() else False
                        partner_country_id = 0
                        if selected_phone_country_id and phone:
                            partner_country_id = request.env['res.country'].sudo().browse(
                                int(selected_phone_country_id))
                            del kwargs['selected_phone_country_id']
                            phone = '+' + str(partner_country_id.phone_code) + ' ' + phone

                        selected_mobile_country_id = kwargs['selected_mobile_country_id'] if 'selected_mobile_country_id' in kwargs.keys() else False
                        mobile = kwargs['mobile'] if 'mobile' in kwargs.keys() else False
                        partner_mobile_country_id = 0
                        if selected_mobile_country_id and mobile:
                            partner_mobile_country_id = request.env['res.country'].sudo().browse(
                                int(selected_mobile_country_id))
                            del kwargs['selected_mobile_country_id']
                            mobile = '+' + str(partner_mobile_country_id.phone_code) + ' ' + mobile
                        if city_id:
                            new_city_id = request.env['res.city'].sudo().browse(int(city_id))
                        update_data = {
                            'name': name,
                            'city_id': int(new_city_id) if new_city_id else False,
                            'city': new_city_id.name if new_city_id else False,
                            'street': street,
                            'street2': street2,
                            'phone': phone if phone else '',
                            'zip': zip,
                            'mobile': mobile if mobile else '',
                            'email': email,
                            'company_name': company_name,
                            'vat': vat,
                            'state_id': state_id,
                            'country_id': country_id,
                        }
                        country = request.env['res.country'].sudo().browse(country_id if country_id else -1)
                        if billing_address:
                            if vat and billing_address._run_vat_test(vat, country, billing_address.is_company) is False:
                                partner_label = _("partner [%s]", billing_address.name)
                                msg = billing_address.sudo()._build_vat_error_message(country and country.code.lower() or None, vat, partner_label)
                                request.session['error_data'] = {
                                    'is_billing_address': True,
                                    'partner': partner.id if partner else -1,
                                    'option': 'edit',
                                    'error_message': msg,
                                    'value': update_data,
                                    'partner_country_id': partner_country_id.id if partner_country_id else -1,
                                    'partner_mobile_country_id': partner_mobile_country_id.id if partner_mobile_country_id else -1,
                                }
                                return json.dumps({'id': partner_id})
                            else:
                                billing_address.update(update_data)
                        else:
                            try:
                                if vat and billing_address._run_vat_test(vat, country, billing_address.is_company) is False:
                                    partner_label = _("partner [%s]", billing_address.name)
                                    msg = billing_address.sudo()._build_vat_error_message(
                                        country and country.code.lower() or None, vat,
                                        partner_label)
                                    request.session['error_data'] = {
                                        'is_billing_address': True,
                                        'partner': partner.id if partner else -1,
                                        'option': 'edit',
                                        'error_message': msg,
                                        'value': update_data,
                                        'partner_country_id': partner_country_id.id if partner_country_id else -1,
                                        'partner_mobile_country_id': partner_mobile_country_id.id if partner_mobile_country_id else -1,
                                    }
                                    return json.dumps({'id': partner_id})
                                else:
                                    parent_partner = request.env['res.partner'].sudo().browse(partner_id)
                                    if parent_partner:
                                        parent_partner.child_ids.create({
                                            'type': 'invoice',
                                            'parent_id': parent_partner.id,
                                            **update_data
                                        })
                            except Exception as error:
                                request.session['error_data'] = {
                                    'is_billing_address': True,
                                    'partner': partner.id if partner else -1,
                                    'option': 'edit',
                                    'error_message': error,
                                    'value': update_data,
                                    'partner_country_id': partner_country_id.id if partner_country_id else -1,
                                    'partner_mobile_country_id': partner_mobile_country_id.id if partner_mobile_country_id else -1,
                                }
                                return json.dumps({'id': partner_id})
                        return json.dumps({'id': partner_id})

                    if kwargs.get('form_name') == 'service_request':
                        partner_id = request.env.user.partner_id
                        res_partner = request.env['res.partner'].sudo().search([('id', '=', int(partner_id))])

                        if kwargs.get('customer_contact_no'):
                            country_id = request.env['res.country'].sudo().browse(
                                int(kwargs.get('country_id')))
                            new_phone = '+' + str(country_id.phone_code) + ' ' + kwargs.get('customer_contact_no')
                            kwargs.update({'customer_contact_no': new_phone})

                        if res_partner:
                            lead_id = request.env['crm.lead'].sudo().create({
                                'email_from': kwargs.get('customer_email'),
                                'phone': kwargs.get('customer_contact_no') if kwargs.get('customer_contact_no') else '',
                                'mobile': kwargs.get('customer_contact_no') if kwargs.get('customer_contact_no') else '',
                                'name': kwargs.get('customer_subject') if 'customer_subject' in kwargs.keys() else '',
                                'service': kwargs.get('service'),
                                'partner_id': partner_id.id,
                                'customer_message': "<p>" + kwargs.get('customer_message') + "</p>" if 'customer_message' in kwargs.keys() else '',
                                'country_id': country_id.id if country_id else False,
                                'type': 'lead',
                            })
                        else:
                            lead_id = request.env['crm.lead'].sudo().create({
                                'email_from': kwargs.get('customer_email'),
                                'phone': kwargs.get('customer_contact_no') if kwargs.get('customer_contact_no') else '',
                                'mobile': kwargs.get('customer_contact_no') if kwargs.get('customer_contact_no') else '',
                                'name': kwargs.get('customer_subject') if 'customer_subject' in kwargs.keys() else '',
                                'contact_name': kwargs.get('customer_name'),
                                'service': kwargs.get('service'),
                                'customer_message': "<p>" + kwargs.get('customer_message') + "</p>" if 'customer_message' in kwargs.keys() else '',
                                'country_id': country_id.id if country_id else False,
                                'type': 'lead',
                            })

                        email_values = {
                            'email_to': lead_id.email_from
                        }
                        user = request.env.user
                        contact_name = lead_id.contact_name
                        template = request.env.ref('cr_web_portal.lead_creation_email',
                                                   raise_if_not_found=False)
                        service_list = 'service_list'
                        if lead_id.service == 'enclosure_design':
                            service_list = 'Enclosure Design'
                        elif lead_id.service == 'fdm_modeling':
                            service_list = '3D Printing (FDM)'
                        elif lead_id.service == 'projection_printing':
                            service_list = '3D Printing (Projection)'
                        elif lead_id.service == 'sheet_metal_fabrication':
                            service_list = 'Sheet Metal Fabrication'
                        elif lead_id.service == 'cnc_machining':
                            service_list = 'CNC Machining'
                        elif lead_id.service == 'injection_molding':
                            service_list = 'Injection Molding'

                        service_link = kwargs.get('service')
                        redirect_path = '/'
                        if service_link == 'enclosure_design':
                            redirect_path = '/enclosure'
                        elif service_link == 'sheet_metal_fabrication':
                            redirect_path = '/sheet-metal-fabrication'
                        elif service_link == 'injection_molding':
                            redirect_path = '/injection-molding'
                        elif service_link == 'cnc_machining':
                            redirect_path = '/cnc-machining'
                        elif service_link == 'fdm_modeling':
                            redirect_path = '/fused-deposition-modeling'
                        elif service_link == 'projection_printing':
                            redirect_path = '/projection-printing-figure'

                        if user and template:
                            template.with_context(service_list=service_list, contact_name=contact_name,
                                                  lead_name=lead_id.name).sudo().send_mail(lead_id.user_id.id,
                                                                                           force_send=True,
                                                                                           email_values=email_values)
                        kwargs.pop('form_name')
                        request.session['redirect_path'] = redirect_path
                        request.session['service_list'] = service_list
                        return json.dumps({'name': lead_id.name})

                    if kwargs.get('form_name') == 'contactus':
                        if request.httprequest.method == 'GET':
                            return request.render('cr_web_portal.contact_us_page')
                        else:
                            user = request.env.user
                            categ_id = []
                            for i in kwargs:
                                if i.startswith('products_'):
                                    temp = i.split('_')
                                    categ_id.append(int(temp[1]))
                            if 'email' in kwargs.keys() and 'contact_no' in kwargs.keys():
                                if kwargs.get('country_id'):
                                    country_id = request.env['res.country'].sudo().browse(
                                        int(kwargs.get('country_id')))
                                    new_phone = '+' + str(country_id.phone_code) + ' ' + kwargs.get('contact_no')
                                    kwargs.update({'contact_no':new_phone})
                                if 'industry_category' in kwargs.keys():
                                    industry_category = int(kwargs.get('industry_category')) if kwargs.get('industry_category') != '' else False
                                else:
                                    industry_category = False
                                if 'sub_category' in kwargs.keys():
                                    sub_category = int(kwargs.get('sub_category')) if kwargs.get('sub_category') != '' else False
                                else:
                                    sub_category = False
                                if user._is_public() != False:
                                    value = {
                                        'contact_name': kwargs.get('partner_name') if 'partner_name' in kwargs.keys() else '',
                                        'email_from': kwargs.get('email') if 'email' in kwargs.keys() else '',
                                        'phone': kwargs.get('contact_no') if 'contact_no' in kwargs.keys() else '',
                                        'mobile': kwargs.get('contact_no') if 'contact_no' in kwargs.keys() else '',
                                        'partner_name': kwargs.get('company_name') if 'company_name' in kwargs.keys() else '',
                                        'industry_category_id': industry_category,
                                        'industry_sub_category_id': sub_category,
                                        'enquire_selection': (kwargs.get('enquire_selection')) if 'enquire_selection' in kwargs.keys() else '',
                                        'name': kwargs.get('customer_subject') if 'customer_subject' in kwargs.keys() else '',
                                        'type': 'lead',
                                        'is_enclosure_designing': True if 'Enclosure_designing' in  kwargs.keys() else False,
                                        'is_fdm_printing': True if 'FDM_Printing' in  kwargs.keys() else False,
                                        'is_projection_printing': True if 'Projection_Printing' in  kwargs.keys() else False,
                                        'is_sheet_metal_fabrication': True if 'Sheet_metal_fabrication' in  kwargs.keys() else False,
                                        'is_injection_moduling': True if 'Injection_Moulding' in  kwargs.keys() else False,
                                        'is_cnc_machining': True if  'CNC_Machining' in  kwargs.keys()  else False,
                                        'customer_message': "<p>"+kwargs.get('message')+"</p>" if  'message' in  kwargs.keys()  else '',
                                        'product_category_ids': [(6, 0, categ_id)],
                                    }
                                else:
                                    value = {
                                        'partner_id': user.partner_id.id,
                                        'email_from': kwargs.get('email') if 'email' in kwargs.keys() else '',
                                        'phone': kwargs.get('contact_no') if 'contact_no' in kwargs.keys() else '',
                                        'mobile': kwargs.get('contact_no') if 'contact_no' in kwargs.keys() else '',
                                        'partner_name': kwargs.get('company_name') if 'company_name' in kwargs.keys() else '',
                                        'industry_category_id': industry_category,
                                        'industry_sub_category_id': sub_category,
                                        'enquire_selection': (kwargs.get('enquire_selection')) if 'enquire_selection' in kwargs.keys() else '',
                                        'name': (kwargs.get('customer_subject')) if 'customer_subject' in kwargs.keys() else '',
                                        'type': 'lead',
                                        'is_enclosure_designing': True if 'Enclosure_designing' in kwargs.keys() else False,
                                        'is_fdm_printing': True if 'FDM_Printing' in kwargs.keys() else False,
                                        'is_projection_printing': True if 'Projection_Printing' in kwargs.keys() else False,
                                        'is_sheet_metal_fabrication': True if 'Sheet_metal_fabrication' in kwargs.keys() else False,
                                        'is_injection_moduling': True if 'Injection_Moulding' in kwargs.keys() else False,
                                        'is_cnc_machining': True if 'CNC_Machining' in kwargs.keys() else False,
                                        'customer_message': "<p>" + kwargs.get('message') + "</p>" if 'message' in kwargs.keys() else '',
                                        'product_category_ids': [(6, 0, categ_id)],
                                    }
                                lead_id = request.env['crm.lead'].sudo().create(value)
                                if lead_id:
                                    _logger.info('The Lead %s has been created By %s from this ip %s',lead_id.code ,user.name if not user._is_public() else 'Public User',request.httprequest.remote_addr)
                                service_list = []

                                if lead_id.is_enclosure_designing == True:
                                    service_list.append('Enclosure Designing')
                                if lead_id.is_fdm_printing == True:
                                    service_list.append('FDM Printing')
                                if lead_id.is_projection_printing == True:
                                    service_list.append('Projection Printing')
                                if lead_id.is_sheet_metal_fabrication == True:
                                    service_list.append('Sheet Metal Fabrication')
                                if lead_id.is_cnc_machining == True:
                                    service_list.append('Cnc Machining')
                                if lead_id.is_injection_moduling == True:
                                    service_list.append('Injection Molding')
                                email_values = {
                                    'email_to': lead_id.email_from
                                }

                                contact_name = lead_id.contact_name
                                phone = lead_id.phone
                                template = request.env.ref('cr_web_portal.lead_creation_email_from_contact_us_form',
                                                           raise_if_not_found=False)
                                if user and template:
                                    template.with_context(service_list=service_list,product_categories=lead_id.product_category_ids ,contact_name=contact_name,phone=phone,
                                                          lead_name=lead_id.name).sudo().send_mail(lead_id.user_id.id,
                                                                                                   force_send=True,
                                                                                           email_values=email_values)
                                kwargs.pop('form_name')
                                return json.dumps({'name': lead_id.id})

                    if kwargs.get('form_name') == 'sign_up_form':
                        if (kwargs.get('name') or kwargs.get('cname')) and kwargs.get('login') and kwargs.get('phone') and kwargs.get('lead_source'):
                            email = tools.email_normalize(kwargs['login'])
                            lead_source = kwargs['lead_source']
                            name = kwargs.get('name') or ''
                            phone = kwargs['phone']
                            industry = kwargs['industry']
                            sub_category = kwargs['sub_category']
                            partner_id = request.env['res.partner'].sudo().search([('email', '=', email)])
                            registration_type = kwargs['registration_type']
                            country_id = False
                            if kwargs.get('country_id'):
                                country_id = request.env['res.country'].sudo().browse(int(kwargs.get('country_id')))
                                new_phone = '+' + str(country_id.phone_code) + ' ' + phone
                                phone = new_phone
                            if not partner_id:
                                if registration_type == 'company':
                                    partner_id = request.env['res.partner'].sudo().create({
                                        'name': kwargs.get('cname') if kwargs.get('cname') else '',
                                        'email': email,
                                        'phone': phone,
                                        'mobile': phone,
                                        'company_name': kwargs.get('cname') if kwargs.get('cname') else '',
                                        'industry_main_category': int(industry) if industry else False,
                                        'industry_sub_category': int(sub_category) if sub_category else False,
                                        'lead_source': lead_source,
                                        'opt_out': True if kwargs.get('opt_check') else False,
                                        'company_type': registration_type,
                                        'registration_source': 'online'
                                    })
                                else:
                                    partner_id = request.env['res.partner'].sudo().create({
                                        'name': name,
                                        'email': email,
                                        'phone': phone,
                                        'mobile': phone,
                                        'company_name': kwargs.get('cname') if kwargs.get('cname') else '',
                                        'industry_main_category': int(industry) if industry else False,
                                        'industry_sub_category': int(sub_category) if sub_category else False,
                                        'lead_source': lead_source,
                                        'opt_out': True if kwargs.get('opt_check') else False,
                                        'company_type': registration_type,
                                        'registration_source': 'online'
                                    })
                                if country_id:
                                    partner_id.country_id = country_id.id
                                if partner_id:
                                    portal_wizard = request.env['portal.wizard'].sudo().with_context(
                                        active_ids=[partner_id.id]).create(
                                        {})
                                    portal_user = portal_wizard.user_ids
                                    portal_user.email = email
                                    portal_user.action_grant_access()
                                    if registration_type == 'company':
                                        if kwargs.get('name'):
                                            child_partner_id = request.env['res.partner'].sudo().create({
                                                'name': kwargs.get('name'),
                                                'parent_id': partner_id.id,
                                                'type': 'contact',
                                                'phone': phone,
                                                'mobile': phone,
                                                'industry_main_category': int(industry) if industry else False,
                                                'industry_sub_category': int(sub_category) if sub_category else False,
                                                'lead_source': lead_source,
                                                'opt_out': True if kwargs.get('opt_check') else False,
                                                'registration_source': 'online'
                                            })
                                    kwargs.pop('form_name')
                                    return json.dumps({'name': partner_id.id})

                            else:
                                return json.dumps({
                                    'name': 'error',
                                    'errors': [{'login': 'Another user is already registered using this email address.'}]
                                })


                        kwargs.pop('form_name')
                        return json.dumps({'name': partner_id.id})

                    if request.env.user.has_group('base.group_user'):
                        source_id = request.env.ref('cr_web_portal.utm_source_by_mech_power').id
                    else:
                        source_id = request.env.ref('cr_web_portal.utm_source_by_customer').id
                    if kwargs.get('form_name') == 'create_fdm_product':
                        so_id = False
                        if kwargs:
                            if 'recaptcha_token_response' in kwargs:
                                kwargs.pop('recaptcha_token_response')
                            if 'uv_printing_side' in kwargs:
                                uv_printing_side_id = int(kwargs['uv_printing_side'])
                                uv_printing_side_id = request.env['service.number.of.sides'].sudo().search([('id','=',uv_printing_side_id)])
                                kwargs['uv_printing_side'] = str(uv_printing_side_id.no_sides)

                            if 'fdm_material' in kwargs:
                                product_fdm_material = request.env['service.materials'].sudo().browse(int(kwargs['fdm_material']))
                                kwargs['fdm_material'] = product_fdm_material.name.strip() if product_fdm_material else False
                            if 'fdm_print_quality' in kwargs:
                                product_fdm_print_quality = request.env['service.print.quality'].sudo().browse(int(kwargs['fdm_print_quality']))
                                kwargs['fdm_print_quality'] = str(product_fdm_print_quality.thickness)+' mm' if product_fdm_print_quality else False
                            if 'fdm_infill' in kwargs:
                                product_fdm_infill = request.env['service.infill'].sudo().browse(int(kwargs['fdm_infill']))
                                kwargs['fdm_infill'] = str(int(product_fdm_infill.percent))+'%' if product_fdm_infill else False
                            list_price = 0.0
                            if 'fdm_product_price' in kwargs:
                                list_price = float(kwargs['fdm_product_price'])
                                kwargs.pop('fdm_product_price')
                            if 'lead_time' in kwargs:
                                lead_time = int(kwargs.get('lead_time'))
                                kwargs.pop('lead_time')
                            else:
                                lead_time = False

                            categ_id = request.env['product.category'].sudo().search(
                                [('parent_id.name', '=', 'Customer Specific Goods'), ('name', '=', 'Finished')],
                                limit=1)
                            uom_id = request.env['uom.uom'].sudo().search([('name', '=', 'NOS')], limit=1)

                            if "fdm_technical_drawings[0][0]" in list(kwargs.keys()):
                                kwargs['fdm_technical_drawings'] = kwargs.get('fdm_technical_drawings[0][0]')
                                kwargs.pop('fdm_technical_drawings[0][0]')

                            if "fdm_technical_drawings[1][0]" in list(kwargs.keys()):
                                kwargs['fdm_technical_drawings'] = kwargs.get('fdm_technical_drawings[1][0]')
                                kwargs.pop('fdm_technical_drawings[1][0]')

                            if "fdm_uv_printing_file[0][0]" in list(kwargs.keys()):
                                kwargs['fdm_uv_printing_file'] = kwargs.get('fdm_uv_printing_file[0][0]')
                                kwargs.pop('fdm_uv_printing_file[0][0]')

                            if "fdm_uv_printing_file[1][0]" in list(kwargs.keys()):
                                kwargs['fdm_uv_printing_file'] = kwargs.get('fdm_uv_printing_file[1][0]')
                                kwargs.pop('fdm_uv_printing_file[1][0]')

                            file1 = kwargs.get('fdm_technical_drawings')
                            file2 = kwargs.get('fdm_uv_printing_file')
                            if file1:
                                kwargs.pop('fdm_technical_drawings')
                                kwargs['fdm_technical_drawings_filename'] = file1.filename
                            if file2:
                                kwargs.pop('fdm_uv_printing_file')
                                kwargs['fdm_uv_printing_filename'] = file2.filename
                            template_value = {
                                'name': kwargs['fdm_product_name'],
                                'detailed_type': 'product',
                                'list_price': list_price if list_price != 0.0 else False ,
                                'categ_id': categ_id.id,
                                'uom_id': uom_id.id,
                                'uom_po_id': uom_id.id
                            }

                            kwargs['name'] = kwargs['fdm_product_name']
                            kwargs['detailed_type'] = 'product'
                            kwargs['list_price'] = list_price if list_price != 0.0 else False
                            kwargs['categ_id'] = categ_id.id
                            kwargs['uom_id'] = uom_id.id
                            kwargs['uom_po_id'] = uom_id.id
                            kwargs['is_fdm_service'] = True
                            kwargs['purchase_ok'] = False
                            kwargs['route_ids'] = [(6, 0, request.env.ref('mrp.route_warehouse0_manufacture').ids)]
                            kwargs.pop('form_name')

                            product_tmpl_id = request.env['product.template'].sudo().create(template_value)
                            if product_tmpl_id and product_tmpl_id.product_variant_ids:
                                product_tmpl_id.product_variant_ids[0].default_code = request.env[
                                    'ir.sequence'].sudo().next_by_code('product.product')
                                product_tmpl_id.product_variant_ids[0].sudo().write(kwargs)
                            f1 = False
                            f2 = False

                            if file1:
                                f1 = request.env['ir.attachment'].sudo().create({
                                    'name': file1.filename,
                                    'res_model': 'product.product',
                                    'res_id': product_tmpl_id.product_variant_ids[0].id,
                                    'res_field': 'fdm_technical_drawings',
                                    'datas': base64.b64encode(file1.read())
                                })
                            if file2:
                                f2 = request.env['ir.attachment'].sudo().create({
                                    'name': file2.filename,
                                    'res_model': 'product.product',
                                    'res_id': product_tmpl_id.product_variant_ids[0].id,
                                    'res_field': 'fdm_uv_printing_file',
                                    'datas': base64.b64encode(file2.read())
                                })

                            if 'fdm_is_uv_printing' in kwargs and kwargs['fdm_is_uv_printing'] in ['Yes', 'on']:
                                product_tmpl_id.product_variant_ids[0].fdm_is_uv_printing = True
                            else:
                                product_tmpl_id.product_variant_ids[0].fdm_is_uv_printing = False
                            data = {}
                            document = request.env['document.history'].sudo()
                            if f1:
                                data['document'] = f1.datas
                                data['product_id'] = product_tmpl_id.product_variant_ids[0].id
                                data['file_type'] = 'fdm_technical_drawings'
                                data['user_id'] = request.env.user.id
                                doc_id = document.create(data)
                                doc_id.name = kwargs['fdm_technical_drawings_filename']
                            if f2:
                                data['document'] = f2.datas
                                data['product_id'] = product_tmpl_id.product_variant_ids[0].id
                                data['file_type'] = 'fdm_uv_printing_file'
                                data['user_id'] = request.env.user.id
                                doc_id = document.create(data)
                                doc_id.name = kwargs['fdm_uv_printing_filename']
                            if list_price and lead_time:
                                order = request.website.sale_get_order()
                                if order and order.order_line:
                                    if not order.is_place_inquiry:
                                        order_line_values = order._cart_update(
                                            product_id=product_tmpl_id.product_variant_ids[0].id,
                                            add_qty=float(kwargs.get('fdm_quantity') or 1),
                                            allowd_for_customised=True,
                                        )
                                        if 'line_id' in order_line_values:
                                            order_line = request.env['sale.order.line'].sudo().search([('id','=',int(order_line_values['line_id']))])
                                            if order_line:
                                                order_line.sudo().write({
                                                    'x_studio_lead_time_in_days': lead_time if lead_time else False,
                                                })
                                        so_id = order

                                else:
                                    so_dict = request.website.sale_get_order(force_create=1)._cart_update(
                                        product_id=product_tmpl_id.product_variant_ids[0].id,
                                        add_qty=float(1),
                                        set_qty=float(kwargs.get('fdm_quantity') or 1),
                                        allowd_for_customised=True
                                    )
                                    if 'line_id' in so_dict:
                                        order_line = request.env['sale.order.line'].sudo().search([('id', '=', int(so_dict['line_id']))])
                                        if order_line:
                                            order_line.sudo().write({
                                                'x_studio_lead_time_in_days': lead_time if lead_time else False,
                                            })
                                            so_id = order_line.order_id
                                            so_id.sudo().write({
                                                'partner_id': request.env.user.partner_id.id,
                                                'service': 'fdm_modeling',
                                                'source_id': source_id
                                            })
                            else:
                                so_id = request.env['sale.order'].sudo().create({
                                    'partner_id': request.env.user.partner_id.id,
                                    'service': 'fdm_modeling',
                                    'state': 'inquiry',
                                    'order_line': [(0, 0, {
                                        'product_id': product_tmpl_id.product_variant_ids[0].id,
                                        'name': kwargs['name'],
                                        'product_uom_qty': kwargs.get('fdm_quantity') or 1,
                                        'x_studio_lead_time_in_days' : lead_time if lead_time else False,
                                    })],
                                    'source_id':source_id
                                })
                            # user = request.env.user
                            # email_values = {
                            #     'email_to': user.email_formatted,
                            #     'subject': 'We have received your FDM Modeling inquiry %s | Mech Power' % so_id.name,
                            # }
                            # template = request.env.ref('cr_web_portal.inquiry_creation_email_service',
                            #                            raise_if_not_found=False)
                            # value = {
                            #     'contact_name': user.name,
                            #     'service': 'FDM Modeling',
                            #     'inq_no': so_id.name if so_id else ''
                            # }
                            #
                            # if user and template:
                            #     template.with_context(cus_value=value).sudo().send_mail(user.id, force_send=True,
                            #                                                             email_values=email_values)
                            request.session['inquiry'] = so_id.name if so_id else ''
                            request.session['service'] = 'FDM Modeling'
                        return json.dumps({'name': so_id.name})

                    if kwargs.get('form_name') == 'create_enclosure_design':
                        so_id = False
                        if kwargs:
                            if kwargs.get('enclosure_design_product_communicater_phone'):
                                country_id = request.env['res.country'].sudo().browse(
                                    int(kwargs.get('country_id')))
                                new_phone = '+' + str(country_id.phone_code) + ' ' + kwargs.get(
                                    'enclosure_design_product_communicater_phone')
                                kwargs.update({'enclosure_design_product_communicater_phone': new_phone})
                            if kwargs.get('country_id'):
                                del kwargs['country_id']
                            categ_id = request.env['product.category'].sudo().search(
                                [('parent_id.name', '=', 'Customer Specific Goods'), ('name', '=', 'Finished')],
                                limit=1)
                            uom_id = request.env['uom.uom'].sudo().search([('name', '=', 'NOS')], limit=1)
                            if 'enclosure_design_product_file[0][0]' in list(kwargs.keys()):
                                kwargs['enclosure_design_product_file'] = kwargs.get('enclosure_design_product_file[0][0]')
                                kwargs.pop('enclosure_design_product_file[0][0]')
                            file = kwargs.get('enclosure_design_product_file')
                            if file:
                                kwargs.pop('enclosure_design_product_file')
                                kwargs['enclosure_design_product_filename'] = file.filename
                            template_value = {
                                'name': kwargs['enclosure_design_product_name'],
                                'detailed_type': 'product',
                                'list_price': 0,
                                'categ_id': categ_id.id,
                                'uom_id': uom_id.id,
                                'uom_po_id': uom_id.id
                            }
                            kwargs['name'] = kwargs['enclosure_design_product_name']
                            kwargs['detailed_type'] = 'product'
                            kwargs['list_price'] = 0
                            kwargs['categ_id'] = categ_id.id
                            kwargs['uom_id'] = uom_id.id
                            kwargs['uom_po_id'] = uom_id.id
                            kwargs['is_enclosure_service'] = True
                            product_tmpl_id = request.env['product.template'].sudo().create(template_value)
                            kwargs['purchase_ok'] = False
                            kwargs['route_ids'] = [(6, 0, request.env.ref('mrp.route_warehouse0_manufacture').ids)]
                            kwargs.pop('form_name')
                            if product_tmpl_id and product_tmpl_id.product_variant_ids:
                                product_tmpl_id.product_variant_ids[0].default_code = request.env[
                                    'ir.sequence'].sudo().next_by_code('product.product')
                                if 'recaptcha_token_response' in kwargs:
                                    kwargs.pop('recaptcha_token_response')
                                product_tmpl_id.product_variant_ids[0].write(kwargs)
                            f1 = False
                            if file:
                                f1 = request.env['ir.attachment'].sudo().create({
                                    'name': file.filename,
                                    'res_model': 'product.product',
                                    'res_id': product_tmpl_id.product_variant_ids[0].id,
                                    'res_field': 'enclosure_design_product_file',
                                    'datas': base64.b64encode(file.read())
                                })
                            so_id = request.env['sale.order'].sudo().create({
                                'partner_id': request.env.user.partner_id.id,
                                'service': 'enclosure_design',
                                'state': 'inquiry',
                                'order_line': [(0, 0, {'product_id': product_tmpl_id.product_variant_ids[0].id,
                                                       'name': kwargs['name']})],
                                'source_id':source_id
                            })
                            data = {}
                            document = request.env['document.history'].sudo()
                            if f1:
                                data['document'] = f1.datas
                                data['product_id'] = product_tmpl_id.product_variant_ids[0].id
                                data['file_type'] = 'enclosure_design_product_file'
                                data['user_id'] = request.env.user.id
                                doc_id = document.create(data)
                                doc_id.name = kwargs['name'] = kwargs['enclosure_design_product_name']
                            user = request.env.user
                            email_values = {
                                'email_to': user.email_formatted,
                                'subject': 'We have received your Enclosure Design inquiry %s | Mech Power' % so_id.name,
                            }
                            template = request.env.ref('cr_web_portal.inquiry_creation_email_service',
                                                       raise_if_not_found=False)
                            value = {
                                'contact_name': user.name,
                                'service': 'Enclosure Design',
                                'inq_no': so_id.name
                            }
                            if user and template:
                                template.with_context(cus_value=value).sudo().send_mail(user.id, force_send=True,
                                                                                        email_values=email_values)
                            request.session['inquiry'] = so_id.name
                            request.session['service'] = 'Enclosure Design'
                        return json.dumps({'name': so_id.name})

                    if kwargs.get('form_name') == 'create_metal_fab_product':
                        so_id = False
                        if kwargs:
                            categ_id = request.env['product.category'].sudo().search(
                                [('parent_id.name', '=', 'Customer Specific Goods'), ('name', '=', 'Finished')],
                                limit=1)
                            uom_id = request.env['uom.uom'].sudo().search([('name', '=', 'NOS')], limit=1)

                            if "metal_feb_technical_drawings[0][0]" in list(kwargs.keys()):
                                kwargs['metal_feb_technical_drawings'] = kwargs.get('metal_feb_technical_drawings[0][0]')
                                kwargs.pop('metal_feb_technical_drawings[0][0]')

                            if "metal_feb_technical_drawings[1][0]" in list(kwargs.keys()):
                                kwargs['metal_feb_technical_drawings'] = kwargs.get('metal_feb_technical_drawings[1][0]')
                                kwargs.pop('metal_feb_technical_drawings[1][0]')

                            if "metal_feb_uv_printing_file[0][0]" in list(kwargs.keys()):
                                kwargs['metal_feb_uv_printing_file'] = kwargs.get('metal_feb_uv_printing_file[0][0]')
                                kwargs.pop('metal_feb_uv_printing_file[0][0]')

                            if "metal_feb_uv_printing_file[1][0]" in list(kwargs.keys()):
                                kwargs['metal_feb_uv_printing_file'] = kwargs.get('metal_feb_uv_printing_file[1][0]')
                                kwargs.pop('metal_feb_uv_printing_file[1][0]')

                            file1 = kwargs.get('metal_feb_technical_drawings')
                            file2 = kwargs.get('metal_feb_uv_printing_file')
                            if file1:
                                kwargs.pop('metal_feb_technical_drawings')
                                kwargs['metal_feb_technical_drawings_filename'] = file1.filename
                            if file2:
                                kwargs.pop('metal_feb_uv_printing_file')
                                kwargs['metal_feb_uv_printing_filename'] = file2.filename
                            template_value = {
                                'name': kwargs['metal_feb_product_name'],
                                'detailed_type': 'product',
                                'list_price': 0,
                                'categ_id': categ_id.id,
                                'uom_id': uom_id.id,
                                'uom_po_id': uom_id.id
                            }
                            kwargs['name'] = kwargs['metal_feb_product_name']
                            kwargs['detailed_type'] = 'product'
                            kwargs['list_price'] = 0
                            kwargs['categ_id'] = categ_id.id
                            kwargs['uom_id'] = uom_id.id
                            kwargs['uom_po_id'] = uom_id.id
                            kwargs['is_metal_feb_service'] = True
                            product_tmpl_id = request.env['product.template'].sudo().create(template_value)
                            kwargs['purchase_ok'] = False
                            kwargs['route_ids'] = [(6, 0, request.env.ref('mrp.route_warehouse0_manufacture').ids)]
                            kwargs.pop('form_name')

                            if product_tmpl_id and product_tmpl_id.product_variant_ids:
                                product_tmpl_id.product_variant_ids[0].default_code = request.env[
                                    'ir.sequence'].sudo().next_by_code('product.product')
                                if 'recaptcha_token_response' in kwargs:
                                    kwargs.pop('recaptcha_token_response')
                                product_tmpl_id.product_variant_ids[0].write(kwargs)
                            f1 = False
                            f2 = False
                            if file1:
                                f1 = request.env['ir.attachment'].sudo().create({
                                    'name': file1.filename,
                                    'res_model': 'product.product',
                                    'res_id': product_tmpl_id.product_variant_ids[0].id,
                                    'res_field': 'metal_feb_technical_drawings',
                                    'datas': base64.b64encode(file1.read())
                                })
                            if file2:
                                f2 = request.env['ir.attachment'].sudo().create({
                                    'name': file2.filename,
                                    'res_model': 'product.product',
                                    'res_id': product_tmpl_id.product_variant_ids[0].id,
                                    'res_field': 'metal_feb_uv_printing_file',
                                    'datas': base64.b64encode(file2.read())
                                })
                            if 'metal_feb_is_uv_printing' in kwargs and kwargs['metal_feb_is_uv_printing'] in ['Yes', 'on']:
                                product_tmpl_id.product_variant_ids[0].metal_feb_is_uv_printing = True
                            else:
                                product_tmpl_id.product_variant_ids[0].metal_feb_is_uv_printing = False

                            if 'metal_feb_is_welding' in kwargs and kwargs['metal_feb_is_welding'] in ['Yes','on']:
                                product_tmpl_id.product_variant_ids[0].metal_feb_is_welding = True
                            else:
                                product_tmpl_id.product_variant_ids[0].metal_feb_is_welding = False
                            data = {}
                            document = request.env['document.history'].sudo()
                            if f1:
                                data['document'] = f1.datas
                                data['product_id'] = product_tmpl_id.product_variant_ids[0].id
                                data['file_type'] = 'metal_feb_technical_drawings'
                                data['user_id'] = request.env.user.id
                                doc_id = document.create(data)
                                doc_id.name = kwargs['metal_feb_technical_drawings_filename']
                            if f2:
                                data['document'] = f2.datas
                                data['product_id'] = product_tmpl_id.product_variant_ids[0].id
                                data['file_type'] = 'metal_feb_uv_printing_file'
                                data['user_id'] = request.env.user.id
                                doc_id = document.create(data)
                                doc_id.name = kwargs['metal_feb_uv_printing_filename']
                            so_id = request.env['sale.order'].sudo().create({
                                'partner_id': request.env.user.partner_id.id,
                                'service': 'sheet_metal_fabrication',
                                'state': 'inquiry',
                                'order_line': [(0, 0, {
                                    'product_id': product_tmpl_id.product_variant_ids[0].id,
                                    'name': kwargs['name'],
                                    'product_uom_qty': kwargs.get('metal_feb_quantity') or 1
                                })],
                                'source_id':source_id
                            })
                            user = request.env.user
                            email_values = {
                                'email_to': user.email_formatted,
                                'subject': 'We have received your Sheet Metal Fabrication inquiry %s | Mech Power' % so_id.name,
                            }
                            template = request.env.ref('cr_web_portal.inquiry_creation_email_service',
                                                       raise_if_not_found=False)
                            value = {
                                'contact_name': user.name,
                                'service': 'Sheet Metal Fabrication',
                                'inq_no': so_id.name
                            }
                            if user and template:
                                template.with_context(cus_value=value).sudo().send_mail(user.id, force_send=True,
                                                                                        email_values=email_values)
                            request.session['inquiry'] = so_id.name
                            request.session['service'] = 'Sheet Metal Fabrication'
                        return json.dumps({'name': so_id.name})

                    if kwargs.get('form_name') == 'create_injection_molding_product':
                        so_id = False
                        if kwargs:
                            categ_id = request.env['product.category'].sudo().search(
                                [('parent_id.name', '=', 'Customer Specific Goods'), ('name', '=', 'Finished')],
                                limit=1)
                            uom_id = request.env['uom.uom'].sudo().search([('name', '=', 'NOS')], limit=1)

                            if "injection_mold_upload_technical_drawing[0][0]" in list(kwargs.keys()):
                                kwargs['injection_mold_upload_technical_drawing'] = kwargs.get('injection_mold_upload_technical_drawing[0][0]')
                                kwargs.pop('injection_mold_upload_technical_drawing[0][0]')

                            if "injection_mold_upload_technical_drawing[1][0]" in list(kwargs.keys()):
                                kwargs['injection_mold_upload_technical_drawing'] = kwargs.get('injection_mold_upload_technical_drawing[1][0]')
                                kwargs.pop('injection_mold_upload_technical_drawing[1][0]')

                            if "injection_uv_printing_file[0][0]" in list(kwargs.keys()):
                                kwargs['injection_uv_printing_file'] = kwargs.get('injection_uv_printing_file[0][0]')
                                kwargs.pop('injection_uv_printing_file[0][0]')

                            if "injection_uv_printing_file[1][0]" in list(kwargs.keys()):
                                kwargs['injection_uv_printing_file'] = kwargs.get('injection_uv_printing_file[1][0]')
                                kwargs.pop('injection_uv_printing_file[1][0]')

                            file1 = kwargs.get('injection_mold_upload_technical_drawing')
                            file2 = kwargs.get('injection_uv_printing_file')
                            if file1:
                                kwargs.pop('injection_mold_upload_technical_drawing')
                                kwargs['injection_mold_upload_technical_drawing_filename'] = file1.filename
                            if file2:
                                kwargs.pop('injection_uv_printing_file')
                                kwargs['injection_uv_printing_filename'] = file2.filename
                            template_value = {
                                'name': kwargs['injection_mold_product_name'],
                                'detailed_type': 'product',
                                'list_price': 0,
                                'categ_id': categ_id.id,
                                'uom_id': uom_id.id,
                                'uom_po_id': uom_id.id
                            }
                            kwargs['name'] = kwargs['injection_mold_product_name']
                            kwargs['detailed_type'] = 'product'
                            kwargs['list_price'] = 0
                            kwargs['categ_id'] = categ_id.id
                            kwargs['uom_id'] = uom_id.id
                            kwargs['uom_po_id'] = uom_id.id
                            kwargs.pop('form_name')

                            kwargs['is_injection_mold_service'] = True
                            product_tmpl_id = request.env['product.template'].sudo().create(template_value)

                            kwargs['purchase_ok'] = False
                            kwargs['route_ids'] = [(6, 0, request.env.ref('mrp.route_warehouse0_manufacture').ids)]

                            if product_tmpl_id and product_tmpl_id.product_variant_ids:
                                product_tmpl_id.product_variant_ids[0].default_code = request.env[
                                    'ir.sequence'].sudo().next_by_code('product.product')
                                if 'recaptcha_token_response' in kwargs:
                                    kwargs.pop('recaptcha_token_response')
                                product_tmpl_id.product_variant_ids[0].write(kwargs)
                            f1 = False
                            f2 = False
                            if file1:
                                f1 = request.env['ir.attachment'].sudo().create({
                                    'name': file1.filename,
                                    'res_model': 'product.product',
                                    'res_id': product_tmpl_id.product_variant_ids[0].id,
                                    'res_field': 'injection_mold_upload_technical_drawing',
                                    'datas': base64.b64encode(file1.read())
                                })
                            if file2:
                                f2 = request.env['ir.attachment'].sudo().create({
                                    'name': file2.filename,
                                    'res_model': 'product.product',
                                    'res_id': product_tmpl_id.product_variant_ids[0].id,
                                    'res_field': 'injection_uv_printing_file',
                                    'datas': base64.b64encode(file2.read())
                                })
                            if 'injection_is_uv_printing' in kwargs and kwargs['injection_is_uv_printing'] in ['Yes','on']:
                                product_tmpl_id.product_variant_ids[0].injection_is_uv_printing = True
                            else:
                                product_tmpl_id.product_variant_ids[0].injection_is_uv_printing = False
                            data = {}
                            document = request.env['document.history'].sudo()
                            if f1:
                                data['document'] = f1.datas
                                data['product_id'] = product_tmpl_id.product_variant_ids[0].id
                                data['file_type'] = 'injection_mold_upload_technical_drawing'
                                data['user_id'] = request.env.user.id
                                doc_id = document.create(data)
                                doc_id.name = f1.name
                            if f2:
                                data['document'] = f2.datas
                                data['product_id'] = product_tmpl_id.product_variant_ids[0].id
                                data['file_type'] = 'injection_uv_printing_file'
                                data['user_id'] = request.env.user.id
                                doc_id = document.create(data)
                                doc_id.name = f2.name
                            so_id = request.env['sale.order'].sudo().create({
                                'partner_id': request.env.user.partner_id.id,
                                'service': 'injection_molding',
                                'state': 'inquiry',
                                'order_line': [(0, 0, {
                                    'product_id': product_tmpl_id.product_variant_ids[0].id,
                                    'name': kwargs['name'],
                                    'product_uom_qty': kwargs.get('injection_mold_quantity') or 1
                                })],
                                'source_id':source_id
                            })
                            user = request.env.user
                            email_values = {
                                'email_to': user.email_formatted,
                                'subject': 'We have received your Injection Molding inquiry %s | Mech Power' % so_id.name,
                            }
                            template = request.env.ref('cr_web_portal.inquiry_creation_email_service',
                                                       raise_if_not_found=False)
                            value = {
                                'contact_name': user.name,
                                'service': 'Injection Molding',
                                'inq_no': so_id.name
                            }
                            if user and template:
                                template.with_context(cus_value=value).sudo().send_mail(user.id, force_send=True,
                                                                                        email_values=email_values)
                            request.session['inquiry'] = so_id.name
                            request.session['service'] = 'Injection Molding'
                        return json.dumps({'name': so_id.name})

                    if kwargs.get('form_name') == 'create_projection_product':
                        so_id = False
                        if kwargs:
                            if 'recaptcha_token_response' in kwargs:
                                kwargs.pop('recaptcha_token_response')
                            if 'uv_printing_side' in kwargs:
                                uv_printing_side_id = int(kwargs['uv_printing_side'])
                                uv_printing_side_id = request.env['service.number.of.sides'].sudo().search(
                                    [('id', '=', uv_printing_side_id)])
                                kwargs['uv_printing_side'] = str(uv_printing_side_id.no_sides)
                            list_price = 0.0
                            if 'projection_product_price' in kwargs:
                                list_price = float(kwargs['projection_product_price'])
                                kwargs.pop('projection_product_price')
                            if 'lead_time' in kwargs:
                                lead_time = int(kwargs.get('lead_time'))
                                kwargs.pop('lead_time')
                            else:
                                lead_time = False
                            if 'projection_material' in kwargs:
                                product_projection_material = request.env['service.materials'].sudo().browse(int(kwargs['projection_material']))
                                kwargs['projection_material'] = product_projection_material.name.strip() if product_projection_material else False

                            if 'projection_print_quality' in kwargs:
                                product_projection_print_quality = request.env['service.print.quality'].sudo().browse(int(kwargs['projection_print_quality']))
                                kwargs['projection_print_quality'] = str(int(product_projection_print_quality.thickness))+' micron' if product_projection_print_quality else False

                            categ_id = request.env['product.category'].sudo().search(
                                [('parent_id.name', '=', 'Customer Specific Goods'), ('name', '=', 'Finished')],
                                limit=1)
                            uom_id = request.env['uom.uom'].sudo().search([('name', '=', 'NOS')], limit=1)
                            if "projection_uv_printing_file[0][0]" in list(kwargs.keys()):
                                kwargs['projection_uv_printing_file'] = kwargs.get(
                                    'projection_uv_printing_file[0][0]')
                                kwargs.pop('projection_uv_printing_file[0][0]')

                            if "projection_uv_printing_file[1][0]" in list(kwargs.keys()):
                                kwargs['projection_uv_printing_file'] = kwargs.get(
                                    'projection_uv_printing_file[1][0]')
                                kwargs.pop('projection_uv_printing_file[1][0]')

                            if "projection_technical_drawings[0][0]" in list(kwargs.keys()):
                                kwargs['projection_technical_drawings'] = kwargs.get('projection_technical_drawings[0][0]')
                                kwargs.pop('projection_technical_drawings[0][0]')

                            if "projection_technical_drawings[1][0]" in list(kwargs.keys()):
                                kwargs['projection_technical_drawings'] = kwargs.get('projection_technical_drawings[1][0]')
                                kwargs.pop('projection_technical_drawings[1][0]')

                            file1 = kwargs.get('projection_uv_printing_file')
                            file2 = kwargs.get('projection_technical_drawings')
                            if file1:
                                kwargs.pop('projection_uv_printing_file')
                                kwargs['projection_uv_printing_filename'] = file1.filename
                            if file2:
                                kwargs.pop('projection_technical_drawings')
                                kwargs['projection_technical_drawings_filename'] = file2.filename
                            template_value = {
                                'name': kwargs['projection_product_name'],
                                'detailed_type': 'product',
                                'list_price': list_price if list_price != 0.0 else False ,
                                'categ_id': categ_id.id,
                                'uom_id': uom_id.id,
                                'uom_po_id': uom_id.id
                            }
                            kwargs['name'] = kwargs['projection_product_name']
                            kwargs['detailed_type'] = 'product'
                            kwargs['list_price'] = list_price if list_price != 0.0 else False
                            kwargs['categ_id'] = categ_id.id
                            kwargs['uom_id'] = uom_id.id
                            kwargs['uom_po_id'] = uom_id.id
                            kwargs['is_fdm_service'] = True
                            kwargs.pop('form_name')
                            kwargs['is_projection_service'] = True
                            product_tmpl_id = request.env['product.template'].sudo().create(template_value)
                            kwargs['purchase_ok'] = False
                            kwargs['route_ids'] = [(6, 0, request.env.ref('mrp.route_warehouse0_manufacture').ids)]
                            if product_tmpl_id and product_tmpl_id.product_variant_ids:
                                product_tmpl_id.product_variant_ids[0].default_code = request.env[
                                    'ir.sequence'].sudo().next_by_code('product.product')
                                if 'recaptcha_token_response' in kwargs:
                                    kwargs.pop('recaptcha_token_response')
                                product_tmpl_id.product_variant_ids[0].write(kwargs)
                            f1 = False
                            f2 = False
                            if file1:
                                f1 = request.env['ir.attachment'].sudo().create({
                                    'name': file1.filename,
                                    'res_model': 'product.product',
                                    'res_id': product_tmpl_id.product_variant_ids[0].id,
                                    'res_field': 'projection_uv_printing_file',
                                    'datas': base64.b64encode(file1.read())
                                })
                            if file2:
                                f2 = request.env['ir.attachment'].sudo().create({
                                    'name': file2.filename,
                                    'res_model': 'product.product',
                                    'res_id': product_tmpl_id.product_variant_ids[0].id,
                                    'res_field': 'projection_technical_drawings',
                                    'datas': base64.b64encode(file2.read())
                                })
                            if 'projection_is_uv_printing' in kwargs and kwargs['projection_is_uv_printing'] in ['Yes','on']:
                                product_tmpl_id.product_variant_ids[0].projection_is_uv_printing = True
                            else:
                                product_tmpl_id.product_variant_ids[0].projection_is_uv_printing = False
                            data = {}
                            document = request.env['document.history'].sudo()
                            if f1:
                                data['document'] = f1.datas
                                data['product_id'] = product_tmpl_id.product_variant_ids[0].id
                                data['file_type'] = 'projection_uv_printing_file'
                                data['user_id'] = request.env.user.id
                                doc_id = document.create(data)
                                doc_id.name = kwargs['projection_uv_printing_filename']
                            if f2:
                                data['document'] = f2.datas
                                data['product_id'] = product_tmpl_id.product_variant_ids[0].id
                                data['file_type'] = 'projection_technical_drawings'
                                data['user_id'] = request.env.user.id
                                doc_id = document.create(data)
                                doc_id.name = kwargs['projection_technical_drawings_filename']

                            if list_price:
                                order = request.website.sale_get_order()
                                if order and order.order_line:
                                    if not order.is_place_inquiry:
                                        order_line_values = order._cart_update(
                                            product_id=product_tmpl_id.product_variant_ids[0].id,
                                            add_qty=float(kwargs.get('projection_quantity') or 1),
                                            allowd_for_customised=True
                                        )
                                        if 'line_id' in order_line_values:
                                            order_line = request.env['sale.order.line'].sudo().search([('id','=',int(order_line_values['line_id']))])
                                            if order_line:
                                                order_line.sudo().write({
                                                    'x_studio_lead_time_in_days': lead_time if lead_time else False,
                                                })
                                        so_id = order
                                else:
                                    so_dict = request.website.sale_get_order(force_create=1)._cart_update(
                                        product_id=product_tmpl_id.product_variant_ids[0].id,
                                        add_qty=float(1),
                                        set_qty=float(kwargs.get('projection_quantity') or 1),
                                        allowd_for_customised=True
                                    )
                                    if 'line_id' in so_dict:
                                        order_line = request.env['sale.order.line'].sudo().search(
                                            [('id', '=', int(so_dict['line_id']))])
                                        if order_line:
                                            order_line.sudo().write({
                                                'x_studio_lead_time_in_days': lead_time if lead_time else False,
                                            })
                                            so_id = order_line.order_id
                                            so_id.sudo().write({
                                                'partner_id': request.env.user.partner_id.id,
                                                'service': 'projection_printing',
                                                'source_id': source_id
                                            })
                            else:
                                so_id = request.env['sale.order'].sudo().create({
                                    'partner_id': request.env.user.partner_id.id,
                                    'service': 'projection_printing',
                                    'state': 'inquiry',
                                    'order_line': [(0, 0, {
                                        'product_id': product_tmpl_id.product_variant_ids[0].id,
                                        'name': kwargs['name'],
                                        'product_uom_qty': kwargs.get('projection_quantity') or 1,
                                        'x_studio_lead_time_in_days': lead_time if lead_time else False,
                                    })],
                                    'source_id':source_id
                                })
                            # user = request.env.user
                            # email_values = {
                            #     'email_to': user.email_formatted,
                            #     'subject': 'We have received your Projection Printing inquiry %s | Mech Power' % so_id.name,
                            # }
                            # template = request.env.ref('cr_web_portal.inquiry_creation_email_service',
                            #                            raise_if_not_found=False)
                            # value = {
                            #     'contact_name': user.name,
                            #     'service': 'Projection Printing',
                            #     'inq_no': so_id.name
                            # }
                            # if user and template:
                            #     template.with_context(cus_value=value).sudo().send_mail(user.id, force_send=True,
                            #                                                             email_values=email_values)
                            request.session['inquiry'] = so_id.name if so_id else ''
                            request.session['service'] = 'Projection Printing'
                        return json.dumps({'name':so_id.name})

                    if kwargs.get('form_name') == 'create_cnc_product':
                        so_id = False
                        if kwargs:
                            categ_id = request.env['product.category'].sudo().search(
                                [('parent_id.name', '=', 'Customer Specific Goods'), ('name', '=', 'Finished')],
                                limit=1)
                            uom_id = request.env['uom.uom'].sudo().search([('name', '=', 'NOS')], limit=1)

                            if "cnc_machining_upload_technical_drawing[0][0]" in list(kwargs.keys()):
                                kwargs['cnc_machining_upload_technical_drawing'] = kwargs.get('cnc_machining_upload_technical_drawing[0][0]')
                                kwargs.pop('cnc_machining_upload_technical_drawing[0][0]')

                            if "cnc_machining_upload_technical_drawing[1][0]" in list(kwargs.keys()):
                                kwargs['cnc_machining_upload_technical_drawing'] = kwargs.get('cnc_machining_upload_technical_drawing[1][0]')
                                kwargs.pop('cnc_machining_upload_technical_drawing[1][0]')

                            if "cnc_uv_printing_file[0][0]" in list(kwargs.keys()):
                                kwargs['cnc_uv_printing_file'] = kwargs.get('cnc_uv_printing_file[0][0]')
                                kwargs.pop('cnc_uv_printing_file[0][0]')

                            if "cnc_uv_printing_file[1][0]" in list(kwargs.keys()):
                                kwargs['cnc_uv_printing_file'] = kwargs.get('cnc_uv_printing_file[1][0]')
                                kwargs.pop('cnc_uv_printing_file[1][0]')

                            file1 = kwargs.get('cnc_machining_upload_technical_drawing')
                            file2 = kwargs.get('cnc_uv_printing_file')
                            if file1:
                                kwargs.pop('cnc_machining_upload_technical_drawing')
                                kwargs['cnc_machining_upload_technical_drawing_filename'] = file1.filename
                            if file2:
                                kwargs.pop('cnc_uv_printing_file')
                                kwargs['cnc_uv_printing_filename'] = file2.filename
                            template_value = {
                                'name': kwargs['cnc_machining_product_name'],
                                'detailed_type': 'product',
                                'list_price': 0,
                                'categ_id': categ_id.id,
                                'uom_id': uom_id.id,
                                'uom_po_id': uom_id.id
                            }
                            kwargs['name'] = kwargs['cnc_machining_product_name']
                            kwargs['detailed_type'] = 'product'
                            kwargs['list_price'] = 0
                            kwargs['categ_id'] = categ_id.id
                            kwargs['uom_id'] = uom_id.id
                            kwargs['uom_po_id'] = uom_id.id
                            kwargs.pop('form_name')
                            kwargs['is_cnc_machining_service'] = True
                            product_tmpl_id = request.env['product.template'].sudo().create(template_value)

                            kwargs['purchase_ok'] = False
                            kwargs['route_ids'] = [(6, 0, request.env.ref('mrp.route_warehouse0_manufacture').ids)]

                            if product_tmpl_id and product_tmpl_id.product_variant_ids:
                                product_tmpl_id.product_variant_ids[0].default_code = request.env[
                                    'ir.sequence'].sudo().next_by_code('product.product')
                                if 'recaptcha_token_response' in kwargs:
                                    kwargs.pop('recaptcha_token_response')
                                product_tmpl_id.product_variant_ids[0].write(kwargs)
                            f1 = False
                            f2 = False
                            if file1:
                                f1 = request.env['ir.attachment'].sudo().create({
                                    'name': file1.filename,
                                    'res_model': 'product.product',
                                    'res_id': product_tmpl_id.product_variant_ids[0].id,
                                    'res_field': 'cnc_machining_upload_technical_drawing',
                                    'datas': base64.b64encode(file1.read())
                                })
                            if file2:
                                f2 = request.env['ir.attachment'].sudo().create({
                                    'name': file2.filename,
                                    'res_model': 'product.product',
                                    'res_id': product_tmpl_id.product_variant_ids[0].id,
                                    'res_field': 'cnc_uv_printing_file',
                                    'datas': base64.b64encode(file2.read())
                                })
                            if 'cnc_is_uv_printing' in kwargs and kwargs['cnc_is_uv_printing'] in ['Yes','on']:
                                product_tmpl_id.product_variant_ids[0].cnc_is_uv_printing = True
                            else:
                                product_tmpl_id.product_variant_ids[0].cnc_is_uv_printing = False
                            data = {}
                            document = request.env['document.history'].sudo()
                            if f1:
                                data['document'] = f1.datas
                                data['product_id'] = product_tmpl_id.product_variant_ids[0].id
                                data['file_type'] = 'cnc_machining_upload_technical_drawing'
                                data['user_id'] = request.env.user.id
                                doc_id = document.create(data)
                                doc_id.name = kwargs['cnc_machining_upload_technical_drawing_filename']
                            if f2:
                                data['document'] = f2.datas
                                data['product_id'] = product_tmpl_id.product_variant_ids[0].id
                                data['file_type'] = 'cnc_uv_printing_file'
                                data['user_id'] = request.env.user.id
                                doc_id = document.create(data)
                                doc_id.name = kwargs['cnc_uv_printing_filename']
                            so_id = request.env['sale.order'].sudo().create({
                                'partner_id': request.env.user.partner_id.id,
                                'service': 'cnc_machining',
                                'state': 'inquiry',
                                'order_line': [(0, 0, {
                                    'product_id': product_tmpl_id.product_variant_ids[0].id,
                                    'name': kwargs['name'],
                                    'product_uom_qty': kwargs.get('cnc_machining_quantity') or 1
                                })],
                                'source_id':source_id
                            })
                            user = request.env.user
                            email_values = {
                                'email_to': user.email_formatted,
                                'subject': 'We have received your CNC Machining inquiry %s | Mech Power' % so_id.name,
                            }
                            template = request.env.ref('cr_web_portal.inquiry_creation_email_service',
                                                       raise_if_not_found=False)
                            value = {
                                'contact_name': user.name,
                                'service': 'CNC Machining',
                                'inq_no': so_id.name
                            }
                            if user and template:
                                template.with_context(cus_value=value).sudo().send_mail(user.id, force_send=True,
                                                                                        email_values=email_values)
                            request.session['inquiry'] = so_id.name
                            request.session['service'] = 'CNC Machining'
                        return json.dumps({'name':so_id.name})

                    return self._handle_website_form(model_name, **kwargs)
            error = _("Suspicious activity detected by Google reCaptcha.")
        except (ValidationError, UserError) as e:
            error = e.args[0]
        return json.dumps({
            'error': error,
        })
