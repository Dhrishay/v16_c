# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _


class CustomerFiles(models.Model):
    _name = "customer.files"
    _description = 'Customer Files'

    name = fields.Char()
    file = fields.Binary()
    attachment_type_id = fields.Many2many('attachment.type', string='Attachment Types')
    attachment_note = fields.Char(string='Attachment Note')
    order_id = fields.Many2one('sale.order')


class AttachmentType(models.Model):
    _name = "attachment.type"
    _description = 'Attachment Type'

    name = fields.Char()