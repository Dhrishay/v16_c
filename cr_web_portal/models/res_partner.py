# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    industry_main_category = fields.Many2one('main.category', string="Industry Main Category", tracking=True)
    industry_sub_category = fields.Many2one('sub.category', string="Industry Sub Category", tracking=True)
    # is_special_economic_zone = fields.Boolean(string="SEZ")
    sez_classification = fields.Selection([('with_gst_treatment','With Payment of GST'),('without_gst_treatment','Without Payment of GST.')])
    property_payment_term_id = fields.Many2one(tracking=True)
    lead_source = fields.Selection(
        [('search_engine', 'Search Engine'), ('social_media', 'Social Media'), ('referral', 'Referral'),
         ('advertisement', 'Advertisement'), ('events', 'Events'), ('other', 'Other')], string="Customer Source")
    opt_out = fields.Boolean('Opt In')
    company_type = fields.Selection(selection_add=[
        ('educational_institution', 'Educational Institution'), ('government_organisation', 'Government Organisation'),
    ])
    is_educational_institution = fields.Boolean()
    is_government_organisation = fields.Boolean()
    create_date = fields.Datetime('Registration Date')
    registration_source = fields.Selection([('online', 'Online'), ('offline', 'Offline')], string='Registration Source')
    nda_file = fields.Binary('NDA')
    nda_filename = fields.Char('NDA')
    nda_last_update_date = fields.Datetime()
    mou_file = fields.Binary('MoU')
    mou_filename = fields.Char('MoU')
    mou_last_update_date = fields.Datetime()
    gst_certificate_file = fields.Binary('GST Certificate')
    gst_certificate_filename = fields.Char('GST Certificate')
    gst_last_update_date = fields.Datetime()

    @api.onchange('nda_file', 'mou_file', 'gst_certificate_file')
    def _onchange_files(self):
        msg = ''
        raise_warning = False
        if self.nda_filename and '.pdf' not in self.nda_filename.lower():
            raise_warning = True
            msg = 'PDF'
            self.write({'nda_file': False, 'nda_filename': False})
        elif self.mou_filename and '.pdf' not in self.mou_filename.lower() and '.jpeg' not in self.mou_filename.lower():
            raise_warning = True
            msg = 'PDF or JPEG'
            self.write({'mou_file': False, 'mou_filename': False})
        elif self.gst_certificate_filename and '.pdf' not in self.gst_certificate_filename.lower():
            raise_warning = True
            msg = 'PDF'
            self.write({'gst_certificate_file': False, 'gst_certificate_filename': False})
        if raise_warning:
            return {
                "warning": {"title": "File Mismatch Warning", "message": f"Only {msg} file type allowed."}
            }


    @api.constrains('email')
    def _check_email(self):
        for partner in self:
            if partner.email:
                existing_partner = self.search([('email', '=', partner.email), ('id', '!=', partner.id)])
                if existing_partner:
                    raise ValidationError("The email address '%s' is already used by another contact." % partner.email)

    @api.depends('is_company', 'is_educational_institution', 'is_government_organisation')
    def _compute_company_type(self):
        for partner in self:
            if partner.is_company:
                partner.company_type = 'company'
            elif partner.is_educational_institution:
                partner.company_type = 'educational_institution'
            elif partner.is_government_organisation:
                partner.company_type = 'government_organisation'
            else:
                partner.company_type = 'person'

    def _write_company_type(self):
        for partner in self:
            if partner.company_type == 'company':
                partner.is_company = True
                partner.is_educational_institution = False
                partner.is_government_organisation = False
            elif partner.company_type == 'educational_institution':
                partner.is_company = False
                partner.is_educational_institution = True
                partner.is_government_organisation = False
            elif partner.company_type == 'government_organisation':
                partner.is_company = False
                partner.is_educational_institution = False
                partner.is_government_organisation = True
            else:
                partner.is_company = False
                partner.is_educational_institution = False
                partner.is_government_organisation = False

    def onchange_company_type(self):
        for partner in self:
            if partner.is_educational_institution:
                partner.company_type = 'educational_institution'
            elif partner.is_government_organisation:
                partner.company_type = 'government_organisation'
            elif partner.is_company:
                partner.company_type = 'company'
            else:
                partner.company_type = 'person'

    @api.model
    def create(self, vals):

        if not vals.get('registration_source'):
            vals['registration_source'] = 'offline'
        if vals.get('nda_file'):
            vals['nda_last_update_date'] = fields.Datetime.now()
        if vals.get('mou_file'):
            vals['mou_last_update_date'] = fields.Datetime.now()
        if vals.get('gst_certificate_file'):
            vals['gst_last_update_date'] = fields.Datetime.now()
        res = super().create(vals)
        payment_term_id = self.env.ref('cr_web_portal.mech_advance_payment_term')
        res.property_payment_term_id = payment_term_id.id
        if res.email:
            # same_email_partner_ids = self.env['res.partner'].sudo().search(
            #     [('email', '=', res.email), ('id', '!=', res.id)])
            # if len(same_email_partner_ids) > 0:
            #     raise ValidationError(_("%s email is already exist.", res.email))
            if not res.parent_id and len(
                    res.user_ids) == 0 and not self.env.user._is_public() and res.customer_rank > 0:
                portal_wizard = self.env['portal.wizard'].with_context(active_ids=[res.id]).create({})
                portal_user = portal_wizard.user_ids
                portal_user.email = res.email
                portal_user.action_grant_access()
        return res

    def write(self, vals):
        if vals.get('nda_file'):
            vals['nda_last_update_date'] = fields.Datetime.now()
        if vals.get('mou_file'):
            vals['mou_last_update_date'] = fields.Datetime.now()
        if vals.get('gst_certificate_file'):
            vals['gst_last_update_date'] = fields.Datetime.now()
        res = super().write(vals)
        if 'l10n_in_gst_treatment' in vals and vals.get('l10n_in_gst_treatment') and 'update_sale_order' in self.env.context and self.env.context.get('update_sale_order'):
            so_id = int(self.env.context.get('update_sale_order'))
            so = self.env['sale.order'].browse(so_id)
            so.l10n_in_gst_treatment = vals.get('l10n_in_gst_treatment')
        return res


class PaymentTerm(models.Model):
    _inherit = 'account.payment.term'

    is_advance_payment = fields.Boolean('Advance Payment')


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model
    def create(self, vals):
        res = super().create(vals)
        res.groups_id = [(3, self.env.ref('base.group_allow_export').id)]
        return res