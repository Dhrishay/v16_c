import base64
import os
from odoo import models, fields, api, tools

class Dashboard(models.Model):
    _name = 'dashboard.record'
    _description = 'Dashboard Record'

    name = fields.Char(string='Name', required=True)
    image_url = fields.Char(string='Image')
    url = fields.Char(string='Image URL')
    description = fields.Text(string='Description')
    category_ids = fields.Many2many('dashboard.category', string='Categories')

    icon_image = fields.Binary(string='Icon', compute='_compute_icon_image', store=True , readonly=False)

    @api.depends('image_url')
    def _compute_icon_image(self):
        for record in self:
            record.icon_image = False
            if record.image_url:
                path = os.path.join(record.image_url.lstrip("/"))
                if path:
                    try:
                        with tools.file_open(path, 'rb',
                                             filter_ext=('.png', '.svg', '.gif', '.jpeg', '.jpg')) as image_file:
                            record.icon_image = base64.b64encode(image_file.read())
                    except FileNotFoundError:
                        record.icon_image = False
class DashboardCategory(models.Model):
    _name = 'dashboard.category'
    _description = 'Dashboard Category'

    name = fields.Char(string='Category', required=True)
