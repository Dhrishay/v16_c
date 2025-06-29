# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, tools


class MultiSmtpServer(models.Model):
    _inherit = 'ir.mail_server'

    model_ids = fields.Many2many('ir.model')


class MailMail(models.Model):
    _inherit = "mail.mail"

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if res.model:
            mail_server_id = self.env['ir.mail_server'].search([('model_ids.model', '=', res.model)], limit=1)
            if mail_server_id:
                res.mail_server_id = mail_server_id.id
        return res
