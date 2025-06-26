# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _


class Documents(models.Model):
    _inherit = "documents.document"

    crm_id = fields.Many2one('crm.lead')
    crm_doc_map_id = fields.Many2one('crm.doc.map')

    @api.model_create_multi
    def create(self, vals_list):
        new_vals_list = []
        if type(vals_list) == list:
            for vals in vals_list:
                if vals.get('crm_doc_map_id', False):
                    self = self.with_context(crm_doc_mp=True)
                    crm_map_id = self.env['crm.doc.map'].search([('id', '=', vals['crm_doc_map_id'])])
                    vals['folder_id'] = crm_map_id.folder_id.id
                    vals['type'] = 'binary'
                new_vals_list.append(vals)
        res = super(Documents, self).create(new_vals_list)
        return res