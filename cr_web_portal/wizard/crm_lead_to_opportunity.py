# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class Lead2OpportunityPartner(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'

    partner_company_type = fields.Selection([('person', 'Individual'),('company','Company'),('educational_institution', 'Educational Institution'), ('government_organisation', 'Government Organisation')],default='company',string="Contact Company Type")
    partner_industry_main_category = fields.Many2one('main.category', string="Industry Main Category")
    partner_industry_sub_category = fields.Many2one('sub.category', string="Industry Sub Category")
    partner_lead_source = fields.Selection(
        [('search_engine', 'Search Engine'), ('social_media', 'Social Media'), ('referral', 'Referral'),
         ('advertisement', 'Advertisement'), ('events', 'Events'), ('other', 'Other')], string="Customer Source")
    email = fields.Char()
    user_action = fields.Selection([('create', 'Create a new customer'),('exist', 'Link to an existing customer')], string='Customer',default="exist",store=True)

    @api.onchange('user_action')
    def _onchange_user_action(self):
        if self.user_action:
            self.action = self.user_action

    @api.model
    def default_get(self, fields):
        result = super(Lead2OpportunityPartner, self).default_get(fields)
        if result.get('lead_id'):
            lead_id = self.env['crm.lead'].sudo().search([('id','=',int(result.get('lead_id')))])
            result['partner_industry_main_category'] = lead_id.industry_category_id.id if lead_id.industry_category_id else False
            result['partner_industry_sub_category'] = lead_id.industry_sub_category_id.id if lead_id.industry_sub_category_id else False
            result['email'] = lead_id.email_from if lead_id.email_from else ''
        return result

    def _convert_handle_partner(self, lead, action, partner_id):
        if action == 'create' and lead.partner_name:
            lead.with_context(default_user_id=self.user_id.id)._handle_partner_assignment(
                force_partner_id=partner_id,
                force_partner_company_type= self.partner_company_type,
                force_partner_industry_main_category= self.partner_industry_main_category.id if self.partner_industry_main_category else False,
                force_partner_industry_sub_category= self.partner_industry_sub_category.id if self.partner_industry_sub_category else False,
                force_partner_lead_source= self.partner_lead_source if self.partner_lead_source else False,
                email= self.email,
                create_missing=(action == 'create')
            )
        else:
            lead.with_context(default_user_id=self.user_id.id)._handle_partner_assignment(
                force_partner_id=partner_id,
                force_partner_industry_main_category=self.partner_industry_main_category.id if self.partner_industry_main_category else False,
                force_partner_industry_sub_category=self.partner_industry_sub_category.id if self.partner_industry_sub_category else False,
                force_partner_lead_source=self.partner_lead_source if self.partner_lead_source else False,
                email=self.email,
                create_missing=(action == 'create')
            )