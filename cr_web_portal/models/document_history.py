# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class DocumentHistory(models.Model):
    _name = 'document.history'

    name = fields.Char('Name')
    document_id = fields.Many2one('ir.attachment', 'Document')
    product_id = fields.Many2one('product.product', 'Product Variant')
    product_template_id = fields.Many2one('product.template', 'Product')
    document = fields.Binary('Document')
    user_id = fields.Many2one('res.users', 'User')
    file_type = fields.Char('File')

    def delete_history(self):
        self.unlink()

    def replace_document(self):
        if self.file_type == 'fcstd_file':
            attachment = self.env['ir.attachment'].search(
                [('res_id', '=', self.product_id.id), ('res_field', '=', 'fcstd_file'),
                 ('res_model', '=', 'product.product')])
            attachment.write({'datas': self.document})
            attachment.write({'name': self.name})
            self.product_id.fcstd_file_name = self.name

        if self.file_type == 'product_step_file':
            attachment = self.env['ir.attachment'].search([('res_id', '=', self.product_id.id), ('res_field', '=', 'product_step_file'),('res_model', '=', 'product.product')])
            attachment.write({'datas': self.document})
            attachment.write({'name': self.name})
            self.product_id.fcstd_file_name = self.name

        if self.file_type == 'drawing_fcstd_file':
            attachment = self.env['ir.attachment'].search(
                [('res_id', '=', self.product_id.id), ('res_field', '=', 'drawing_fcstd_file'),
                 ('res_model', '=', 'product.product')])
            attachment.write({'datas': self.document})
            attachment.write({'name': self.name})
            self.product_id.fcstd_file_name = self.name

        if self.file_type == 'pdf_file':
            attachment = self.env['ir.attachment'].search(
        [('res_id', '=', self.product_id.id), ('res_field', '=', 'pdf_file'),
         ('res_model', '=', 'product.product')])
            attachment.write({'datas': self.document})
            attachment.write({'name': self.name})
            self.product_id.fcstd_file_name = self.name


        if self.file_type == 'doc_file':
            attachment = self.env['ir.attachment'].search(
                [('res_id', '=', self.product_id.id), ('res_field', '=', 'doc_file'),
                 ('res_model', '=', 'product.product')])
            attachment.write({'datas': self.document})
            attachment.write({'name': self.name})
            self.product_id.doc_file_name = self.name


        if self.file_type == 'stl_file':
            attachment = self.env['ir.attachment'].search(
                [('res_id', '=', self.product_id.id), ('res_field', '=', 'stl_file'),
                 ('res_model', '=', 'product.product')])
            attachment.write({'datas': self.document})
            attachment.write({'name': self.name})
            self.product_id.stl_file_name = self.name

        if self.file_type == 'x_studio_customer_drawing_file':
            attachment = self.env['ir.attachment'].search(
                [('res_id', '=', self.product_id.id), ('res_field', '=', 'x_studio_customer_drawing_file'),
                 ('res_model', '=', 'product.product')])
            attachment.write({'datas': self.document})
            attachment.write({'name': self.name})
            self.product_id.fcstd_file_name = self.name


        if self.file_type == 'x_studio_exception_file':
            attachment = self.env['ir.attachment'].search(
                [('res_id', '=', self.product_id.id), ('res_field', '=', 'x_studio_exception_file'),
                 ('res_model', '=', 'product.product')])
            attachment.write({'datas': self.document})
            attachment.write({'name': self.name})
            self.product_id.exception_file_name = self.name


        if self.file_type == 'x_studio_exception_reply_file':
            attachment = self.env['ir.attachment'].search(
                [('res_id', '=', self.product_id.id), ('res_field', '=', 'x_studio_exception_reply_file'),
                 ('res_model', '=', 'product.product')])
            attachment.write({'datas': self.document})
            attachment.write({'name': self.name})
            self.product_id.exception_reply_file_name = self.name
