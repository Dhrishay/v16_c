# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import tools, _
import json
import base64
from odoo import http
from odoo.http import request
import functools
from odoo.modules import get_resource_path
import odoo
from odoo.http import request, Response
import io
try:
    from werkzeug.utils import send_file
except ImportError:
    from odoo.tools._vendor.send_file import send_file
from odoo.tools.mimetypes import guess_mimetype
import base64
from odoo.tools.image import image_data_uri
import json
from odoo.exceptions import UserError, ValidationError, AccessError

from markupsafe import escape
from psycopg2 import IntegrityError
from werkzeug.exceptions import BadRequest
from odoo import http, fields, tools
from odoo.addons.http_routing.models.ir_http import slug, unslug
from odoo.addons.website.controllers.main import QueryURL
from odoo.http import request
from odoo.tools import html2plaintext
from odoo.tools.misc import get_lang
from odoo.tools import sql
import requests
# from http import http.client
import logging
_logger = logging.getLogger(__name__)

class MechPowerWeb(http.Controller):

    @http.route(['/about-us'], type='http', auth="public", website=True)
    def about_us_page(self):
        return request.render('cr_web_portal.about_us_page')

    @http.route(['/instant-quote'], type='http', auth="public", website=True)
    def instant_quote(self):
        website = request.env['website'].get_current_website()
        service_cost_fdm = request.env['service.cost'].sudo().search([('id','=',request.env.ref('cr_web_portal.service_cost_fdm').sudo().id)])
        service_cost_projection = request.env['service.cost'].sudo().search([('id','=',request.env.ref('cr_web_portal.service_cost_projection').sudo().id)])
        service_cost_uv_printing = request.env['service.cost'].sudo().search([('id','=',request.env.ref('cr_web_portal.service_cost_uv_printing').sudo().id)])
        customer_lead_time = request.env['x_customer_lead_time'].sudo().search([])
        vals = {
            'fdm_material_ids' : service_cost_fdm.material_ids if service_cost_fdm and service_cost_fdm.material_ids else [],
            'fdm_print_quality_ids' : service_cost_fdm.print_quality_ids if service_cost_fdm and service_cost_fdm.print_quality_ids else [],
            'fdm_infill_ids' : service_cost_fdm.infill_ids if service_cost_fdm and service_cost_fdm.infill_ids else [],
            'projection_material_ids' : service_cost_projection.material_ids if service_cost_projection and service_cost_projection.material_ids else [],
            'projection_print_quality_ids' : service_cost_projection.print_quality_ids if service_cost_projection and service_cost_projection.print_quality_ids else [],
            'projection_infill_ids' : service_cost_projection.infill_ids if service_cost_projection and service_cost_projection.infill_ids else [],
            'uv_printing_side' : service_cost_uv_printing.no_of_sides_ids if service_cost_uv_printing and service_cost_uv_printing.no_of_sides_ids else [],
            'customer_lead_time' : customer_lead_time if customer_lead_time else [],
            'website' : website if website else False,
        }
        return request.render('cr_web_portal.instant_quote_page',vals)

    # @http.route(['/powervis'], type='http', auth="public", website=True, )
    # def powervis_page(self):
    #     return request.render('cr_web_portal.powervis_page')

    @http.route(['/enclosure'], type='http', auth="public", website=True)
    def enclosure_design_page(self):
        return request.render('cr_web_portal.enclosure_design_page')

    @http.route(['/enclosure-design'], type='http', auth="public", website=True)
    def new_enclosure_design_page(self):
        return request.render('cr_web_portal.new_enclosure_design_page')

    @http.route(['/3d-printing'], type='http', auth="public", website=True)
    def service_3d_printing_page(self):
        return request.render('cr_web_portal.service_3d_printing_page')

    @http.route(['/fused-deposition-modeling'], type='http', auth="public", website=True)
    def fused_deposition_modeling_page(self):
        return request.render('cr_web_portal.fused_deposition_modeling_page')

    @http.route(['/projection-printing-figure'], type='http', auth="public", website=True)
    def projection_printing_figure_page(self):
        return request.render('cr_web_portal.projection_printing_figure_page')

    @http.route(['/sheet-metal-fabrication'], type='http', auth="public", website=True)
    def sheet_metal_fabrication_page(self):
        return request.render('cr_web_portal.sheet_metal_fabrication')

    @http.route(['/cnc-machining'], type='http', auth="public", website=True)
    def service_cnc_machining(self):
        return request.render('cr_web_portal.cnc_machining')

    @http.route(['/injection-molding'], type='http', auth="public", website=True)
    def service_injection_molding(self):
        return request.render('cr_web_portal.injection_molding')

    @http.route(['/contactus'], type='http', auth="public", website=True, sitemap=False)
    def contactus__base_page(self):
        # return request.render('cr_web_portal.contact_us_page')
        return request.redirect('/contact-us')

    @http.route(['/contact-us'], type='http', auth="public", website=True, methods=['GET', 'POST'], csrf=False)
    def contact_us_page(self,**post):
        return request.render('cr_web_portal.contact_us_page')

    @http.route(['/contactus/thank-you'], type='http', auth="public", website=True, csrf=False)
    def contact_us_thank_you_page(self, **post):
        return request.render('cr_web_portal.thank_you_page_contact_us')


    @http.route(['/service/request/thank-you'], type='http', auth="public", website=True)
    def service_request_thank_you(self, **kw):
        redirect_path = request.session.get('redirect_path') if 'redirect_path' in request.session else False
        service_list = request.session.get('service_list') if 'service_list' in request.session else False
        if 'redirect_path' in request.session:
            request.session.pop('redirect_path')
        if 'service_list' in request.session:
            request.session.pop('service_list')
        if redirect_path and service_list:
            return request.render('cr_web_portal.thank_you_page',{'redirect_path': redirect_path, 'service_list': service_list})
        else:
            return request.redirect('/')

    @http.route(['/customer/questions/<int:lead_id>'], type='http', auth="public", website=True)
    def customer_questions(self, lead_id):
        lead_id = request.env['crm.lead'].sudo().search([('id', '=', lead_id)])
        product_ids = lead_id.lead_product_ids.filtered(
            lambda x: x.product_id and x.product_id.detailed_type == 'service').mapped('product_id')
        product_id = False
        service_id = False
        if product_ids:
            product_id = product_ids[0]
            service_id = request.env['services.services'].sudo().search(
                [('product_id', '=', product_id.product_tmpl_id.id)])
        question_ids = service_id.question_ids
        return request.render('cr_web_portal.customer_question_answer_form',
                              {'question_ids': question_ids, 'lead_id': lead_id})


    @http.route('/web/sign/up', type='http', auth='public', website=True, sitemap=False)
    def mech_signup(self, *args, **kw):
        res = requests.get('http://ip-api.com/json/%s'% request.httprequest.remote_addr)
        if request.env.user and not request.env.user._is_public():
            return request.redirect('/my')
        return request.render('cr_web_portal.mech_signup')

    @http.route(['/partner/signup/thankyou'], type='http', auth="public", website=True)
    def partner_signup(self, **kwargs):
        if request.session.get('error'):
            error = request.session.get('error')
            request.session.pop('error')
            return request.render('cr_web_portal.mech_signup',{'error':error})
        return request.render('cr_web_portal.mech_signup', {'success': _(
            "Thank you for registering with us! \n Please check your email inbox for a verification link to activate your account. \n If you don't receive the email within a few minutes, please check your spam folder. \n For any assistance, feel free to contact our team.")})

    @http.route(['/create/attachment/powerviz'], type='json', auth="public", website=True)
    def create_attachment_for_powerviz(self, **kw):
        base64Data = kw['base64Data'] if 'base64Data' in kw else False
        name = kw['name'] if 'name' in kw else False
        mimetype = kw['mimetype'] if 'mimetype' in kw else False
        if base64Data and name or mimetype:
            doc_id = request.env['ir.attachment'].sudo().create({
                'datas':  base64Data,
                'name': name,
                'mimetype': mimetype,
                'public': True,
                'is_temp' : True,
            })
            powervis_domain = request.env['ir.config_parameter'].sudo().get_param('cr_web_portal.powervis_url')
            base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
            if powervis_domain and base_url:
                powervis_url = powervis_domain + base_url + '/web/content/' + str(doc_id.id)
                return powervis_url
        return False


    @http.route(['/calculate/fdm/price'], type='json', auth="public", website=True)
    def calculate_fdm_price(self, **kw):

        powervis_domain = request.env['ir.config_parameter'].sudo().get_param('cr_web_portal.powervis_url')
        fdm_step_file_url = kw['fdm_step_file_url'] if 'fdm_step_file_url' in kw else False
        if fdm_step_file_url:
            fdm_step_file_url = fdm_step_file_url.replace(powervis_domain, '')

        fdm_material_id = kw['fdm_material'] if 'fdm_material' in kw else False
        fdm_quantity = float(kw['fdm_quantity']) if 'fdm_quantity' in kw else False
        fdm_print_quality_id = kw['fdm_print_quality'] if 'fdm_print_quality' in kw else False
        fdm_infill_id = kw['fdm_infill'] if 'fdm_infill' in kw else False
        uv_printing_side_id = kw['uv_printing_side'] if 'uv_printing_side' in kw else False
        dyn_lead_time = kw['lead_time'] if 'lead_time' in kw else False
        powerviz_volume = False
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        if fdm_step_file_url:
            endpoint = f"{base_url}/api/analyze"
            headers = {'Content-Type': 'application/json'}
            url = fdm_step_file_url.strip()

            # Payload (URL to be sent in the request)
            payload = json.dumps({'file_url': url})

            try:
                # Make the POST request
                response = requests.post(endpoint, headers=headers, data=payload)
                # Check for successful response
                if response.status_code == 200:
                    reponse_json = response.json().get('result')
                    _logger.info('==================result===============%s' % reponse_json)

                    if reponse_json.get('volume'):
                        powerviz_volume = float(reponse_json.get('volume'))
                    else:
                        _logger.exception("Failed to analyze STEP file.")
                        return {'error': 'Failed to analyze STEP file.'}
                else:
                    _logger.exception("Failed to analyze STEP file.")
                    return {'error': 'Failed to analyze STEP file.'}

            except requests.RequestException as e:
                _logger.exception("Connection error occurred: %s", e)
                return {'error': 'Connection error'}
        else:
            _logger.exception("Failed to Generate STEP file URL.")
            return {'error': 'Failed to Generate STEP file URL.'}
        if powerviz_volume and fdm_material_id and fdm_print_quality_id and fdm_infill_id:
            fdm_material_id = request.env['service.materials'].sudo().browse(fdm_material_id)
            fdm_print_quality_id = request.env['service.print.quality'].sudo().browse(fdm_print_quality_id)
            fdm_infill_id = request.env['service.infill'].sudo().browse(fdm_infill_id)
            uv_printing_side_price = False
            # conodition for user didn't select UV Priting option
            # if not uv_printing_side_id:
            material_gram = float(powerviz_volume) * fdm_material_id.density * fdm_material_id.factor_support
            material_cost_gram = material_gram * fdm_material_id.rate_per_gram
            rm_cost = material_cost_gram
            print_quality = fdm_print_quality_id.rate
            infill = fdm_infill_id.rate

            lead_time = round((24 + (material_gram * 0.24)) / 24)
            all_lead_times = request.env['x_customer_lead_time'].sudo().search([])
            filtered_lead_times = all_lead_times.filtered(
                lambda lt: lt.x_name in ['3', '5', '7'] and int(lt.x_name) >= lead_time)
            cost_wh_lt = material_cost_gram + (material_cost_gram * print_quality) + (material_cost_gram * infill)
            if uv_printing_side_id:
                uv_printing_side_id = request.env['service.number.of.sides'].sudo().browse(uv_printing_side_id)
                uv_printing_side_factor = uv_printing_side_id.factor
                cosu_uv = (uv_printing_side_id.factor/100) * cost_wh_lt
                final_cost_uv = max(cosu_uv, uv_printing_side_id.min_price)
                cost_wh_lt = material_cost_gram + (material_cost_gram * print_quality) + (material_cost_gram * infill) + final_cost_uv
            cost_wh_freight = False
            if filtered_lead_times and not dyn_lead_time:
                if int(filtered_lead_times[0].x_name) == 3:
                    cost_wh_freight = round(cost_wh_lt * 1.2)
                elif int(filtered_lead_times[0].x_name) == 5:
                    cost_wh_freight = round(cost_wh_lt * 1.1)
                elif int(filtered_lead_times[0].x_name) == 7:
                    cost_wh_freight = round(cost_wh_lt * 1)
                if '5' in filtered_lead_times.mapped('x_name'):
                    cost_wh_freight = round(cost_wh_lt * 1.1)
            if dyn_lead_time:
                lead_time_id = request.env['x_customer_lead_time'].sudo().browse(dyn_lead_time)
                if int(lead_time_id.x_name) == 3:
                    cost_wh_freight = round(cost_wh_lt * 1.2)
                elif int(lead_time_id.x_name) == 5:
                    cost_wh_freight = round(cost_wh_lt * 1.1)
                elif int(lead_time_id.x_name) == 7:
                    cost_wh_freight = round(cost_wh_lt * 1)

            freight_id = request.env['service.cost'].sudo().search([('service', '=', 'delivery')], limit=1)
            freight_charge = freight_id.rate * ( (float(powerviz_volume) * freight_id.package_factor)/freight_id.logi_factor )
            freight_final_charges = max(freight_charge, freight_id.min_rate)

            fdm_price = round((rm_cost + ((rm_cost * print_quality) + (rm_cost * infill))), 0) * fdm_quantity
            fdm_product_price = round(rm_cost + ((rm_cost * print_quality) + (rm_cost * infill)), 0)
            # total_price = fdm_price
            fdm_final_price = freight_final_charges + cost_wh_freight
            if dyn_lead_time or filtered_lead_times:
                total_price = (freight_final_charges + cost_wh_freight) * fdm_quantity
                fdm_price = total_price
            else:
                total_price = 0
                fdm_product_price = 0
                fdm_price = total_price
            if uv_printing_side_id and filtered_lead_times:
                # uv_printing_side_price = round((float(projection_price_per_qty * uv_printing_side_factor) / 100.00) * projection_quantity)
                uv_printing_side_price = round(final_cost_uv)
                fdm_price = int(total_price - uv_printing_side_price)
            return {'success':{'total_price':total_price , 'uv_printing_side_price':uv_printing_side_price,'fdm_price':fdm_price,'fdm_product_price':total_price, 'lead_time':lead_time, 'customer_lead_time': [{'id': lt.id, 'x_name': lt.x_name} for lt in filtered_lead_times]}}
            # else:
            #     uv_printing_side_id = request.env['service.number.of.sides'].sudo().browse(uv_printing_side_id)
            #     material_gram = float(powerviz_volume) * fdm_material_id.density * fdm_material_id.factor_support
            #     material_cost_gram = material_gram * fdm_material_id.rate_per_gram
            #     uv_printing_side_factor = uv_printing_side_id.factor
            #
            #     lead_time = round((24 + (material_gram * 0.24)) / 24)
            #     all_lead_times = request.env['x_customer_lead_time'].sudo().search([])
            #     filtered_lead_times = all_lead_times.filtered(
            #         lambda lt: lt.x_name in ['3', '5', '7'] and int(lt.x_name) >= lead_time)
            #
            #     rm_cost = material_cost_gram
            #     print_quality = fdm_print_quality_id.rate
            #     infill = fdm_infill_id.rate
            #
            #     fdm_price_per_qty = round(rm_cost + ((rm_cost * print_quality) + (rm_cost * infill)), 0)
            #     fdm_price =  round(rm_cost + ((rm_cost * print_quality) + (rm_cost * infill)), 0) * fdm_quantity
            #     uv_printing_side_price = round((float(fdm_price_per_qty * uv_printing_side_factor )) / 100.00,1) * fdm_quantity
            #
            #     fdm_product_price_without_qty = round(rm_cost + ((rm_cost * print_quality) + (rm_cost * infill)), 0)
            #     uv_printing_side_price_without_qty = round((float(fdm_product_price_without_qty * uv_printing_side_factor )) / 100.00,0)
            #
            #     fdm_product_price = round(fdm_product_price_without_qty + uv_printing_side_price_without_qty ,0)
            #     total_price = round(fdm_price + uv_printing_side_price ,0)
            #
            #     return {'success':{'total_price':total_price , 'uv_printing_side_price':uv_printing_side_price,'fdm_price':fdm_price,'fdm_product_price':fdm_product_price, 'lead_time':lead_time, 'customer_lead_time': [{'id': lt.id, 'x_name': lt.x_name} for lt in filtered_lead_times]}}

        _logger.exception("Failed to analyze STEP file.")
        return {'error': 'Failed to analyze STEP file.'}

    @http.route(['/calculate/projection/price'], type='json', auth="public", website=True)
    def calculate_projection_price(self, **kw):
        powervis_domain = request.env['ir.config_parameter'].sudo().get_param('cr_web_portal.powervis_url')
        projection_step_file_url = kw['projection_step_file_url'] if 'projection_step_file_url' in kw else ''
        if projection_step_file_url:
            projection_step_file_url = projection_step_file_url.replace(powervis_domain, '')

        projection_material_id = kw['projection_material'] if 'projection_material' in kw else False
        projection_print_quality_id = kw['projection_print_quality'] if 'projection_print_quality' in kw else False
        uv_printing_side_id = kw['uv_printing_side'] if 'uv_printing_side' in kw else False
        projection_quantity = float(kw['projection_quantity']) if 'projection_quantity' in kw else False
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        dyn_lead_time = kw['lead_time'] if 'lead_time' in kw else False
        powerviz_volume = False
        uv_printing_side_price = False

        if projection_step_file_url:
            endpoint = f"{base_url}/api/analyze"
            headers = {'Content-Type': 'application/json'}
            url = projection_step_file_url.strip()

            # Payload (URL to be sent in the request)
            payload = json.dumps({'file_url': url})

            try:
                # Make the POST request
                response = requests.post(endpoint, headers=headers, data=payload)

                # Check for successful response
                if response.status_code == 200:
                    reponse_json = response.json().get('result')
                    _logger.info('==================result===============%s' % reponse_json)
                    if reponse_json.get('volume'):
                        powerviz_volume = float(reponse_json.get('volume'))
                    else:
                        _logger.exception("Failed to analyze STEP file.")
                        return {'error': 'Failed to analyze STEP file.'}
                else:
                    _logger.exception("Failed to analyze STEP file.")
                    return {'error': 'Failed to analyze STEP file.'}

            except requests.RequestException as e:
                # Log any connection errors
                _logger.exception("Connection error occurred: %s", e)
                return {'error': 'Connection error'}
        else:
            _logger.exception("Failed to Generate STEP file URL.")
            return {'error': 'Failed to Generate STEP file URL.'}

        # if not uv_printing_side_id:
        projection_material_id = request.env['service.materials'].sudo().browse(projection_material_id)
        projection_print_quality_id = request.env['service.print.quality'].sudo().browse(
            projection_print_quality_id)
        # material_gram = float(powerviz_volume) * projection_material_id.density
        material_gram = float(powerviz_volume) * projection_material_id.density * projection_material_id.factor_support
        material_cost_gram = material_gram * projection_material_id.rate_per_gram
        lead_time = round((24 + (material_gram * 0.08)) / 24)
        all_lead_times = request.env['x_customer_lead_time'].sudo().search([])
        print_quality = projection_print_quality_id.rate
        filtered_lead_times = all_lead_times.filtered(
            lambda lt: lt.x_name in ['2', '4', '6'] and int(lt.x_name) >= lead_time)
        cost_wh_lt = material_cost_gram + (material_cost_gram * print_quality)
        cost_wh_freight = False
        if uv_printing_side_id:
            uv_printing_side_id = request.env['service.number.of.sides'].sudo().browse(uv_printing_side_id)
            cosu_uv = (uv_printing_side_id.factor/100) * cost_wh_lt
            final_cost_uv = max(cosu_uv, uv_printing_side_id.min_price)
            cost_wh_lt = material_cost_gram + (material_cost_gram * print_quality) + final_cost_uv
            uv_printing_side_factor = uv_printing_side_id.factor
        if filtered_lead_times and not dyn_lead_time:
            if int(filtered_lead_times[0].x_name) == 2:
                cost_wh_freight = round(cost_wh_lt * 1.2)
            elif int(filtered_lead_times[0].x_name) == 4:
                cost_wh_freight = round(cost_wh_lt * 1.1)
            elif int(filtered_lead_times[0].x_name) == 6:
                cost_wh_freight = round(cost_wh_lt * 1)
            if '4' in filtered_lead_times.mapped('x_name'):
                cost_wh_freight = round(cost_wh_lt * 1.1)
        if dyn_lead_time:
            lead_time_id = request.env['x_customer_lead_time'].sudo().browse(dyn_lead_time)
            if int(lead_time_id.x_name) == 2:
                cost_wh_freight = round(cost_wh_lt * 1.2)
            elif int(lead_time_id.x_name) == 4:
                cost_wh_freight = round(cost_wh_lt * 1.1)
            elif int(lead_time_id.x_name) == 6:
                cost_wh_freight = round(cost_wh_lt * 1)
        # uv_printing_side_factor = uv_printing_side_id.factor
        # rm_cost = material_cost_gram
        rm_cost = cost_wh_freight
        freight_id = request.env['service.cost'].sudo().search([('service', '=', 'delivery')], limit=1)
        freight_charge = freight_id.rate * ((float(powerviz_volume) * freight_id.package_factor) / freight_id.logi_factor)
        freight_final_charges = max(freight_charge, freight_id.min_rate)

        projection_price = round(rm_cost + (rm_cost * print_quality), 0) * projection_quantity
        projection_product_price = round(rm_cost + (rm_cost * print_quality), 0)
        # uv_printing_side_price = round((float(projection_price * uv_printing_side_factor)) / 100.00, 0)
        # total_price = projection_price
        projection_price_per_qty = round(rm_cost + (rm_cost * print_quality), 0)
        fdm_final_price = freight_final_charges + cost_wh_freight

        if dyn_lead_time or filtered_lead_times:
            total_price = (freight_final_charges + cost_wh_freight) * projection_quantity
            projection_price = total_price
        else:
            total_price = 0
            projection_product_price = 0
            projection_price = total_price
        if uv_printing_side_id and filtered_lead_times:
            # uv_printing_side_price = round((float(projection_price_per_qty * uv_printing_side_factor) / 100.00) * projection_quantity)
            uv_printing_side_price = round(final_cost_uv)
            projection_price = int(total_price - uv_printing_side_price)
        return {'success': {'total_price': total_price, 'uv_printing_side_price': uv_printing_side_price,'projection_price': projection_price,'projection_product_price':total_price, 'lead_time':lead_time, 'customer_lead_time': [{'id': lt.id, 'x_name': lt.x_name} for lt in filtered_lead_times]}}
        # else:
        #     projection_material_id = request.env['service.materials'].sudo().browse(projection_material_id)
        #     projection_print_quality_id = request.env['service.print.quality'].sudo().browse(projection_print_quality_id)
        #     uv_printing_side_id = request.env['service.number.of.sides'].sudo().browse(uv_printing_side_id)
        #     material_gram = float(powerviz_volume) * projection_material_id.density
        #     material_cost_gram = material_gram * projection_material_id.rate_per_gram
        #     uv_printing_side_factor = uv_printing_side_id.factor
        #
        #     rm_cost = material_cost_gram
        #     print_quality = projection_print_quality_id.rate
        #
        #     projection_price_per_qty = round(rm_cost + (rm_cost * print_quality),0)
        #     projection_price =  round(rm_cost + (rm_cost * print_quality),0) * projection_quantity
        #     uv_printing_side_price = round((float(projection_price_per_qty * uv_printing_side_factor )) / 100.00,1) * projection_quantity
        #
        #     projection_product_price_without_qty =  projection_price_per_qty
        #     uv_printing_side_price_without_qty = round((float(projection_product_price_without_qty * uv_printing_side_factor)) / 100.00, 0)
        #
        #     projection_product_price = round(projection_product_price_without_qty + uv_printing_side_price_without_qty ,0)
        #     total_price = round(projection_price + uv_printing_side_price ,0)
        #
        #     return {'success':{'total_price':total_price , 'uv_printing_side_price':uv_printing_side_price,'projection_price':projection_price,'projection_product_price':projection_product_price}}

        _logger.exception("Failed to analyze STEP file.")
        return {'error': 'Failed to analyze STEP file.'}


    @http.route(['/get/product/files'], type='json', auth="public", website=True)
    def get_product_rec(self, product_id):
        product_id = request.env['product.product'].sudo().browse([int(product_id)])
        data = {}
        variant_images = list(product_id.product_variant_image_ids)
        template_images = list(product_id.product_tmpl_id.product_template_image_ids)
        image_ids = []
        if not variant_images and template_images:
            image_ids.append(template_images)
        if not variant_images and not template_images:
            image_ids.append(product_id)
        if variant_images and variant_images:
            image_ids = variant_images + template_images
        for rec in image_ids:
            if rec._name == 'product.image':
                if rec.glb_image:
                    data['glb_image_url'] = '/web/image/product.image/%s/glb_image' % rec.id
                    data['product_name'] = product_id.name

        data['product_id'] = product_id.id

        if product_id.pdf_file:
            # data['pdf_file'] = product_id.pdf_file
            data['pdf_file_name'] = product_id.pdf_file_name
        if product_id.drawing_fcstd_file:
            # data['drawing_fcstd_file'] = product_id.drawing_fcstd_file
            data['drawing_fcstd_file_name'] = product_id.drawing_fcstd_file_name
        # if product_id.dxf_file:
        #     data['dxf_file'] = product_id.dxf_file
        #     data['dxf_file_name'] = product_id.dxf_file_name
        # if product_id.outsource_pdf_file:
        #     data['outsource_pdf_file'] = product_id.outsource_pdf_file
        #     data['outsource_pdf_file_name'] = product_id.outsource_pdf_file_name
        if product_id and product_id.product_step_file:
            powervis_url =request.env['ir.config_parameter'].sudo().get_param('cr_web_portal.powervis_url')
            base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
            if powervis_url:
                redirect_url = powervis_url + base_url + '/web/content/product.product/%s/product_step_file/%s?download=true' % (product_id.id, product_id.product_step_file_name)
                data['powervis_url'] = redirect_url

        price_list_items = request.env['product.pricelist.item'].sudo().search([('product_id', '=', int(product_id))],
                                                                               order='min_quantity asc')
        is_table_print = True
        for l_items in price_list_items:
            if l_items.fixed_price == 0.0:
                is_table_print = False

        if price_list_items and is_table_print:
            list_items = list(price_list_items)
            header = '''<div class="row product_qty_price_table" style=""> 
                            <div class="product-table">
                                <table class="table table-responsive">
                                    <tbody>
                                        <tr>
                                            <td class="price_table_bg">
                                                <b>Quantity</b>
                                            </td>
                                            <td class="price_table_bg">
                                                <b>Price/Unit</b>
                                            </td>
                                        </tr>
                                        '''
            footer = '''</tbody>
                                </table>
                            </div> 
                    </div>'''
            html = ''
            index = 0
            for index in range(0, len(list_items)):
                html += '<tr><td>'
                if list_items[index].min_quantity:
                    html += str(round(list_items[index].min_quantity))
                    if index + 1 < len(list_items):
                        if round(list_items[index].min_quantity) != (round(list_items[index + 1].min_quantity) - 1):
                            html += ' - ' + str(round(list_items[index + 1].min_quantity) - 1)
                    else:
                        html += ' + </td>'
                html += '<td>' + request.env.company.currency_id.symbol + ' ' + str(
                    list_items[index].fixed_price) + '</td></tr>'

            data['dynamic_html'] = header + html + footer

        data['internal_ref'] = product_id.default_code
        return data

    @http.route(['/create/product/thankyou'], type='http', auth="public", website=True, csrf=False)
    def create_product_thankyou(self, **kwargs):
        if 'service' in request.session and 'inquiry' in request.session:
            service = request.session.get('service')
            inquiry = request.session.get('inquiry')
            request.session.pop('service')
            request.session.pop('inquiry')
            return request.render('cr_web_portal.thank_you_page_for_answer',{'service':service,'inquiry':inquiry})
        else:
            return request.redirect('/my')

    @http.route(['/privacy/policy'], type='http', auth="public", website=True)
    def privacy_page_page(self, ):
        return request.render('cr_web_portal.mechpower_privacy_policy')

    @http.route(['/term/condition'], type='http', auth="public", website=True)
    def term_condition_page(self, ):
        return request.render('cr_web_portal.mechpower_term_and_conditions')

    @http.route(['/shipping/policy'], type='http', auth="public", website=True)
    def shipping_policy_page(self, ):
        return request.render('cr_web_portal.mechpower_shipping_policy')

    @http.route(['/cancellation/policy'], type='http', auth="public", website=True)
    def cancellation_policy_page(self, ):
        return request.render('cr_web_portal.mechpower_cancellation_policy')

    @http.route(['/logo.linkedin',], type='http', auth="none", cors="*")
    def linkedin_logo(self, dbname=None, **kw):
        imgname = 'logo'
        imgext = '.png'
        placeholder = functools.partial(get_resource_path, 'web', 'static', 'img')
        dbname = request.db
        uid = (request.session.uid if dbname else None) or odoo.SUPERUSER_ID

        if not dbname:
            response = http.Stream.from_path(placeholder(imgname + imgext)).get_response()
        else:
            try:
                # create an empty registry
                # registry = odoo.modules.registry.Registry(dbname)
                # with registry.cursor() as cr:
                company = int(kw['company']) if kw and kw.get('company') else False
                if company:
                    # cr.execute("""SELECT linkedin_logo, write_date
                    #                    FROM res_company
                    #                   WHERE id = %s
                    #               """, (company,))
                    # row = cr.fetchone()
                    company = request.env['res.company'].sudo().search([('id', '=', company)])
                    if company:
                        image_base64 = base64.b64decode(company.linkedin_logo)
                        image_data = io.BytesIO(image_base64)
                        mimetype = guess_mimetype(image_base64, default='image/png')
                        imgext = '.' + mimetype.split('/')[1]
                        if imgext == '.svg+xml':
                            imgext = '.svg'
                        response = send_file(
                            image_data,
                            request.httprequest.environ,
                            download_name=imgname + imgext,
                            mimetype=mimetype,
                            last_modified=company.write_date,
                            response_class=Response,
                        )
                    else:
                        response = http.Stream.from_path(placeholder('nologo.png')).get_response()
            except Exception:
                response = http.Stream.from_path(placeholder(imgname + imgext)).get_response()

        return response

    @http.route(['/logo.facebook', ], type='http', auth="none", cors="*")
    def facebook_logo(self, dbname=None, **kw):
        imgname = 'logo'
        imgext = '.png'
        placeholder = functools.partial(get_resource_path, 'web', 'static', 'img')
        dbname = request.db
        uid = (request.session.uid if dbname else None) or odoo.SUPERUSER_ID

        if not dbname:
            response = http.Stream.from_path(placeholder(imgname + imgext)).get_response()
        else:
            try:
                # create an empty registry
                # registry = odoo.modules.registry.Registry(dbname)
                # with registry.cursor() as cr:
                company = int(kw['company']) if kw and kw.get('company') else False
                if company:
                    # cr.execute("""SELECT linkedin_logo, write_date
                    #                    FROM res_company
                    #                   WHERE id = %s
                    #               """, (company,))
                    # row = cr.fetchone()
                    company = request.env['res.company'].sudo().search([('id', '=', company)])
                    if company:
                        image_base64 = base64.b64decode(company.facebook_logo)
                        image_data = io.BytesIO(image_base64)
                        mimetype = guess_mimetype(image_base64, default='image/png')
                        imgext = '.' + mimetype.split('/')[1]
                        if imgext == '.svg+xml':
                            imgext = '.svg'
                        response = send_file(
                            image_data,
                            request.httprequest.environ,
                            download_name=imgname + imgext,
                            mimetype=mimetype,
                            last_modified=company.write_date,
                            response_class=Response,
                        )
                    else:
                        response = http.Stream.from_path(placeholder('nologo.png')).get_response()
            except Exception:
                response = http.Stream.from_path(placeholder(imgname + imgext)).get_response()

        return response

    @http.route(['/logo.instagram', ], type='http', auth="none", cors="*")
    def instagram_logo(self, dbname=None, **kw):
        imgname = 'logo'
        imgext = '.png'
        placeholder = functools.partial(get_resource_path, 'web', 'static', 'img')
        dbname = request.db
        uid = (request.session.uid if dbname else None) or odoo.SUPERUSER_ID

        if not dbname:
            response = http.Stream.from_path(placeholder(imgname + imgext)).get_response()
        else:
            try:
                # create an empty registry
                # registry = odoo.modules.registry.Registry(dbname)
                # with registry.cursor() as cr:
                company = int(kw['company']) if kw and kw.get('company') else False
                if company:
                    # cr.execute("""SELECT linkedin_logo, write_date
                    #                    FROM res_company
                    #                   WHERE id = %s
                    #               """, (company,))
                    # row = cr.fetchone()
                    company = request.env['res.company'].sudo().search([('id', '=', company)])
                    if company:
                        image_base64 = base64.b64decode(company.instagram_logo)
                        image_data = io.BytesIO(image_base64)
                        mimetype = guess_mimetype(image_base64, default='image/png')
                        imgext = '.' + mimetype.split('/')[1]
                        if imgext == '.svg+xml':
                            imgext = '.svg'
                        response = send_file(
                            image_data,
                            request.httprequest.environ,
                            download_name=imgname + imgext,
                            mimetype=mimetype,
                            last_modified=company.write_date,
                            response_class=Response,
                        )
                    else:
                        response = http.Stream.from_path(placeholder('nologo.png')).get_response()
            except Exception:
                response = http.Stream.from_path(placeholder(imgname + imgext)).get_response()

        return response

    @http.route(['/industry_segment_validate'], type='json', auth="public", website=True)
    def industry_segment_validation(self,**kw):
        if request.env.user._is_public():
            return True
        partner_id = request.env.user.partner_id
        error = {'industry_mandatory': True,'address_mandatory':True}
        if not partner_id.industry_main_category or not partner_id.industry_sub_category:
            error['industry_mandatory'] = False
        if not partner_id.street or not partner_id.zip or not partner_id.city or not partner_id.state_id or not partner_id.country_id:
            error['address_mandatory'] = False
        return error

    @http.route(['/filter_state'], type='json', auth="user", website=True)
    def filter_state(self,country_id,**kw):
        states = request.env['res.country.state'].sudo().search([('country_id','=',int(country_id))])
        response = []
        if states:
            for state in states:
                response.append({'id':state.id,'state_name':state.name})

            return response
        return []

    @http.route(['/get_cities'], type='json', auth="user", website=True)
    def get_cities(self, country_id, state_id,**kw):
        cities = False
        if country_id and state_id:
            cities = request.env['res.city'].sudo().search([('country_id', '=', int(country_id)), ('state_id', '=', int(state_id))])
        elif country_id:
            cities = request.env['res.city'].sudo().search([('country_id', '=', int(country_id))])
        elif state_id:
            cities = request.env['res.city'].sudo().search([('state_id', '=', int(state_id))])
        response = []
        if cities:
            for city in cities:
                response.append({'id': city.id, 'city_name': city.name})
            return response
        return []
