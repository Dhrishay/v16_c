# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.web.controllers.home import Home

import logging
from odoo.addons.web.controllers.home import ensure_db, Home, SIGN_UP_REQUEST_PARAMS, LOGIN_SUCCESSFUL_PARAMS
from odoo.tools import OrderedSet, escape_psql, html_escape as escape

from odoo.exceptions import UserError
from textwrap import shorten
import odoo
import odoo.modules.registry
from odoo import http
from odoo.http import request
from odoo.tools.translate import _
import re

_logger = logging.getLogger(__name__)

class MechPowerWebLogin(Home):


    def _prepare_signup_values(self, qcontext):
        values = {key: qcontext.get(key) for key in ('login', 'name', 'password')}
        if not values:
            raise UserError(_("The form was not properly filled in."))
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("The password you entered did not match."))
        if 'login' in values:
            email = values['login']
            partner = request.env['res.partner'].sudo().search([('email','=',email)],limit=1)
            incomplete_registration_tag_id = request.env.ref('cr_web_portal.incomplete_registration_tag').sudo()
            if partner and incomplete_registration_tag_id:
                partner.category_id = [(5,0, [incomplete_registration_tag_id.id])]
            mailing_contact_id = request.env["mailing.contact"].sudo().search([('email', '=', email)], limit=1)
            remove_mail_list_ids = [request.env.ref('mechpower_base_extended.never_connected_customer_mailing_list').sudo().id,
                                    request.env.ref('mechpower_base_extended.lead_mailing_list').sudo().id
                                    ]
            add_mailing_list_ids = [
                request.env.ref('mechpower_base_extended.product_and_service_mailing_list').sudo().id,
                request.env.ref('mechpower_base_extended.design_best_practices_mailing_list').sudo().id,
                request.env.ref('mechpower_base_extended.industry_insights_mailing_list').sudo().id,
                request.env.ref('mechpower_base_extended.events_mailing_list').sudo().id,
                request.env.ref('mechpower_base_extended.customer_mailing_list').sudo().id
            ]
            mailing_contact_id.list_ids = [(3, ml)for ml in remove_mail_list_ids]
            if partner.opt_out and partner.registration_source == 'online':
                if mailing_contact_id:
                    mailing_contact_id.list_ids = [(4, ml)for ml in add_mailing_list_ids]
                else:
                    contact_vals = {
                        "name": partner.name,
                        "email": email,
                        "list_ids": [(6, 0, add_mailing_list_ids)],
                        "company_name": partner.company_id.name or False,
                        "country_id": partner.country_id.id or False,
                    }
                    mailing_contact_id = request.env["mailing.contact"].sudo().create(contact_vals)
            elif partner.registration_source == 'offline':
                if mailing_contact_id:
                    mailing_contact_id.list_ids = [(4, ml)for ml in add_mailing_list_ids]
                else:
                    contact_vals = {
                        "name": partner.name,
                        "email": email,
                        "list_ids": [(6, 0, add_mailing_list_ids)],
                        "company_name": partner.company_id.name or False,
                        "country_id": partner.country_id.id or False,
                    }
                    mailing_contact_id = request.env["mailing.contact"].sudo().create(contact_vals)

        supported_lang_codes = [code for code, _ in request.env['res.lang'].get_installed()]
        lang = request.context.get('lang', '')
        if lang in supported_lang_codes:
            values['lang'] = lang
        return values
