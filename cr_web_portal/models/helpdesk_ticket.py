# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.tools import html2plaintext

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    description_searchable = fields.Text(string="Description Searchable", compute="_compute_description_searchable", store=True)

    @api.depends('description')
    def _compute_description_searchable(self):
        for rec in self:
            rec.description_searchable = html2plaintext(rec.description or "")