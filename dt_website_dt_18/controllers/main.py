# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json
from werkzeug.exceptions import NotFound
import re


class WebsiteCustom(http.Controller):
    
    #################################################################################################
    #                                               PLATFORM                                        #
    #################################################################################################

    @http.route(['/platform/digital-analytics-platform'], type='http', auth="public", website=True)
    def digital_analytics(self, **kw):
        return request.render("website_dt.digital_analytics_platform")
    
    @http.route(['/platform/turn-key-reporting-implementation'], type='http', auth="public", website=True)
    def reporting_implementation(self, **kw):
        return request.render("website_dt.turn_key_reporting_implementation")
    
    @http.route(['/platform/self-analytics-solution'], type='http', auth="public", website=True)
    def self_analytics_solution(self, **kw):
        return request.render("website_dt.self_analytics_solution")
    
    @http.route(['/platform/dashboard-builder'], type='http', auth="public", website=True)
    def dashboard_builder(self, **kw):
        return request.render("website_dt.dashboard_builder")
    
    #################################################################################################
    #                                               SOLUTIONS                                       #
    #################################################################################################

    @http.route(['/solutions'], type='http', auth="public", website=True)
    def solutions(self, **kw):
        return request.render("website_dt.solutions")
    
    @http.route(['/solutions/brand-health-tracking'], type='http', auth="public", website=True)
    def brand_health_tracking(self, **kw):
        return request.render("website_dt.brand_health_tracking")
    
    @http.route(['/solutions/net-promoter-score'], type='http', auth="public", website=True)
    def net_promoter_score(self, **kw):
        return request.render("website_dt.net_promoter_score")
    
    @http.route(['/solutions/hr-tracking'], type='http', auth="public", website=True)
    def hr_tracking(self, **kw):
        return request.render("website_dt.hr_tracking")
    
    #################################################################################################
    #                                               CASES                                           #
    #################################################################################################

    @http.route(['/case-studies'], type='http', auth="public", website=True)
    def case_studies(self, **kw):
        return request.render("website_dt.case_studies")
    
    @http.route(['/cases/jicmail-discovery'], type='http', auth="public", website=True)
    def jicmail_discovery(self, **kw):
        return request.render("website_dt.jicmail_discovery")
    
    @http.route(['/cases/transformed-employee-satisfaction-analysis'], type='http', auth="public", website=True)
    def employee_satisfaction(self, **kw):
        return request.render("website_dt.employee_satisfaction")
    
    @http.route(['/cases/fastuna'], type='http', auth="public", website=True)
    def fastuna(self, **kw):
        return request.render("website_dt.fastuna")
    
    @http.route(['/cases/sinomonitor'], type='http', auth="public", website=True)
    def sinomonitor(self, **kw):
        return request.render("website_dt.sinomonitor")
    
    @http.route(['/cases/global'], type='http', auth="public", website=True)
    def global_cases(self, **kw):
        return request.render("website_dt.global_cases")

    #################################################################################################
    #                                               LEGAl                                           #
    #################################################################################################

    @http.route(['/legal/privacy-policy'], type='http', auth="public", website=True)
    def privacy_policy(self, **kw):
        return request.render("website_dt.privacy_policy")
    
    @http.route(['/legal/terms-of-use'], type='http', auth="public", website=True)
    def terms_of_use(self, **kw):
        return request.render("website_dt.terms_of_use")

    @http.route(['/about-us'], type='http', auth="public", website=True)
    def about_us(self, **kw):
        return request.render("website_dt.about_us")
    
    @http.route(['/contact-us'], type='http', auth="public", website=True)
    def contact_us(self, **kw):
        return request.render("website_dt.contact_us")

    @http.route(['/legal/cookie-list'], type='http', auth="public", website=True)
    def cookie_list(self, **kw):
        return request.render("website_dt.cookie_list")

    @http.route(['/legal/license-agreement'], type='http', auth="public", website=True)
    def licence_agreement(self, **kw):
        return request.render("website_dt.licence_agreement")

    @http.route(['/legal/license-agreement-archive'], type='http', auth="public", website=True)
    def licence_agreement_archive(self, **kw):
        return request.render("website_dt.licence_agreement_archive")

    @http.route(['/pricing'], type='http', auth="public", website=True)
    def pricing(self, **kw):
        return request.render("website_dt.pricing")

    @http.route('/contact-us/thankyou', type='http', auth="public", methods=['POST'], website=True)
    def submit_contact_form(self, **kw):
        # Handle form submission
        company_name = kw.get('companyName')
        email = kw.get('email')
        full_name = kw.get('fullName')
        job_title = kw.get('jobTitle')
        message = kw.get('message')

        # You can create a CRM lead or perform any other actions here
        request.env['crm.lead'].sudo().create({
            'name': company_name,
            'email_from': email,
            'contact_name': full_name,
            'function': job_title,
            'description': message,
        })

        return request.render("website_dt.thank_you_template")

    #################################################################################################
    #                                               Dashboard                                       #
    #################################################################################################

    @http.route('/dashboard/filter', type='json', auth='public')
    def filter_dashboard(self, category_ids=None):
        domain = []
        if category_ids:
            domain = [('category_ids', 'in', category_ids)]

        records = request.env['dashboard.record'].sudo().search(domain)
        data = []
        for record in records:
            data.append({
                'name': record.name,
                'image': record.icon_image,
                'url': record.url,
                'description': record.description,
                'categories': [c.name for c in record.category_ids]
            })

        return data

    @http.route(['/dashboard-gallery'], type='http', auth="public", website=True)
    def dashboard_gallery(self, category_ids=None):
        domain = []
        if category_ids:
            domain = [('category_ids', 'in', category_ids)]

        records = request.env['dashboard.record'].sudo().search(domain)
        data = []
        for record in records:
            data.append({
                'name': record.name,
                'image': record.icon_image,
                'url': record.url,
                'description': record.description,
                'categories': [c.name for c in record.category_ids]
            })
        return request.render("website_dt.dashboard_gallery", {
            'dashboards': data
        })

    @http.route(['/dashboards/hr-dashboard'], type='http', auth="public", website=True)
    def dashboards_hr_dashboard(self, **kw):
        return request.render("website_dt.dashboards_hr_dashboard")

    @http.route(['/dashboards/energy-drink-bht'], type='http', auth="public", website=True)
    def dashboards_energy_drink(self, **kw):
        return request.render("website_dt.dashboards_energy_drink_bht")

    @http.route(['/dashboards/global-brand-tracking'], type='http', auth="public", website=True)
    def dashboards_global_brand_tracking(self, **kw):
        return request.render("website_dt.dashboards_global_brand_tracking")

    @http.route(['/dashboards/social-media-listening'], type='http', auth="public", website=True)
    def dashboards_social_media_listening(self, **kw):
        return request.render("website_dt.dashboards_social_media_listening")

    @http.route(['/dashboards/tv-set-purchase'], type='http', auth="public", website=True)
    def dashboards_tv_set_purchase(self, **kw):
        return request.render("website_dt.dashboards_tv_set_purchase")

    @http.route(['/dashboards/renewable-energy-worldwide'], type='http', auth="public", website=True)
    def dashboards_renewable_energy_worldwide(self, **kw):
        return request.render("website_dt.dashboards_renewable_energy_worldwide")

    @http.route(['/dashboards/ocean-clean-up'], type='http', auth="public", website=True)
    def dashboards_ocean_clean_up(self, **kw):
        return request.render("website_dt.dashboards_ocean_clean_up")

    @http.route(['/dashboards/bank-csi'], type='http', auth="public", website=True)
    def dashboards_bank_csi(self, **kw):
        return request.render("website_dt.dashboards_bank_csi")

    @http.route(['/dashboards/tv-series-audience'], type='http', auth="public", website=True)
    def dashboards_tv_series_audience(self, **kw):
        return request.render("website_dt.dashboards_tv_series_audience")

    @http.route(['/dashboards/freedom-of-the-net-2024'], type='http', auth="public", website=True)
    def dashboards_freedom_of_the_net_2024(self, **kw):
        return request.render("website_dt.dashboards_freedom_of_the_net_2024")

    #################################################################################################
    #                                          SANDBOX SUBMIT                                       #
    #################################################################################################

    @http.route('/create/access', type='http', auth='public', methods=['POST'], csrf=False)
    def create_lead(self, **kwargs):
        try:
            # Extract form data
            email = kwargs.get("email")
            company = kwargs.get("company")
            country_id = kwargs.get("country_id")
            first_name = kwargs.get("first_name")
            last_name = kwargs.get("last_name")

            # Create Lead in CRM
            lead = request.env["crm.lead"].sudo().create({
                "name": f"Sandbox Request: {first_name} {last_name}",
                "email_from": email,
                "partner_name": company,
                "country_id": int(country_id) if country_id else False,
                "contact_name": f"{first_name} {last_name}",
                "description": "Request for sandbox access",
            })

            return json.dumps({"success": True, "lead_id": lead.id})

        except Exception as e:
            return json.dumps({"success": False, "message": str(e)})

    @http.route('/create/subscription', type='http', auth="public", methods=['POST'], csrf=False)
    def create_subscription(self, **post):
        try:
            email = post.get('email')
            if not email:
                return json.dumps({"success": False, "message": "Email is required"})

            mailing_contact = request.env['mailing.contact'].sudo().create({
                'email': email,
                'name': email,
                'list_ids': [(4, request.env.ref('mass_mailing.mailing_list_data').id)]
            })

            return json.dumps({"success": True, "message": "Successfully subscribed"})

        except Exception as e:
            return json.dumps({"success": False, "message": str(e)})