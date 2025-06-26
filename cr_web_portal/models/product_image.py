# -*- coding: utf-8 -*-

import base64

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError

from odoo.addons.web_editor.tools import get_video_embed_code, get_video_thumbnail


class ProductImage(models.Model):
    _inherit = 'product.image'

    glb_image = fields.Binary()
    image_1920_filename = fields.Char()
    glb_image_filename = fields.Char()