# -*- coding: utf-8 -*-
import logging

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.http import Controller, request, route

class SignatureIcons(models.Model):
    _name = 'signature.icons'
    _description = 'Social Media Signature Icons'

    def _compute_icon_url(self):
        for rec in self:
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            if rec.img_file_name and base_url:
                rec.icon_url = base_url + '/newsletter/'+rec.img_file_name
            else:
                rec.icon_url = ''

    name = fields.Char(string='Name')
    icon_url = fields.Char(string='Icon Url',compute="_compute_icon_url")
    signature_image = fields.Binary(string='Image icon')
    img_file_name = fields.Char(string="Img File Name")