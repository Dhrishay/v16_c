# -*- coding: utf-8 -*-
from odoo import models, fields
class Company(models.Model):
    _inherit = 'res.company'

    gst_number = fields.Char()
    cin = fields.Char()
    pan = fields.Char()

