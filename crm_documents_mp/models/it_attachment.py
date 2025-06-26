# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    @api.model_create_multi
    def create(self, vals_list):
        new_vals_list = []
        if self.env.context.get('crm_doc_mp', False) and type(vals_list) == list:
            for vals in vals_list:
                if not vals.get('type', False):
                    vals['type'] = 'binary'
                new_vals_list.append(vals)
        else:
            new_vals_list = vals_list
        res = super(IrAttachment, self).create(new_vals_list)
        return res