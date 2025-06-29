# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import re
import csv
import odoo
from unidecode import unidecode
from datetime import datetime, timedelta


class ResPartner(models.Model):
    _inherit = "res.partner"

    pan_number = fields.Char(size=10)
    product_count = fields.Integer(compute='compute_product_count')
    last_inquiry_date = fields.Datetime('Last Inquiry Date')
    last_order_date = fields.Datetime('Last Order Date')

    @api.onchange('state_id')
    def _onchange_state(self):
        super()._onchange_state()
        if self.state_id and self.env.company.state_id and self.state_id != self.env.company.state_id:
            fp = self.env['account.fiscal.position'].search([('name', '=', 'Inter State')])
            if fp:
                self.property_account_position_id = fp.id

    @api.onchange('name')
    def _onchange_name(self):
        if self and self.name and not re.match("^[a-zA-Z0-9 ]*$", self.name):
            self.name = ''
            raise ValidationError(_('Please Enter Valid Name.'))

    def fetch_city_data(self):
        file_path = odoo.modules.module.get_resource_path('mechpower_base_extended', 'static', 'worldcities.csv')
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                state_id = self.env['res.country.state'].search(
                    [('country_id.code', '=', row.get('iso2')), ('name', '=', row.get('admin_name'))], limit=1)
                if not state_id:
                    state = unidecode(row.get('admin_name'))
                    state_id = self.env['res.country.state'].search(
                        [('country_id.code', '=', row.get('iso2')), ('name', '=', state)], limit=1)
                if state_id:
                    self.env['res.city'].create({
                        'name': row.get('city_ascii') if row.get('city_ascii') else row.get('city') or '',
                        'state_id': state_id.id,
                        'country_id': state_id.country_id.id
                    })
    @api.model
    def create(self, vals):
        res = super().create(vals)
        res.onchange_name()
        if res.mobile and not res.phone:
            res.phone = res.mobile
        if res.city_id:
            res.city = res.city_id.name
        return res

    def write(self, vals):
        if 'mobile' in vals and (not 'phone' in vals and not self.phone):
            vals['phone'] = vals.get('mobile')
        elif not 'mobile' in vals and 'phone' in vals and self.mobile:
            if not vals['phone']:
                vals['phone'] = self.mobile
        if vals.get('city_id'):
            city_id = self.env['res.city'].browse(int(vals.get('city_id')))
            vals['city'] = city_id.name
        if vals.get('property_payment_term_id'):
            so_ids = self.env['sale.order'].search([('partner_id', 'in', self.ids), ('state', '=', 'draft')])
            so_ids.write({'payment_term_id': vals.get('property_payment_term_id')})
        res = super().write(vals)
        return res

    def compute_product_count(self):
        for rec in self:
            all_child = self.with_context(active_test=False).search([('id', 'child_of', rec.ids)])
            domain = [("partner_id", "in", all_child.ids), ('state', 'in', ['sale', 'done'])]
            sale_order_ids = self.env['sale.order'].search(domain)
            if sale_order_ids:
                product_ids = self.env['sale.order.line'].search(
                    [('order_id', 'in', sale_order_ids.ids), ('is_delivery', '=', False),
                     ('is_downpayment', '=', False), ('display_type', '=', False)]).mapped('product_id')
                rec.product_count = len(set(product_ids.ids))
            else:
                rec.product_count = 0

    def open_customer_product_list(self):
        tree_view_id = self.env.ref('mechpower_base_extended.customer_products_list').id
        form_view_id = self.env.ref('product.product_normal_form_view').id
        product_list = []
        all_child = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
        so_domain = [("partner_id", "in", all_child.ids), ('state', 'in', ['sale', 'done'])]
        sale_order_ids = self.env['sale.order'].search(so_domain)
        if sale_order_ids:
            product_ids = self.env['sale.order.line'].search(
                [('order_id', 'in', sale_order_ids.ids), ('is_delivery', '=', False), ('is_downpayment', '=', False),
                 ('display_type', '=', False)]).mapped('product_id')
            product_list = list(set(product_ids.ids))
        domain = [('id', 'in', product_list)]
        action = {
            'type': 'ir.actions.act_window',
            'views': [(tree_view_id, 'tree'), (form_view_id, 'form')],
            'view_mode': 'tree,form',
            'name': _('Products'),
            'res_model': 'product.product',
            'domain': domain,
        }
        return action

    @api.onchange('name', 'company_name')
    def onchange_name(self):
        if self.name:
            self.name = self.name.title()

        if self.company_name:
            self.company_name = self.company_name.title()

    def cron_add_to_mailing_list(self):
        # self.add_to_mail_list_from_partner()
        self.add_to_mail_list_lead()
        self.add_to_mail_list_incomplete_users()

    def add_to_mail_list_from_partner(self):
        date_from = datetime.now().strftime('%Y-%m-%d 00:00:00'),
        date_to = datetime.now().strftime('%Y-%m-%d 23:59:59'),
        contact_obj = self.env["mailing.contact"]
        # partners = self.env["res.users"].search([('create_date', '>=', date_from),
        #                                            ('create_date', '<', date_to),
        #                                            ('state', '=', 'active'),
        #                                            ('partner_share', '=', True)]).mapped('partner_id')

        so_partners = self.env["sale.order"].search([('create_date', '>=', date_from),('create_date', '<', date_to)]).mapped('partner_id')
        if so_partners:
            partners = self.env["res.users"].search([('partner_share', '=', True),('partner_id','in',so_partners.ids), ('state', '=', 'active')]).mapped('partner_id')
            if partners:
                mail_list_id = self.env.ref('mechpower_base_extended.customer_mailing_list').id
                for partner in partners:
                    if partner.email:
                        mailing_contact_id = contact_obj.search([('email', '=', partner.email)], limit=1)
                        if mailing_contact_id and mail_list_id not in mailing_contact_id.list_ids.ids:
                            mailing_contact_id.list_ids = [(4, mail_list_id)]
                        elif not mailing_contact_id:
                            contact_vals = {
                                "name": partner.name,
                                "email": partner.email,
                                "list_ids": [(4, mail_list_id)],
                                "company_name": partner.company_id.name or False,
                                "country_id": partner.country_id.id or False,
                                "opt_out": True if not partner.opt_out else False
                            }
                            mailing_contact_id = contact_obj.create(contact_vals)
                        self.env.cr.commit()
                        if mailing_contact_id:
                            subscription_line_id = mailing_contact_id.subscription_list_ids.filtered(lambda x: x.list_id and x.list_id.id == mail_list_id)
                            if subscription_line_id:
                                subscription_line_id.opt_out = True if not partner.opt_out else False

    def add_to_mail_list_lead(self):
        date_from = datetime.now().strftime('%Y-%m-%d 00:00:00'),
        date_to = datetime.now().strftime('%Y-%m-%d 23:59:59'),
        contact_obj = self.env["mailing.contact"]
        lead_ids = self.env["crm.lead"].search([('create_date', '>=', date_from), ('create_date', '<', date_to)])
        mail_list_id = self.env.ref('mechpower_base_extended.lead_mailing_list').id
        for lead in lead_ids:
            if lead.partner_id:
                partner = lead.partner_id
                if partner.email and not self.env['res.users'].search([('email', '=', partner.email)]):
                    mailing_contact_id = contact_obj.search([('email', '=', partner.email)], limit=1)
                    if mailing_contact_id and mail_list_id not in mailing_contact_id.list_ids.ids:
                        mailing_contact_id.list_ids = [(4, mail_list_id)]
                    elif not mailing_contact_id:
                        contact_vals = {
                            "name": partner.name,
                            "email": partner.email,
                            "list_ids": [(4, mail_list_id)],
                            "company_name": partner.company_id.name or False,
                            "country_id": partner.country_id.id or False,
                            "opt_out": True if not partner.opt_out else False
                        }
                        contact_obj.create(contact_vals)
            elif lead.email_from and not self.env['res.users'].search([('email', '=', lead.email_from)]):
                mailing_contact_id = contact_obj.search([('email', '=', lead.email_from)], limit=1)
                if mailing_contact_id and mail_list_id not in mailing_contact_id.list_ids.ids:
                    mailing_contact_id.list_ids = [(4, mail_list_id)]
                elif not mailing_contact_id:
                    name = ''
                    if lead.contact_name:
                        name = lead.contact_name
                    elif lead.partner_name:
                        name = lead.partner_name
                    contact_vals = {
                        "name": name,
                        "email": lead.email_from,
                        "list_ids": [(4, mail_list_id)],
                        "country_id": lead.country_id.id or False,
                    }
                    contact_obj.create(contact_vals)

    def set_tag(self):
        mailing_list_ids = [
            self.env.ref('mechpower_base_extended.product_and_service_mailing_list').id,
            self.env.ref('mechpower_base_extended.design_best_practices_mailing_list').id,
            self.env.ref('mechpower_base_extended.industry_insights_mailing_list').id,
            self.env.ref('mechpower_base_extended.events_mailing_list').id,
            self.env.ref('mechpower_base_extended.never_connected_customer_mailing_list').id,
            self.env.ref('mechpower_base_extended.customer_mailing_list').id,
            self.env.ref('mechpower_base_extended.lead_mailing_list').id
        ]
        for contact in self.env["mailing.contact"].search([]):
            contact.list_ids = [(3, ml)for ml in mailing_list_ids]

        remove_mail_list_ids = [
            self.env.ref('mechpower_base_extended.never_connected_customer_mailing_list').id,
            self.env.ref('mechpower_base_extended.lead_mailing_list').id
            ]
        add_mailing_list_ids = [
            self.env.ref('mechpower_base_extended.product_and_service_mailing_list').id,
            self.env.ref('mechpower_base_extended.design_best_practices_mailing_list').id,
            self.env.ref('mechpower_base_extended.industry_insights_mailing_list').id,
            self.env.ref('mechpower_base_extended.events_mailing_list').id,
            self.env.ref('mechpower_base_extended.customer_mailing_list').id
        ]
        lead_ids = self.env["crm.lead"].search([])
        connected_partner_ids = self.env["res.users"].search([('groups_id', 'in', self.env.ref('base.group_portal').ids), ('state', '=', 'active')])
        not_connected_partner_ids = self.env["res.users"].search([('groups_id', 'in', self.env.ref('base.group_portal').ids), ('state', '=', 'new')])
        for partner in connected_partner_ids:
            if partner.email:
                contact_obj = self.env["mailing.contact"]
                mailing_contact_id = contact_obj.search([('email', '=', partner.email)], limit=1)
                if mailing_contact_id:
                    mailing_contact_id.list_ids = [(4, ml)for ml in add_mailing_list_ids]
                else:
                    contact_vals = {
                        "name": partner.name,
                        "email": partner.email,
                        "list_ids": [(4, ml)for ml in add_mailing_list_ids],
                        "company_name": partner.company_id.name or False,
                        "country_id": partner.country_id.id or False,
                    }
                    mailing_contact_id = self.env["mailing.contact"].create(contact_vals)
        for partner in not_connected_partner_ids:
            if partner.email:
                contact_obj = self.env["mailing.contact"]
                mailing_contact_id = contact_obj.search([('email', '=', partner.email)], limit=1)
                if mailing_contact_id:
                    mailing_contact_id.list_ids = [4, self.env.ref('mechpower_base_extended.never_connected_customer_mailing_list').id]
                else:
                    contact_vals = {
                        "name": partner.name,
                        "email": partner.email,
                        "list_ids": [4, self.env.ref('mechpower_base_extended.never_connected_customer_mailing_list').id],
                        "company_name": partner.company_id.name or False,
                        "country_id": partner.country_id.id or False,
                    }
                    mailing_contact_id = self.env["mailing.contact"].create(contact_vals)
        for lead in lead_ids:
            if lead.partner_id:
                partner = lead.partner_id
                if partner.email and not self.env['res.users'].search([('email', '=', partner.email)]):
                    mailing_contact_id = contact_obj.search([('email', '=', partner.email)], limit=1)
                    if mailing_contact_id:
                        mailing_contact_id.list_ids = [(4,  self.env.ref('mechpower_base_extended.lead_mailing_list').id)]
                    elif not mailing_contact_id:
                        contact_vals = {
                            "name": partner.name,
                            "email": partner.email,
                            "list_ids": [(4,  self.env.ref('mechpower_base_extended.lead_mailing_list').id)],
                            "company_name": partner.company_id.name or False,
                            "country_id": partner.country_id.id or False,
                        }
                        contact_obj.create(contact_vals)
            elif lead.email_from and not self.env['res.users'].search([('email', '=', lead.email_from)]):
                mailing_contact_id = contact_obj.search([('email', '=', lead.email_from)], limit=1)
                if mailing_contact_id:
                    mailing_contact_id.list_ids = [(4,  self.env.ref('mechpower_base_extended.lead_mailing_list').id)]
                elif not mailing_contact_id:
                    name = ''
                    if lead.contact_name:
                        name = lead.contact_name
                    elif lead.partner_name:
                        name = lead.partner_name
                    contact_vals = {
                        "name": name,
                        "email": lead.email_from,
                        "list_ids": [(4,  self.env.ref('mechpower_base_extended.lead_mailing_list').id)],
                        "country_id": lead.country_id.id or False,
                    }
                    contact_obj.create(contact_vals)
        # so_partners = self.env["sale.order"].search([('partner_id.partner_share', '=', True), ('state', '=', 'active')]).mapped('partner_id')
        # for u in list(set(so_partners)):
        #     if u.email:
        #         contact_obj = self.env["mailing.contact"]
        #         mailing_contact_id = contact_obj.search([('email', '=', u.email)], limit=1)
        #         if mailing_contact_id:
        #             for mailing in mailing_list_ids:
        #                 mailing_contact_id.list_ids = [(4, mailing)]


    def add_to_mail_list_incomplete_users(self):
        date_from = datetime.now().strftime('%Y-%m-%d 00:00:00'),
        date_to = datetime.now().strftime('%Y-%m-%d 23:59:59'),
        contact_obj = self.env["mailing.contact"]
        partners = self.env["res.users"].search([('create_date', '>=', date_from),
                                                   ('create_date', '<', date_to),
                                                    ('state', '=', 'new'),
                                                   ('partner_share', '=', True),]).mapped('partner_id')
        mail_list_id = self.env.ref('mechpower_base_extended.never_connected_customer_mailing_list').id
        for partner in partners:
            if partner.email:
                mailing_contact_id = contact_obj.search([('email', '=', partner.email)], limit=1)
                if mailing_contact_id and mail_list_id not in mailing_contact_id.list_ids.ids:
                    mailing_contact_id.list_ids = [(4, mail_list_id)]
                elif not mailing_contact_id:
                    contact_vals = {
                        "name": partner.name,
                        "email": partner.email,
                        "list_ids": [(4, mail_list_id)],
                        "company_name": partner.company_id.name or False,
                        "country_id": partner.country_id.id or False,
                        "opt_out": True if not partner.opt_out else False
                    }
                    mailing_contact_id = contact_obj.create(contact_vals)
                self.env.cr.commit()
                if mailing_contact_id:
                    subscription_line_id = mailing_contact_id.subscription_list_ids.filtered(lambda x: x.list_id and x.list_id.id == mail_list_id)
                    if subscription_line_id:
                        subscription_line_id.opt_out = True if not partner.opt_out else False


class ResCompany(models.Model):
    _inherit = 'res.company'

    po_email = fields.Char(string='PO Email')
    po_phone = fields.Char(string='PO Mobile')
    bill_signature = fields.Binary('Bill Signature')

    linkedin_logo = fields.Binary('Linkedin')
    facebook_logo = fields.Binary('Facebook')
    instagram_logo = fields.Binary('Instagram')


class InheritResUsers(models.Model):
    _inherit = "res.users"
    
    show_model_ids = fields.Many2many('ir.model', 'res_users_model_rel', 'uid', 'mid', string='Select Model to View Archive and Delete')

    @api.model
    def get_is_hide_archive_and_applied_models(self,model=None):

        current_user = self.env.user
        if current_user and model and len(current_user.show_model_ids) > 0:
            for show_model in current_user.show_model_ids:
                if model == show_model.model:
                    return {
                        "show_archive_delete_option": True,
                        "archive_available": True if self.env[show_model.model]._fields.get('active') else False
                    }
        return {
            "show_archive_delete_option": False,
            "archive_available": False
        }

    def signup(self, values, token=None):
        if token:
            # signup with a token: find the corresponding partner id
            partner = self.env['res.partner']._signup_retrieve_partner(token, check_validity=True, raise_exception=True)
            # invalidate signup token
            partner.write({'signup_token': False, 'signup_type': False, 'signup_expiration': False})

            partner_user = partner.user_ids and partner.user_ids[0] or False

            # avoid overwriting existing (presumably correct) values with geolocation data
            if partner.country_id or partner.zip or partner.city:
                values.pop('city', None)
                values.pop('country_id', None)
            if partner.lang:
                values.pop('lang', None)

            if partner_user:
                # user exists, modify it according to values
                values.pop('login', None)
                values.pop('name', None)
                partner_user.write(values)
                if not partner_user.login_date:
                    partner_user._notify_inviter()
                return (partner_user.login, values.get('password'))
            else:
                # user does not exist: sign up invited user
                values.update({
                    'name': partner.name,
                    'partner_id': partner.id,
                    'email': values.get('email') or values.get('login'),
                })
                if partner.company_id:
                    values['company_id'] = partner.company_id.id
                    values['company_ids'] = [(6, 0, [partner.company_id.id])]
                partner_user = self._signup_create_user(values)
                partner_user._notify_inviter()

        return (values.get('login'), values.get('password'))
