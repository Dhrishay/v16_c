# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _


class SaleCloseReason(models.Model):
    _name = "sale.close.reason"
    _description = 'Sale Close Reason'

    name = fields.Char('Reason', tracking=True)
