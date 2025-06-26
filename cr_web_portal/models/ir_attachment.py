# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from datetime import datetime, timedelta
from collections import defaultdict

from odoo import api, fields, models, tools, _


class IrAttachmentSignatureIcons(models.Model):
    _inherit = 'ir.attachment'

    is_temp = fields.Boolean(default=False)

    def _cron_daily_clean_temp_attachment(self):
        temp_attachments = self.search([('is_temp','=',True)]).unlink()

    @api.model
    def create(self, vals):
        res = super(IrAttachmentSignatureIcons, self).create(vals)
        for rec in res:
            if rec.res_model == 'signature.icons' and rec.res_field == 'signature_image':
                rec.public = True
        return res

    def write(self, vals):
        res = super(IrAttachmentSignatureIcons, self).write(vals)
        for rec in self:
            if rec.res_model == 'signature.icons' and rec.res_field == 'signature_image':
                if rec.public == False:
                    rec.public = True
        return res