# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _


class Product(models.Model):
    _inherit = "product.product"

    fcstd_file = fields.Binary(help='Only .fcstd file type allowed.', string='Prepared Data')
    fcstd_file_name = fields.Char()
    product_step_file = fields.Binary(help='Only .step file type allowed.', string='Step File')
    product_step_file_name = fields.Char()
    drawing_fcstd_file = fields.Binary(help='Only .fcstd file type allowed.', string='PCB Outline')
    drawing_fcstd_file_name = fields.Char()
    pdf_file = fields.Binary(help='Only .pdf file type allowed.', string='Data Sheet')
    pdf_file_name = fields.Char()
    doc_file = fields.Binary(help='Only .doc file type allowed.', string='DFM Checklist')
    doc_file_name = fields.Char()
    stl_file = fields.Binary(help='Only .stl file type allowed.', string='Production Data')
    stl_file_name = fields.Char()
    exception_file_name = fields.Char()
    exception_reply_file_name = fields.Char()
    is_service = fields.Boolean("is service", compute='_check_compute_service')
    additional_notes = fields.Text("Additional Notes")
    technical_drawing_file = fields.Binary('Technical Drawing', store=True)
    technical_drawing_file_name = fields.Char("Technical Drawing")
    uv_printing_file = fields.Binary('Uv Printing File', store=True)
    uv_printing_file_name = fields.Char("Uv Printing File")

    @api.onchange('fcstd_file', 'product_step_file', 'drawing_fcstd_file', 'pdf_file', 'doc_file', 'stl_file',
                  'x_studio_exception_file', 'x_studio_exception_reply_file','technical_drawing_file','uv_printing_file')
    def _onchange_files(self):
        allowed_type = self._context.get('allowed_type', False)
        msg = ''
        if allowed_type:
            allowed_type.lower()
        raise_warning = 0

        if allowed_type == '.zip' and self.fcstd_file_name and allowed_type not in self.fcstd_file_name.lower():
            self.write({'fcstd_file': False, 'fcstd_file_name': False})
            msg = '.zip'
            raise_warning = 1
        elif allowed_type == '.product_step' and self.product_step_file_name and (
                '.step' not in self.product_step_file_name.lower() and '.stp' not in self.product_step_file_name.lower()):
            self.write({'product_step_file': False, 'product_step_file_name': False})
            msg = '.step, .stp'
            raise_warning = 1
        elif allowed_type == '.drawing_fcstd' and self.drawing_fcstd_file_name and '.dxf' not in self.drawing_fcstd_file_name.lower():
            self.write({'drawing_fcstd_file': False, 'drawing_fcstd_file_name': False})
            msg = '.dxf'
            raise_warning = 1
        elif allowed_type == '.pdf' and self.pdf_file_name and allowed_type not in self.pdf_file_name.lower():
            self.write({'pdf_file': False, 'pdf_file_name': False})
            msg = '.pdf'
            raise_warning = 1
        elif allowed_type == '.doc_1' and self.doc_file_name and self.doc_file_name.split('.')[1].lower() not in ['xls',
                                                                                                                  'doc',
                                                                                                                  'docx']:
            self.write({'doc_file': False, 'doc_file_name': False})
            msg = ".xls, .doc, .docx"
            raise_warning = 1
        elif allowed_type == '.uv_printing_file' and self.uv_printing_file_name and self.uv_printing_file_name.split('.')[1].lower() not in ['png',
                                                                                                                  'jpeg',
                                                                                                                  'jpg','pdf','tiff']:
            self.write({'uv_printing_file': False, 'uv_printing_file_name': False})
            msg = ".png, .jpg, .jpeg,.tiff,.pdf"
            raise_warning = 1
        elif allowed_type == '.technical_drawing_file' and self.technical_drawing_file_name and self.technical_drawing_file_name.split('.')[1].lower() not in ['zip',
                                                                                                                  'stl','stp','pdf','dxf','dwg',
                                                                                                                  'step']:
            self.write({'technical_drawing_file': False, 'technical_drawing_file_name': False})
            msg = ".zip, .stl, .stp,.pdf,.zip,.dxf,.dwg,.step"
            raise_warning = 1
        # elif allowed_type == '.doc_2' and self.doc_file_name and self.doc_file_name.split('.')[1].lower() not in ['xls','.doc']:
        #     self.write({'doc_file': False, 'doc_file_name': False})
        #     raise_warning = 1
        elif allowed_type == '.stl' and self.stl_file_name and '.zip' not in self.stl_file_name.lower():
            self.write({'stl_file': False, 'stl_file_name': False})
            msg = '.zip'
            raise_warning = 1
        elif allowed_type == '.tech_query_1' and self.exception_file_name and self.exception_file_name.split('.')[
            1].lower() not in ['xls', 'doc', 'docx', 'pdf']:
            self.write({'x_studio_exception_file': False, 'exception_file_name': False})
            msg = ".xls, .doc, .docx, .pdf"
            raise_warning = 1
        # elif allowed_type == '.tech_query_2' and self.exception_file_name and self.exception_file_name.split('.')[1].lower() not in ['xls', '.doc']:
        #     self.write({'x_studio_exception_file': False, 'exception_file_name': False})
        #     raise_warning = 1
        elif allowed_type == '.tech_reply_1' and self.exception_reply_file_name and \
                self.exception_reply_file_name.split('.')[1].lower() not in ['xls', 'doc', 'docx', 'pdf']:
            self.write({'x_studio_exception_reply_file': False, 'exception_reply_file_name': False})
            msg = ".xls, .doc, .docx, .pdf"
            raise_warning = 1
        # elif allowed_type == '.tech_reply_2' and self.exception_reply_file_name and self.exception_reply_file_name.split('.')[1].lower() not in ['xls','.doc','.docx']:
        #     self.write({'x_studio_exception_reply_file': False, 'exception_reply_file_name': False})
        #     raise_warning = 1

        if raise_warning:
            return {
                "warning": {"title": "File Mismatch Warning", "message": "Only %s file type allowed." % (msg)}
            }

    # def _compute_product_original_step_file_url(self):
    #     if self.product_original_step_file:
    #         attachment = self.sudo().message_main_attachment_id.search([('res_id', '=', self.id),('res_model', '=', self._name),('res_field', '=', 'product_original_step_file')])
    #         if attachment:
    #             cad_url = attachment.get_cad_url()
    #             self.product_original_step_file_url = cad_url
    #         else:
    #             self.product_original_step_file_url = ''
    #     else:
    #         self.product_original_step_file_url = ''

    def _check_compute_service(self):
        for rec in self:
            if rec.default_code:
                if rec.default_code.startswith('CFGX') and not rec.is_customisable:
                    rec.is_service = True
                else:
                    rec.is_service = False
            else:
                rec.is_service = False