# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _, api
from odoo.exceptions import UserError


class Task(models.Model):
    _inherit = 'project.task'

    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'High'),
    ], index=True, string="Priority", tracking=True, default=False)
    project_partner_ids = fields.Many2many('res.partner', compute='compute_message_follower_ids')


    @api.model
    def message_subscribe(self, partner_ids=None, subtype_ids=None):
        """
        Override message_subscribe to prevent adding followers who don't have project access.
        """
        if partner_ids:
            for partner in self.env['res.partner'].browse(partner_ids):
                if partner and partner.id not in self.project_id.message_partner_ids.ids:
                    raise UserError(_("User %s does not have access to this project and cannot be added as a follower.") % partner.name)
        return super().message_subscribe(partner_ids=partner_ids, subtype_ids=subtype_ids)

    @api.depends('project_id', 'project_id.message_follower_ids')
    def compute_message_follower_ids(self):
        for rec in self:
            if rec.project_id:
                rec.project_partner_ids = [(6, 0, rec.project_id.message_follower_ids.mapped('partner_id').ids)]
            else:
                rec.project_partner_ids = False
