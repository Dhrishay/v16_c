# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Candidroot Solutions Pvt. Ltd.
import io
import logging
import os
import tempfile
from base64 import b64decode
from io import BytesIO
from logging import getLogger
import requests

import numpy as np
from PIL import Image
from odoo.tools.misc import file_open
from odoo.tools.misc import find_in_path
from pdf2image import convert_from_path

logger = logging.getLogger(__name__)

from odoo import api, models, fields, tools

logger = getLogger(__name__)

try:
    from PyPDF2 import PdfFileWriter, PdfFileReader  # pylint: disable=W0404
    from PyPDF2.utils import PdfReadError  # pylint: disable=W0404
except ImportError:
    logger.debug('Can not import PyPDF2')


def _get_wkhtmltopdf_bin():
    return find_in_path('wkhtmltopdf')


class Report(models.Model):
    _inherit = 'ir.actions.report'

    pdf_watermark = fields.Binary('Watermark')
    pdf_watermark_expression = fields.Char(
        'Watermark expression', help='An expression yielding the base64 '
                                     'encoded data to be used as watermark. \n'
                                     'You have access to variables `env` and `docs`')

    def _render_qweb_pdf(self, report_ref, res_ids=None, data=None):
        if not self.env.context.get('res_ids'):
            return super(
                Report, self.with_context(res_ids=res_ids)
            )._render_qweb_pdf(report_ref, res_ids=res_ids, data=data)
        return super(Report, self).render_qweb_pdf(report_ref, res_ids=res_ids, data=data)

    # @api.model
    # def _run_wkhtmltopdf(self, bodies, report_ref=False, header=None, footer=None,
    #                      landscape=False, specific_paperformat_args=None,
    #                      set_viewport_size=False):
    #     print("\n\n\n_run_wkhtmltopdf----------------------------------------------------------")
    #     result = super(Report, self)._run_wkhtmltopdf(
    #         bodies, report_ref=report_ref, header=header, footer=footer, landscape=landscape,
    #         specific_paperformat_args=specific_paperformat_args,
    #         set_viewport_size=set_viewport_size)
    #
    #     image = Image.open(file_open('dns_custom_report/static/img/bg.jpg', mode='rb'))
    #     # Convert the image to binary data
    #     image_binary = io.BytesIO()
    #     image.save(image_binary, format="JPEG")
    #
    #     # Get the binary data as bytes
    #     binary_data = image_binary.getvalue()
    #     if isinstance(report_ref, str):
    #         xml_report_id = self.env.ref('dns_custom_report.action_report_dns_quotation')
    #         xml_report_id2 = self.env.ref('dns_custom_report.action_report_dns_invoice')
    #         report_obj = self.sudo().search(
    #             [('report_name', '=', report_ref), '|', ('id', '=', xml_report_id.id), ('id', '=', xml_report_id2.id)], limit=1)
    #
    #     else:
    #         report_obj = self.sudo().search([('id', '=', report_ref.id)], limit=1)
    #     if isinstance(report_ref, str):
    #         if not report_obj:
    #             action_id = self.env.ref(report_ref).id
    #             report_obj = self.sudo().search([('id', '=', action_id)], limit=1)
    #
    #     docids = self.env.context.get('res_ids', False)
    #     watermark = None
    #
    #     if report_obj and binary_data:
    #         watermark = binary_data
    #
    #     elif docids and report_obj:
    #         watermark = tools.safe_eval(
    #             report_obj.pdf_watermark_expression or 'None',
    #             dict(env=self.env, docs=self.env[report_obj.model].browse(docids)),
    #         )
    #         if watermark:
    #             watermark = b64decode(watermark)
    #
    #     if not watermark:
    #         return result
    #
    #     pdf = PdfFileWriter()
    #     pdf_watermark = None
    #     try:
    #         pdf_watermark = PdfFileReader(BytesIO(watermark))
    #     except PdfReadError:
    #         # let's see if we can convert this with pillow
    #         try:
    #             Image.init()
    #             image = Image.open(BytesIO(watermark))
    #             pdf_buffer = BytesIO()
    #             if image.mode != 'RGB':
    #                 image = image.convert('RGB')
    #             resolution = image.info.get(
    #                 'dpi', report_obj.paperformat_id.dpi or 90
    #             )
    #             if isinstance(resolution, tuple):
    #                 resolution = resolution[0]
    #             image.save(pdf_buffer, 'pdf', resolution=resolution)
    #             pdf_watermark = PdfFileReader(pdf_buffer)
    #         except:
    #             logger.exception('Failed to load watermark')
    #
    #     if not pdf_watermark:
    #         logger.error(
    #             'No usable watermark found, got %s...', watermark[:100]
    #         )
    #         return result
    #
    #     if pdf_watermark.numPages < 1:
    #         logger.error('Your watermark pdf does not contain any pages')
    #         return result
    #     if pdf_watermark.numPages > 1:
    #         logger.debug('Your watermark pdf contains more than one page, '
    #                      'all but the first one will be ignored')
    #
    #     for page in PdfFileReader(BytesIO(result)).pages:
    #         watermark_page = pdf.addBlankPage(
    #             page.mediaBox.getWidth(), page.mediaBox.getHeight()
    #         )
    #         watermark_page.mergePage(pdf_watermark.getPage(0))
    #         watermark_page.mergePage(page)
    #
    #     pdf_content = BytesIO()
    #     pdf.write(pdf_content)
    #
    #     files_command_args = []
    #     temporary_files = []
    #
    #     pdf_content = pdf_content.getvalue()
    #     if report_obj and report_obj.report_type == 'qweb-image':
    #         pdf_report_fd, pdf_report_path = tempfile.mkstemp(suffix='.pdf', prefix='report.tmp.')
    #         os.close(pdf_report_fd)
    #         with open(pdf_report_path, 'wb') as body_file:
    #             body_file.write(pdf_content)
    #
    #         images = convert_from_path(pdf_report_path)
    #         image_path_list = []
    #         for i, image in enumerate(images):
    #             image_path = f"{pdf_report_path}_page_{i + 1}.jpg"
    #             image.save(image_path, "JPEG")
    #             image_path_list.append(image_path)
    #             # with open(image_path, 'rb') as pdf_document:
    #             #     pdf_content += pdf_document.read()
    #
    #         imgs = [Image.open(i) for i in image_path_list]
    #         # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    #         min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
    #         imgs_comb = np.hstack([i.resize(min_shape) for i in imgs])
    #
    #         # save that beautiful picture
    #         imgs_comb = Image.fromarray(imgs_comb)
    #         imgs_comb.save(f"{pdf_report_path}_page_final_demo.jpg")
    #
    #         # for a vertical stacking it is simple: use vstack
    #         imgs_comb = np.vstack([i.resize(min_shape) for i in imgs])
    #         imgs_comb = Image.fromarray(imgs_comb)
    #         imgs_comb.save(f"{pdf_report_path}_page_final.jpg")
    #
    #         with open(f"{pdf_report_path}_page_final.jpg", 'rb') as pdf_document:
    #             pdf_content = pdf_document.read()
    #     return pdf_content

    @api.model
    def _run_wkhtmltopdf(self, bodies, report_ref=False, header=None, footer=None,
                         landscape=False, specific_paperformat_args=None,
                         set_viewport_size=False):
        print("\n\n\n_run_wkhtmltopdf----------------------------------------------------------")
        result = super(Report, self)._run_wkhtmltopdf(
            bodies, report_ref=report_ref, header=header, footer=footer, landscape=landscape,
            specific_paperformat_args=specific_paperformat_args,
            set_viewport_size=set_viewport_size)

        company = self.env.user.company_id
        print("company-----------id------------------",company.id)
        url = self.env.company.get_base_url()
        print("url------------------------------------------",url)
        print("company.background_image------------------------------------------",type(company.background_image))
        if company.background_image:
            image_url = f'{url}/web/image/res.company/{company.id}/background_image'
            print("image_url-----------------------------------------",image_url)
        else:
            image_url = '/web/static/img/placeholder.png'

        try:
            # Fetch the image from the URL
            print("\nFetching image from URL...")
            response = requests.get(image_url)
            response.raise_for_status()  # Check for HTTP errors
            image = Image.open(BytesIO(response.content))
        except requests.exceptions.RequestException as e:
            print("\nError fetching the image: {e}")
            return result

        try:
            # Fetch the image from the URL
            print("\nFetching image from URL...")
            response = requests.get(image_url)
            response.raise_for_status()  # Check for HTTP errors

            # Open the image
            image = Image.open(BytesIO(response.content))

            # Get the image format from the PIL Image object
            image_format = image.format.lower()
            print(f"Image format detected: {image_format}")

            # Prepare the image in binary format
            image_binary = io.BytesIO()
            # Save in the same format detected
            image.save(image_binary, format=image_format.upper())
            image_binary.seek(0)

        except requests.exceptions.RequestException as e:
            print(f"\nError fetching the image: {e}")
            image_binary = None  # In case of an error, we set the binary image to None

        # Get the binary data as bytes
        binary_data = image_binary.getvalue()
        if isinstance(report_ref, str):
            xml_report_id = self.env.ref('dns_custom_report.action_report_dns_quotation')
            xml_report_id2 = self.env.ref('dns_custom_report.action_report_dns_invoice')
            report_obj = self.sudo().search([('report_name', '=', report_ref), '|', ('id', '=', xml_report_id.id), ('id', '=', xml_report_id2.id)],limit=1)

        else:
            report_obj = self.sudo().search([('id', '=', report_ref.id)], limit=1)
        if isinstance(report_ref, str):
            if not report_obj:
                action_id = self.env.ref(report_ref).id
                report_obj = self.sudo().search([('id', '=', action_id)], limit=1)

        docids = self.env.context.get('res_ids', False)
        watermark = None

        if report_obj and binary_data:
            watermark = binary_data

        elif docids and report_obj:
            watermark = tools.safe_eval(
                report_obj.pdf_watermark_expression or 'None',
                dict(env=self.env, docs=self.env[report_obj.model].browse(docids)),
            )
            if watermark:
                watermark = b64decode(watermark)

        if not watermark:
            return result

        pdf = PdfFileWriter()
        pdf_watermark = None
        try:
            pdf_watermark = PdfFileReader(BytesIO(watermark))
        except PdfReadError:
            # let's see if we can convert this with pillow
            try:
                Image.init()
                image = Image.open(BytesIO(watermark))
                pdf_buffer = BytesIO()
                if image.mode != 'RGB':
                    image = image.convert('RGB')
                resolution = image.info.get(
                    'dpi', report_obj.paperformat_id.dpi or 90
                )
                if isinstance(resolution, tuple):
                    resolution = resolution[0]
                image.save(pdf_buffer, 'pdf', resolution=resolution)
                pdf_watermark = PdfFileReader(pdf_buffer)
            except:
                logger.exception('Failed to load watermark')

        if not pdf_watermark:
            logger.error(
                'No usable watermark found, got %s...', watermark[:100]
            )
            return result

        if pdf_watermark.numPages < 1:
            logger.error('Your watermark pdf does not contain any pages')
            return result
        if pdf_watermark.numPages > 1:
            logger.debug('Your watermark pdf contains more than one page, '
                         'all but the first one will be ignored')

        for page in PdfFileReader(BytesIO(result)).pages:
            watermark_page = pdf.addBlankPage(
                page.mediaBox.getWidth(), page.mediaBox.getHeight()
            )
            watermark_page.mergePage(pdf_watermark.getPage(0))
            watermark_page.mergePage(page)

        pdf_content = BytesIO()
        pdf.write(pdf_content)

        files_command_args = []
        temporary_files = []

        pdf_content = pdf_content.getvalue()
        if report_obj and report_obj.report_type == 'qweb-image':
            pdf_report_fd, pdf_report_path = tempfile.mkstemp(suffix='.pdf', prefix='report.tmp.')
            os.close(pdf_report_fd)
            with open(pdf_report_path, 'wb') as body_file:
                body_file.write(pdf_content)

            images = convert_from_path(pdf_report_path)
            image_path_list = []
            for i, image in enumerate(images):
                image_path = f"{pdf_report_path}_page_{i + 1}.jpg"
                image.save(image_path, "JPEG")
                image_path_list.append(image_path)
                # with open(image_path, 'rb') as pdf_document:
                #     pdf_content += pdf_document.read()

            imgs = [Image.open(i) for i in image_path_list]
            # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
            min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
            imgs_comb = np.hstack([i.resize(min_shape) for i in imgs])

            # save that beautiful picture
            imgs_comb = Image.fromarray(imgs_comb)
            imgs_comb.save(f"{pdf_report_path}_page_final_demo.jpg")

            # for a vertical stacking it is simple: use vstack
            imgs_comb = np.vstack([i.resize(min_shape) for i in imgs])
            imgs_comb = Image.fromarray(imgs_comb)
            imgs_comb.save(f"{pdf_report_path}_page_final.jpg")

            with open(f"{pdf_report_path}_page_final.jpg", 'rb') as pdf_document:
                pdf_content = pdf_document.read()
        return pdf_content

