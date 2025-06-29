# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, tools
import uuid
from odoo.exceptions import UserError, ValidationError
import re


class Lead(models.Model):
    _inherit = 'crm.lead'

    phone = fields.Char()
    show_analysis_button = fields.Boolean(compute='compute_show_button')
    show_new_followup_button = fields.Boolean()
    show_won_lost_button = fields.Boolean()
    show_only_won_button = fields.Boolean()

    def compute_show_button(self):
        for rec in self:
            if rec.type != 'lead' and rec.active and rec.stage_id:
                if rec.stage_id.id == self.env.ref('crm.stage_lead1').id:
                    rec.show_analysis_button = True
                    rec.show_new_followup_button = False
                    rec.show_won_lost_button = False
                    rec.show_only_won_button = False
                elif rec.stage_id.id == self.env.ref('crm.stage_lead2').id:
                    rec.show_analysis_button = False
                    rec.show_new_followup_button = True
                    rec.show_won_lost_button = False
                    rec.show_only_won_button = False
                elif rec.stage_id.id == self.env.ref('crm.stage_lead3').id:
                    rec.show_analysis_button = False
                    rec.show_new_followup_button = False
                    rec.show_won_lost_button = True
                    rec.show_only_won_button = False
                else:
                    rec.show_analysis_button = False
                    rec.show_new_followup_button = False
                    rec.show_won_lost_button = False
                    rec.show_only_won_button = False
            elif not rec.active:
                rec.show_analysis_button = False
                rec.show_new_followup_button = False
                rec.show_won_lost_button = False
                rec.show_only_won_button = True
            else:
                rec.show_analysis_button = False
                rec.show_new_followup_button = False
                rec.show_won_lost_button = False
                rec.show_only_won_button = False

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if res.mobile and not res.phone:
            res.phone = res.mobile
        return res

    def write(self, vals):
        if 'mobile' in vals and (not 'phone' in vals and not self.phone):
            vals['phone'] = vals.get('mobile')
        elif not 'mobile' in vals and 'phone' in vals and self.mobile:
            if not vals['phone']:
                vals['phone'] = self.mobile
        res = super().write(vals)
        return res

    @api.onchange('partner_name')
    def _onchange_partner_name(self):
        if self and self.partner_name and not re.match("^[a-zA-Z0-9 ]*$", self.partner_name):
            self.partner_name = ''
            raise ValidationError(_('Please Enter Valid Name.'))

    @api.onchange('contact_name')
    def _onchange_name(self):
        if self and self.contact_name and not re.match("^[a-zA-Z0-9 ]*$", self.contact_name):
            self.contact_name = ''
            raise ValidationError(_('Please Enter Valid Name.'))

    def action_set_analysis(self):
        self.stage_id = self.env.ref('crm.stage_lead2').id

    def action_set_new(self):
        self.stage_id = self.env.ref('crm.stage_lead1').id

    def action_set_follow_up(self):
        self.stage_id = self.env.ref('crm.stage_lead3').id
