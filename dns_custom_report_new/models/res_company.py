from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    background_image = fields.Binary('Background Image', attachment=True, store=True)
    background_image_path = fields.Char('Background Image Path')

