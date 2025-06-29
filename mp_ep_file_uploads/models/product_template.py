# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _


class Product(models.Model):
    _inherit = "product.template"

    product_original_step_file = fields.Binary(help='Only .step file type allowed.')
    product_original_step_file_name = fields.Char()
    fcstd_file = fields.Binary(help='Only .fcstd file type allowed.')
    fcstd_file_name = fields.Char()
    product_step_file = fields.Binary(help='Only .step file type allowed.')
    product_step_file_name = fields.Char()
    drawing_fcstd_file = fields.Binary(help='Only .fcstd file type allowed.')
    drawing_fcstd_file_name = fields.Char()
    pdf_file = fields.Binary(help='Only .pdf file type allowed.')
    pdf_file_name = fields.Char()
    image_file = fields.Binary(help='Only .jpg/.jpeg/.png file type allowed.')
    image_file_name = fields.Char()
    dxf_file = fields.Binary(help='Only .dxf file type allowed.')
    dxf_file_name = fields.Char()
    doc_file = fields.Binary(help='Only .doc file type allowed.')
    doc_file_name = fields.Char()
    outsource_pdf_file = fields.Binary(help='Only .pdf file type allowed.')
    outsource_pdf_file_name = fields.Char()
    tap_file = fields.Binary(help='Only .tap file type allowed.')
    tap_file_name = fields.Char()
    stl_file = fields.Binary(help='Only .stl file type allowed.')
    stl_file_name = fields.Char()
    product_original_step_file_url = fields.Char(compute='_compute_product_original_step_file_url')

    @api.onchange("product_original_step_file",'fcstd_file','product_step_file','drawing_fcstd_file','pdf_file','image_file','dxf_file','doc_file','outsource_pdf_file','tap_file','stl_file')
    def _onchange_files(self):
        allowed_type = self._context.get('allowed_type', False)
        raise_warning = 0
        if allowed_type == '.step' and self.product_original_step_file_name and allowed_type not in self.product_original_step_file_name:
            self.write({'product_original_step_file': False, 'product_original_step_file_name': False})
            raise_warning = 1
        elif allowed_type == '.fcstd' and self.fcstd_file_name and allowed_type not in self.fcstd_file_name:
            self.write({'fcstd_file': False, 'fcstd_file_name': False})
            raise_warning = 1
        elif allowed_type == '.product_step' and self.product_step_file_name and '.step' not in self.product_step_file_name:
            self.write({'product_step_file': False, 'product_step_file_name': False})
            raise_warning = 1
        elif allowed_type == '.drawing_fcstd' and self.drawing_fcstd_file_name and '.fcstd' not in self.drawing_fcstd_file_name:
            self.write({'drawing_fcstd_file': False, 'drawing_fcstd_file_name': False})
            raise_warning = 1
        elif allowed_type == '.pdf' and self.pdf_file_name and allowed_type not in self.pdf_file_name:
            self.write({'pdf_file': False, 'pdf_file_name': False})
            raise_warning = 1
        elif allowed_type == '.image' and self.image_file_name and not self.image_file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            self.write({'image_file': False, 'image_file_name': False})
            raise_warning = 1
        elif allowed_type == '.dxf' and self.dxf_file_name and allowed_type not in self.dxf_file_name:
            self.write({'dxf_file': False, 'dxf_file_name': False})
            raise_warning = 1
        elif allowed_type == '.doc' and self.doc_file_name and allowed_type not in self.doc_file_name:
            self.write({'doc_file': False, 'doc_file_name': False})
            raise_warning = 1
        elif allowed_type == '.outsource_pdf' and self.outsource_pdf_file_name and '.pdf' not in self.outsource_pdf_file_name:
            self.write({'outsource_pdf_file': False, 'outsource_pdf_file_name': False})
            raise_warning = 1
        elif allowed_type == '.tap' and self.tap_file_name and allowed_type not in self.tap_file_name:
            self.write({'tap_file': False, 'tap_file_name': False})
            raise_warning = 1
        elif allowed_type == '.stl' and self.stl_file_name and allowed_type not in self.stl_file_name:
            self.write({'stl_file': False, 'stl_file_name': False})
            raise_warning = 1

        if raise_warning:
            return {
                "warning": {"title": "File Mismatch Warning", "message": "Only %s file type allowed."%(allowed_type)}
            }

    def _compute_product_original_step_file_url(self):
        if self.product_original_step_file:
            attachment = self.sudo().message_main_attachment_id.search([('res_id', '=', self.id),('res_model', '=', self._name),('res_field', '=', 'product_original_step_file')])
            if attachment:
                cad_url = attachment.get_cad_url()
                self.product_original_step_file_url = cad_url
            else:
                self.product_original_step_file_url = ''
        else:
            self.product_original_step_file_url = ''