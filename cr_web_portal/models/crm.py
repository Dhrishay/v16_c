# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, tools
import uuid


class CrmTag(models.Model):
    _inherit = 'crm.tag'

    active = fields.Boolean(default=True)

class Lead(models.Model):
    _inherit = 'crm.lead'


    mobile = fields.Char('Mobile', compute='_compute_mobile', readonly=False, store=True,required=True)
    access_url = fields.Char('Portal Access URL',
                             compute='_compute_access_url',
                             help='Customer Portal URL')
    access_token = fields.Char('Security Token', copy=False)
    service = fields.Selection([
        ('enclosure_design', 'Enclosure Design'),
        ('fdm_modeling', '3D Printing (FDM)'),
        ('projection_printing', '3D Printing (Projection)'),
        ('sheet_metal_fabrication', 'Sheet Metal Fabrication'),
        ('cnc_machining', 'CNC Machining'),
        ('injection_molding', 'Injection Molding'),
        ('italtronic_enclosure', 'Italtronic'),
        ('customized_italtronics', 'Customized Italtronics')
    ])
    industry_category_id = fields.Many2one('main.category', string='Industry')
    industry_sub_category_id = fields.Many2one('sub.category', string='Category')
    product_category_ids = fields.Many2many('product.public.category', string='Product Category')
    is_enclosure_designing = fields.Boolean(string="Enclosure Designing")
    is_fdm_printing = fields.Boolean(string="FDM Printing (3D printing)")
    is_projection_printing = fields.Boolean(string="Projection Printing (3D printing)")
    is_sheet_metal_fabrication = fields.Boolean(string="Sheet metal fabrication")
    is_injection_moduling = fields.Boolean(string="Injection moulding")
    is_cnc_machining = fields.Boolean(string="CNC machining")
    customer_message = fields.Html(string="Customer Message")
    enquire_selection = fields.Selection(
        [('Individual', 'Individual'), ('Company', 'Company'),
         ('Educational_Institution', 'Educational Institution'),
         ('Government_Organisation', 'Government Organisation')], string='Inquire as')
    city_id = fields.Many2one(comodel_name='res.city', string='City')

    @api.onchange('stage_id')
    def _onchange_stage_id(self):
        if self._origin:
            self._cr.execute('Select stage_id from crm_lead where id = %s' % self._origin.id)
            old_state_id = self._cr.fetchall()
            if self.env.ref('cr_web_portal.lost_stage_id').id == self.stage_id.id:
                self.stage_id = old_state_id[0][0]

    @api.model
    def create(self, vals):
        res = super(Lead, self).create(vals)
        if res.create_uid.has_group('base.group_user'):
            res.source_id = self.env.ref('cr_web_portal.utm_source_by_mech_power').id
        else:
            res.source_id = self.env.ref('cr_web_portal.utm_source_by_customer').id
        if res and res.type == 'opportunity':
            if res.partner_id:
                partner_id = res.partner_id
                if self.env.user.has_group('base.group_user'):
                    user_id = self.env['res.users'].sudo().search([('partner_id', '=', partner_id.id)])
                    if not user_id:
                        portal_wizard = self.env['portal.wizard'].sudo().with_context(active_ids=[partner_id.id]).create({})
                        portal_user = portal_wizard.user_ids
                        portal_user.email = partner_id.email if partner_id.email else res.email_from
                        portal_user.action_grant_access()
        return res

    def send_service_email(self):
        mail_template = self.env.ref('cr_web_portal.mail_template_service_product_lead')
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        url = base_url + '/customer/questions/%s' % self.id
        # template_id.sudo().with_context(url=url).send_mail(self.id, force_send=True)
        lang = self.env.context.get('lang')
        if mail_template and mail_template.lang:
            lang = mail_template._render_lang(self.ids)[self.id]
        ctx = {
            'default_model': 'crm.lead',
            'default_res_id': self.id,
            'default_use_template': bool(mail_template),
            'default_template_id': mail_template.id if mail_template else None,
            # 'default_composition_mode': 'comment',
            'force_email': True,
            'url': url,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }

    def _compute_access_url(self):
        for inq in self:
            inq.access_url = '/my/inquiries/%s' % (inq.id)

    def _portal_ensure_token(self):
        if not self.access_token:
            self.sudo().write({'access_token': str(uuid.uuid4())})
        return self.access_token

    def get_portal_url(self, suffix=None, report_type=None, download=None, query_string=None, anchor=None):
        self.ensure_one()
        url = self.access_url + '%s?access_token=%s%s%s%s%s' % (
            suffix if suffix else '',
            self._portal_ensure_token(),
            '&report_type=%s' % report_type if report_type else '',
            '&download=true' if download else '',
            query_string if query_string else '',
            '#%s' % anchor if anchor else ''
        )
        return url

    def _prepare_customer_values(self, partner_name, partner_company_type=False, partner_industry_main_category=False,
                                 partner_industry_sub_category=False, partner_lead_source=False, is_company=False,
                                 parent_id=False, email=False):
        """ Extract data from lead to create a partner.

        :param name : furtur name of the partner
        :param is_company : True if the partner is a company
        :param parent_id : id of the parent partner (False if no parent)

        :return: dictionary of values to give at res_partner.create()
        """
        email_parts = [email]
        res = {
            'name': partner_name,
            'user_id': self.env.context.get('default_user_id') or self.user_id.id,
            'comment': self.description,
            'team_id': self.team_id.id,
            'parent_id': parent_id,
            'phone': self.phone,
            'mobile': self.mobile,
            'title': self.title.id,
            'function': self.function,
            'street': self.street,
            'street2': self.street2,
            'zip': self.zip,
            'city': self.city_id.name if self.city_id else '',
            'city_id': self.city_id.id if self.city_id else False,
            'country_id': self.country_id.id,
            'state_id': self.state_id.id,
            'website': self.website,
            'type': 'contact',
            'industry_main_category': partner_industry_main_category if partner_industry_main_category else False,
            'industry_sub_category': partner_industry_sub_category if partner_industry_sub_category else False,
            'lead_source': partner_lead_source if partner_lead_source else False,
        }
        if self.enquire_selection and self.enquire_selection == 'Company':
            res['is_company'] = True
        elif self.enquire_selection and self.enquire_selection == 'Educational_Institution':
            res['is_educational_institution'] = True
        elif self.enquire_selection and self.enquire_selection == 'Government_Organisation':
            res['is_government_organisation'] = True
        if self.lang_id.active:
            res['lang'] = self.lang_id.code
        if not parent_id and is_company:
            res['company_type'] = partner_company_type if partner_company_type else False
            res['email'] = email_parts[0] if email_parts else False
            res['customer_rank'] = 1
        else:
            if not self.env['res.partner'].sudo().search([('id','=',parent_id)]).email:
                res['email'] = email_parts[0] if email_parts else False
                res['customer_rank'] = 1
        return res

    def _handle_partner_assignment(self, force_partner_id=False, force_partner_company_type=False,
                                   force_partner_industry_main_category=False,
                                   force_partner_industry_sub_category=False, force_partner_lead_source=False,email=False,
                                   create_missing=True):
        for lead in self:
            if force_partner_id:
                lead.partner_id = force_partner_id
            if not lead.partner_id and create_missing:
                partner = lead._create_customer(force_partner_company_type=force_partner_company_type,
                                                force_partner_industry_main_category=force_partner_industry_main_category,
                                                force_partner_industry_sub_category=force_partner_industry_sub_category,
                                                force_partner_lead_source=force_partner_lead_source, email=email)
                if partner.parent_id:
                    lead.partner_id = partner.parent_id.id
                else:
                    lead.partner_id = partner.id

    def _create_customer(self, force_partner_company_type=False, force_partner_industry_main_category=False,
                         force_partner_industry_sub_category=False, force_partner_lead_source=False,email=False):
        Partner = self.env['res.partner']
        contact_name = self.contact_name
        if not contact_name:
            contact_name = Partner._parse_partner_name(self.email_from)[0] if self.email_from else False

        if self.partner_name:
            partner_company = Partner.create(
                self._prepare_customer_values(self.partner_name, partner_company_type=force_partner_company_type,
                                              partner_industry_main_category=force_partner_industry_main_category,
                                              partner_industry_sub_category=force_partner_industry_sub_category,
                                              partner_lead_source=force_partner_lead_source,
                                              email=email,
                                              is_company=True))
        elif self.partner_id:
            partner_company = self.partner_id
        else:
            partner_company = None

        if contact_name:
            return Partner.create(self._prepare_customer_values(contact_name, is_company=False,
                                                                partner_industry_main_category=force_partner_industry_main_category,
                                                                partner_industry_sub_category=force_partner_industry_sub_category,
                                                                partner_lead_source=force_partner_lead_source,
                                                                email=email,
                                                                parent_id=partner_company.id if partner_company else False))

        if partner_company:
            return partner_company
        return Partner.create(self._prepare_customer_values(self.name, is_company=False))

    @api.onchange('contact_name', 'partner_name')
    def onchange_partner_and_contact_name(self):
        if self.contact_name:
            self.contact_name = self.contact_name.title()

        if self.partner_name:
            self.partner_name = self.partner_name.title()