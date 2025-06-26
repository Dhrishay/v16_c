# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Candidroot Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.
import base64
import io
from odoo import http
from odoo.http import request


class DownloadAttachment(http.Controller):

    @http.route(['/attachment/download/<int:order_id>/<string:file_name>/<string:field>'], type='http', auth='public')
    def download_attachment(self, order_id, file_name, field):
        sale_order = request.env['sale.order'].sudo().browse([order_id])
        if field == 'technical_drawing_file':
            attachments = request.env['ir.attachment'].sudo().search([('res_id', '=', int(order_id)),('res_field', '=', 'technical_drawing_file_name')])
            for attachment in attachments:
                attachment.unlink()
            attachment = request.env['ir.attachment'].sudo().create({
                'name': sale_order.technical_drawing_file_name,
                'res_model': 'sale.order',
                'res_id': order_id,
                'res_field': 'technical_drawing_file_name',
                'datas': sale_order.technical_drawing_file,
            })
            data = io.BytesIO(base64.standard_b64decode(attachment["datas"]))
            return http.send_file(data, filename=attachment['name'], as_attachment=True)

        if field == 'uv_printing_file':
            attachments = request.env['ir.attachment'].sudo().search([('res_id', '=', int(order_id)),('res_field', '=', 'uv_printing_file_name')])
            for attachment in attachments:
                attachment.unlink()
            attachment = request.env['ir.attachment'].sudo().create({
                'name': sale_order.uv_printing_file_name,
                'res_model': 'sale.order',
                'res_id': order_id,
                'res_field': 'uv_printing_file_name',
                'datas': sale_order.uv_printing_file,
            })
            data = io.BytesIO(base64.standard_b64decode(attachment["datas"]))
            return http.send_file(data, filename=attachment['name'], as_attachment=True)
        else:
            return True
