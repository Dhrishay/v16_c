# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Candidroot Solutions Pvt. Ltd.
import io
import logging
import os
import tempfile
from base64 import b64decode
from io import BytesIO
import base64
from logging import getLogger

import numpy as np
from PIL import Image, UnidentifiedImageError
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

    @api.model
    def _run_wkhtmltopdf(self, bodies, report_ref=False, header=None, footer=None,
                         landscape=False, specific_paperformat_args=None,
                         set_viewport_size=False):
        print("\n\n\n_run_wkhtmltopdf-----------------------------------------------------")
        result = super(Report, self)._run_wkhtmltopdf(
            bodies, report_ref=report_ref, header=header, footer=footer, landscape=landscape,
            specific_paperformat_args=specific_paperformat_args,
            set_viewport_size=set_viewport_size)

        # image = Image.open(file_open('dns_custom_report/static/img/bg.jpg', mode='rb'))
        image_data = self.env.company.background_image
        # print("image_path----------------------------",image_data)
        if image_data:
            print("*******************************")
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
                    temp_file.write(image_data)
                    print("temp_file-----------------------------")
                    temp_file_path = temp_file.name
                    print(f"Image saved to temporary file: {temp_file_path}")

                image = Image.open(temp_file_path)
                print("Image successfully loaded from temporary file.")
            except Exception as e:
                print(f"Error while handling the image: {e}")

        else:
            print("No background image found.")

        # Convert the image to binary data
        # image_binary = io.BytesIO()
        # image.save(image_binary, format="JPEG")
        aaaaaaaaaaaaaaaa

        # Get the binary data as bytes
        binary_data = image_binary.getvalue()
        if isinstance(report_ref, str):
            xml_report_id = self.env.ref('dns_custom_report.action_report_dns_quotation')
            xml_report_id2 = self.env.ref('dns_custom_report.action_report_dns_invoice')
            report_obj = self.sudo().search(
                [('report_name', '=', report_ref), '|', ('id', '=', xml_report_id.id), ('id', '=', xml_report_id2.id)], limit=1)

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

    # @api.model
    # def _run_wkhtmltopdf(self, bodies, report_ref=False, header=None, footer=None,
    #                      landscape=False, specific_paperformat_args=None,
    #                      set_viewport_size=False):
    #     result = super(Report, self)._run_wkhtmltopdf(
    #         bodies, report_ref=report_ref, header=header, footer=footer, landscape=landscape,
    #         specific_paperformat_args=specific_paperformat_args,
    #         set_viewport_size=set_viewport_size)
    #
    #     # Fetch the background image from the company
    #     company = self.env.user.company_id
    #     background_image = company.background_image  # Assuming 'background_image' field is present
    #
    #     if not background_image:
    #         logger.error("Background image is empty or missing for the company.")
    #         return result
    #
    #     # Log the first 100 bytes of the image for debugging purposes
    #     logger.info(f"Background image data (first 100 bytes): {background_image[:100]}")
    #
    #     try:
    #         # Open the image using PIL
    #         image_binary = BytesIO(background_image)
    #
    #         # Reset pointer to the start to ensure image is read properly
    #         image_binary.seek(0)
    #
    #         # Try to open and validate the image format using PIL
    #         image = Image.open(image_binary)
    #
    #         # Verify that the image is valid
    #         image.verify()  # Verify the image is not corrupted
    #
    #         # After verification, we reset the pointer and read the actual image
    #         image_binary.seek(0)
    #         image = Image.open(image_binary)
    #
    #         # Log success in reading the image
    #         logger.info("Background image successfully opened with PIL.")
    #
    #         # Optionally, you could also save the image to ensure it's correct
    #         # image.save('/path/to/verify_image.jpg')  # Save the image for inspection if needed
    #
    #         # Encode the image to base64
    #         image_data = base64.b64encode(image_binary.read()).decode('utf-8')
    #
    #         # Create a data URL for embedding in HTML
    #         background_data = f"data:image/jpeg;base64,{image_data}"
    #
    #         # Log the image size to verify it is loaded correctly
    #         logger.info(f"Background image successfully loaded with size: {len(background_image)} bytes")
    #
    #         # Add the background image URL to the body of the report
    #         bodies = bodies.replace('<body>',
    #                                 f'<body style="background-image: url({background_data}); background-size: cover;">')
    #
    #     except UnidentifiedImageError:
    #         logger.error("The provided background image is invalid or cannot be identified.")
    #         return result
    #     except Exception as e:
    #         logger.exception("An error occurred while processing the background image.")
    #         return result
    #
    #     # Handle watermark or background (if applicable)
    #     if isinstance(report_ref, str):
    #         xml_report_id = self.env.ref('dns_custom_report.action_report_dns_quotation')
    #         xml_report_id2 = self.env.ref('dns_custom_report.action_report_dns_invoice')
    #         report_obj = self.sudo().search(
    #             [('report_name', '=', report_ref), '|', ('id', '=', xml_report_id.id), ('id', '=', xml_report_id2.id)],
    #             limit=1)
    #     else:
    #         report_obj = self.sudo().search([('id', '=', report_ref.id)], limit=1)
    #
    #     if isinstance(report_ref, str):
    #         if not report_obj:
    #             action_id = self.env.ref(report_ref).id
    #             report_obj = self.sudo().search([('id', '=', action_id)], limit=1)
    #
    #     docids = self.env.context.get('res_ids', False)
    #     watermark = None
    #
    #     # Set watermark if defined in the report template (optional part)
    #     if report_obj and background_image:
    #         watermark = background_image  # Use background as watermark if applicable
    #
    #     elif docids and report_obj:
    #         watermark = tools.safe_eval(
    #             report_obj.pdf_watermark_expression or 'None',
    #             dict(env=self.env, docs=self.env[report_obj.model].browse(docids)),
    #         )
    #         if watermark:
    #             watermark = base64.b64decode(watermark)
    #
    #     if not watermark:
    #         return result
    #
    #     # Create a PDF from the result and apply watermark (background image)
    #     pdf = PdfFileWriter()
    #     pdf_watermark = None
    #
    #     try:
    #         pdf_watermark = PdfFileReader(BytesIO(watermark))
    #     except PdfReadError:
    #         # Convert watermark image if needed
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
    #         logger.error('No usable watermark found')
    #         return result
    #
    #     if pdf_watermark.numPages < 1:
    #         logger.error('Your watermark PDF does not contain any pages')
    #         return result
    #     if pdf_watermark.numPages > 1:
    #         logger.debug('Your watermark PDF contains more than one page, '
    #                      'all but the first one will be ignored')
    #
    #     for page in PdfFileReader(BytesIO(result)).pages:
    #         watermark_page = pdf.addBlankPage(
    #             page.mediaBox.getWidth(), page.mediaBox.getHeight()
    #         )
    #         watermark_page.mergePage(pdf_watermark.getPage(0))
    #         watermark_page.mergePage(page)
    #
    #     # Final PDF content after applying watermark
    #     pdf_content = BytesIO()
    #     pdf.write(pdf_content)
    #
    #     pdf_content = pdf_content.getvalue()
    #
    #     if report_obj and report_obj.report_type == 'qweb-image':
    #         # Handle image conversion if report is of type 'qweb-image'
    #         pdf_report_fd, pdf_report_path = tempfile.mkstemp(suffix='.pdf', prefix='report.tmp.')
    #         os.close(pdf_report_fd)
    #         with open(pdf_report_path, 'wb') as body_file:
    #             body_file.write(pdf_content)
    #
    #         # Convert PDF to images (optional step for image handling)
    #         images = convert_from_path(pdf_report_path)
    #         image_path_list = []
    #         for i, image in enumerate(images):
    #             image_path = f"{pdf_report_path}_page_{i + 1}.jpg"
    #             image.save(image_path, "JPEG")
    #             image_path_list.append(image_path)
    #
    #         imgs = [Image.open(i) for i in image_path_list]
    #         # Resize images to match each other (optional)
    #         min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
    #         imgs_comb = np.hstack([i.resize(min_shape) for i in imgs])
    #
    #         # Save combined image
    #         imgs_comb = Image.fromarray(imgs_comb)
    #         imgs_comb.save(f"{pdf_report_path}_page_final_demo.jpg")
    #
    #         # Save final stacked image
    #         imgs_comb = np.vstack([i.resize(min_shape) for i in imgs])
    #         imgs_comb = Image.fromarray(imgs_comb)
    #         imgs_comb.save(f"{pdf_report_path}_page_final.jpg")
    #
    #         # Read final image back into pdf content
    #         with open(f"{pdf_report_path}_page_final.jpg", 'rb') as pdf_document:
    #             pdf_content = pdf_document.read()
    #
    #     return pdf_content