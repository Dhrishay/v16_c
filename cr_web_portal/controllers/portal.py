import base64
import csv
import tempfile
from collections import OrderedDict
from odoo import fields, http, _
from odoo.addons.portal.controllers import portal
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import pager as portal_pager, get_records_pager
from odoo.exceptions import AccessError, MissingError,AccessDenied,UserError
from odoo.http import content_disposition, Controller, request, route
from werkzeug.urls import url_encode
import binascii
import os
import re
import uuid
import json

class CustomerPortal(portal.CustomerPortal):
    _items_per_page = 20

    @http.route(['/my/invoices/<int:invoice_id>'], type='http', auth="public", website=True)
    def portal_my_invoice_detail(self, invoice_id, access_token=None, report_type=None, download=False, **kw):
        try:
            invoice_sudo = self._document_check_access('account.move', invoice_id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=invoice_sudo, report_type=report_type, report_ref='account.account_invoices',
                                     download=download)

        values = self._invoice_get_page_view_values(invoice_sudo, access_token, **kw)
        return request.render("cr_web_portal.report_invoice_document_custom", values)

    @http.route('/custom/attachment/create', type='http', auth='user', csrf=False)
    def create_attachment(self, **kwargs):
        attachment = request.httprequest.files.get('file')
        
        res_model = kwargs.get('res_model')
        res_id = int(kwargs.get('res_id', 0)) if kwargs.get('res_id') else None
        access_token = uuid.uuid4().hex
        attachment_record = request.env['ir.attachment'].sudo().create({
            'name': attachment.filename,
            'datas': base64.b64encode(attachment.read()),
            'mimetype': attachment.mimetype,
            'res_model': res_model if res_model else None,
            'res_id': res_id if res_id else None,
            'public': True,
            'access_token': access_token
        })

        response_data = {
            'id': attachment_record.id,
            'access_token': access_token
        }
        return request.make_response(json.dumps(response_data), status=200, headers={'Content-Type': 'application/json'})

    @http.route(['/my/messages'], type='http', auth="user", website=True)
    def my_messages(self, filterby='all', search=None):
        user = request.env.user
        sale_orders = []
        quotations = []
        inquirys = []
        invoices = []
        tickets = []
        messages = []
        search_domain = []
        if search:
            search_domain = ['|', ('name', 'ilike', search), ('website_message_ids.body', 'ilike', search)]
        searchbar_filters = {
            'all': {'label': _('All'), 'domain': []},
            'inquiry': {'label': _('Inquiry'), 'domain': []},
            'quotation': {'label': _('Quotation'), 'domain': []},
            'sale_order': {'label': _('Sales Order'), 'domain': []},
            'invoice': {'label': _('Invoice'), 'domain': []},
            'ticket': {'label': _('Ticket'), 'domain': []},
        }

        searchbar_inputs = {
            'all': {'label': _('Search in All'), 'input': 'all'},
        }

        if filterby == 'inquiry':
            domain = [('message_partner_ids', 'child_of', [user.partner_id.commercial_partner_id.id]),
                 ('state', 'in', ['inquiry', 'engineering_review', 'prepared_for_pricing', 'data_feedback'])] + search_domain
            inquirys = request.env['sale.order'].sudo().search(domain)
        elif filterby == 'quotation':
            domain = [('message_partner_ids', 'child_of', [user.partner_id.commercial_partner_id.id]),
                 ('state', '=', 'sent')] + search_domain
            quotations = request.env['sale.order'].sudo().search(domain)
        elif filterby == 'sale_order':
            domain = [('message_partner_ids', 'child_of', [user.partner_id.commercial_partner_id.id]),
                 ('state', '=', 'sale')] + search_domain
            sale_orders = request.env['sale.order'].sudo().search(domain)
        elif filterby == 'invoice':
            type = ('out_invoice', 'out_refund', 'in_invoice', 'in_refund', 'out_receipt', 'in_receipt')
            domain = [('partner_id', '=', user.partner_id.id), ('state', 'not in', ('cancel', 'draft')),
                      ('move_type', 'in', type)] + search_domain
            invoices = request.env['account.move'].sudo().search(domain)
        elif filterby == 'ticket':
            domain = [('partner_id', '=', user.partner_id.id)] + search_domain
            tickets = request.env['helpdesk.ticket'].sudo().search(domain)
        else:
            domain_1 = [('message_partner_ids', 'child_of', [user.partner_id.commercial_partner_id.id]),
                 ('state', '=', 'sale')] + search_domain
            domain_2 = [('message_partner_ids', 'child_of', [user.partner_id.commercial_partner_id.id]),
                 ('state', '=', 'sent')] + search_domain
            domain_3 = [('message_partner_ids', 'child_of', [user.partner_id.commercial_partner_id.id]),
                 ('state', 'in', ['inquiry', 'engineering_review', 'prepared_for_pricing', 'data_feedback'])] + search_domain
            type = ('out_invoice', 'out_refund', 'in_invoice', 'in_refund', 'out_receipt', 'in_receipt')
            domain_4 = [('partner_id', '=', user.partner_id.id), ('state', 'not in', ('cancel', 'draft')), ('move_type', 'in', type)] + search_domain
            domain_5 = [('partner_id', '=', user.partner_id.id)] + search_domain

            sale_orders = request.env['sale.order'].sudo().search(domain_1)
            quotations = request.env['sale.order'].sudo().search(domain_2)
            inquirys = request.env['sale.order'].sudo().search(domain_3)
            invoices = request.env['account.move'].sudo().search(domain_4)
            tickets = request.env['helpdesk.ticket'].sudo().search(domain_5)

        def get_last_message(record):
            """Retrieve the last message, sender name, and whether it was sent by the current user."""

            def strip_html_tags(text):
                """Strip HTML tags from a string."""
                clean = re.compile('<.*?>')
                return re.sub(clean, '', text)

            last_message = record.message_ids.filtered(
                lambda m: m.message_type in ['comment', 'email']
            ).sorted(lambda m: m.date, reverse=True)[:1]
            if last_message:
                message_body = last_message.body or ''
                plain_text_body = strip_html_tags(message_body)  # Remove HTML tags
                sender_name = "You" if last_message.author_id == user.partner_id else last_message.author_id.name
                return {
                    'body': plain_text_body,
                    'sender_name': sender_name + ':' if sender_name else '',
                }
            return {'body': 'No messages', 'sender_name': ''}

        for order in sale_orders:
            last_msg = get_last_message(order)
            messages.append({
                'type': 'sale_order',
                'name': order.name,
                'preview': last_msg['body'],
                'sender_name': last_msg['sender_name'],
                'res_id': order.id,
                'res_model': order._name,
            })

        for quotation in quotations:
            last_msg = get_last_message(quotation)
            messages.append({
                'type': 'quotation',
                'name': quotation.name,
                'preview': last_msg['body'],
                'sender_name': last_msg['sender_name'],
                'res_id': quotation.id,
                'res_model': quotation._name,
            })

        for inquiry in inquirys:
            last_msg = get_last_message(inquiry)
            messages.append({
                'type': 'inquiry',
                'name': inquiry.name,
                'preview': last_msg['body'],
                'sender_name': last_msg['sender_name'],
                'res_id': inquiry.id,
                'res_model': inquiry._name,
            })

        for invoice in invoices:
            last_msg = get_last_message(invoice)
            messages.append({
                'type': 'invoice',
                'name': invoice.name,
                'preview': last_msg['body'],
                'sender_name': last_msg['sender_name'],
                'res_id': invoice.id,
                'res_model': invoice._name,
            })

        for ticket in tickets:
            last_msg = get_last_message(ticket)
            messages.append({
                'type': 'ticket',
                'name': ticket.name,
                'preview': last_msg['body'],
                'sender_name': last_msg['sender_name'],
                'res_id': ticket.id,
                'res_model': ticket._name,
            })
        return request.render('cr_web_portal.portal_my_messages', {
            'messages': messages,
            'user': user.partner_id.id,
            'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            'filterby': filterby,
            'searchbar_inputs': searchbar_inputs,
            'search': search,
            'default_url': '/my/messages'
        })

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        SaleOrder = request.env['sale.order']
        partner = request.env.user.partner_id

        if 'inquiries_count' in counters:
            lead_inquiry = request.env['crm.lead'].sudo().search(
                [('user_id', '=', request.env.user.id), ('type', '=', 'opportunity')])
            values['inquiries_count'] = len(lead_inquiry)

        partner = request.env.user.partner_id

        SaleOrder = request.env['sale.order']
        if 'quotation_count' in counters:
            values['quotation_count'] = len(
                SaleOrder.sudo().search([('partner_id', '=', partner.id), ('state', 'in', ['sent'])])) or 0

        if 'inquiry_quotation_count' in counters:
            values['inquiry_quotation_count'] = len(SaleOrder.sudo().search([('partner_id', '=', partner.id),('state', 'in', ['inquiry','engineering_review', 'data_feedback', 'prepared_for_pricing'])])) or 0
        if 'dashboard_count' in counters:
            values.update({
                'dashboard_count': 1,
            })
        if 'account_count' in counters:
            values.update({
                'account_count': 1,
            })
        if 'security_count' in counters:
            values.update({
                'security_count': 1,
            })
        return values

    @http.route(['/my/inquiries', '/my/inquiries/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_orders_custom(self, page=1, date_begin=None, sortby=None, filterby='all', search=None,
                                groupby='none', search_in='content', **kw):
        values = self._prepare_portal_layout_values()
        user_id = request.env.user
        user_partner_id = request.env.user.partner_id

        searchbar_sortings = {
            'date': {'label': _('Date'), 'order': 'create_date desc'},
            'order_id': {'label': _('Order No'), 'order': 'order_id desc'},
            'amount': {'label': _('Amount'), 'order': 'amount desc'},

        }
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']

        searchbar_filters = {
            'all': {'label': _('All'), 'domain': [('partner_id', '=', user_partner_id.id)]}},

        lead_inquiry = request.env['crm.lead'].sudo().search(
            [('user_id', '=', user_id.id), ('type', '=', 'opportunity')])
        inquiry_count = len(lead_inquiry)

        # pager
        pager = portal_pager(
            url="/my/inquiries",
            url_args=kw,
            total=inquiry_count,
            page=page,
            step=20,

        )
        lead_inquiry = request.env['crm.lead'].sudo().search(
            [('user_id', '=', user_id.id), ('type', '=', 'opportunity')], order=order, limit=self._items_per_page,
            offset=pager['offset'])

        # request.session['my_pricelist_history'] = referral_lines.ids[:100]
        request.session['my_inquiry_history'] = lead_inquiry.ids[:100]
        values.update({
            'date': date_begin,
            'lead_inquiry': lead_inquiry,
            'page_name': 'inquiry_tree',
            'pager': pager,
            'default_url': '/my/inquiries',
            'searchbar_sortings': searchbar_sortings,
            # 'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            'sortby': sortby,
            'filterby': filterby,
        })
        return request.render("cr_web_portal.portal_my_inquiries_portal_list_template", values)

    def _update_password(self, old, new1, new2):
        for k, v in [('old', old), ('new1', new1), ('new2', new2)]:
            if not v:
                return {'errors': {'password': {k: _("You cannot leave any password empty.")}}}

        try:
            request.env.user._check_credentials(old, {'interactive': True})
        except AccessDenied as e:
            msg = e.args[0]
            if msg == AccessDenied().args[0]:
                msg = _('The old password you provided is incorrect.')
                return {'errors': {'password': {'old': msg}}}

        if new1 != new2:
            return {'errors': {'password': {'new2': _("The passwords you entered did not match.")}}}

        try:
            request.env['res.users'].change_password(old, new1)
            template = request.env.ref('cr_web_portal.change_password_email')
            user = request.env.user
            if template and user:
                template.sudo().send_mail(user.id, force_send=True)
        except AccessDenied as e:
            msg = e.args[0]
            if msg == AccessDenied().args[0]:
                msg = _('The old password you provided is incorrect.')
            return {'errors': {'password': {'old': msg}}}
        except UserError as e:
            return {'errors': {'password': e.name}}

        # update session token so the user does not get logged out (cache cleared by passwd change)
        new_token = request.env.user._compute_session_token(request.session.sid)
        request.session.session_token = new_token

        return {'success': {'password': True}}
    @http.route(['/my/inquiries/<int:lead_id>'], type='http', auth="public", website=True)
    def portal_my_inquiries_detail(self, lead_id, report_type=None, access_token=None, message=False, download=False,
                                   **kw):
        try:
            order_sudo = self._document_check_access('crm.lead', lead_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')
        # check for inquiry button to be display or not
        product_ids = order_sudo.lead_product_ids.filtered(
            lambda x: x.product_id and x.product_id.detailed_type == 'service').mapped('product_id')
        product_id = False
        service_id = False
        if product_ids:
            product_id = product_ids[0]
            service_id = request.env['services.services'].sudo().search(
                [('product_id', '=', product_id.product_tmpl_id.id)])
        values = {
            'lead': order_sudo,
            'page_name': 'inquiry',
            'report_type': 'html',
            'show_inquiry_button': True if service_id else False,
            'res_company': order_sudo.company_id,  # Used to display correct company logo
        }
        history_session_key = 'my_inquiry_history'
        values = self._get_page_view_values(
            order_sudo, access_token, values, history_session_key, False)

        return request.render('cr_web_portal.inquiry_portal_template', values)

    def _prepare_quotations_domain(self, partner):
        return [
            ('partner_id', 'in', [partner.id]),
            ('state', 'in', ['sent'])
        ]

    def _prepare_inquiry_quotations_domain(self, partner):
        return [
            ('partner_id', 'in', [partner.id]),
            ('state', 'in', ['inquiry','engineering_review', 'prepared_for_pricing', 'data_feedback'])
        ]

    @http.route(['/my/inquiry/quotes', '/my/inquiry/quotes/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_quotes_inquiry(self, **kwargs):
        values = self._prepare_sale_portal_inquiry_quotation_rendering_values(**kwargs)
        request.session['my_quotations_inquiry_history'] = values['inquiry_quotations'].ids[:100]
        return request.render("cr_web_portal.portal_my_inquiry_quotations", values)

    @http.route(['/my/document/history/<string:field_name>/<int:product_id>','/my/document/history/<string:field_name>/<int:product_id>/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_quotes_inquiry_dhdhhd(self,field_name,product_id,page=1,**kwargs):
        values = self._prepare_portal_layout_values()
        document_history = request.env['document.history'].sudo().search([('product_id','=',product_id),('file_type','=',field_name)])
        cst_url = '/my/document/history/%s/%s' % (field_name,product_id)
        pager = portal_pager(
            url=cst_url,
            total=len(document_history),
            page=page,
            step=20
        )
        document_history = request.env['document.history'].sudo().search(
            [('product_id', '=', product_id), ('file_type', '=', field_name)], limit=self._items_per_page,
            offset=pager['offset'])
        values.update({
            'doc_history':document_history,
            'page_name': 'document_history',
            'default_url': '/my/holidays',
            'pager': pager,
        })
        return request.render("cr_web_portal.portal_document_history", values)

    def _prepare_sale_portal_inquiry_quotation_rendering_values(
        self, page=1, date_begin=None, date_end=None, sortby=None, **kwargs
    ):
        SaleOrder = request.env['sale.order'].sudo()

        if not sortby:
            sortby = 'date'

        partner = request.env.user.partner_id
        values = self._prepare_portal_layout_values()

        url = "/my/inquiry/quotes"
        domain = self._prepare_inquiry_quotations_domain(partner)
        searchbar_sortings = self._get_sale_searchbar_sortings()

        sort_order = searchbar_sortings[sortby]['order']

        if date_begin and date_end:
            domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]
        pager_values = portal_pager(
            url=url,
            total=SaleOrder.search_count(domain),
            page=page,
            step=self._items_per_page,
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
        )
        orders = SaleOrder.search(domain, order=sort_order, limit=self._items_per_page, offset=pager_values['offset'])

        values.update({
            'date': date_begin,
            'inquiry_quotations': orders,
            'page_name': 'inquiry_quote',
            'pager': pager_values,
            'default_url': url,
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })

        return values

    @http.route(['/my/inquiry/quotes/<int:order_id>'], type='http', auth="public", website=True)
    def portal_inquiry_quote__page(self, order_id, report_type=None, access_token=None, message=False, download=False, **kw):
        try:
            order_sudo = self._document_check_access('sale.order', order_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=order_sudo, report_type=report_type,
                                     report_ref='cr_web_portal.action_report_inquiry_quotaion', download=download)

        if request.env.user.share and access_token:
            # If a public/portal user accesses the order with the access token
            # Log a note on the chatter.
            today = fields.Date.today().isoformat()
            session_obj_date = request.session.get('view_inquiry_quote_%s' % order_sudo.id)
            if session_obj_date != today:
                # store the date as a string in the session to allow serialization
                request.session['view_inquiry_quote_%s' % order_sudo.id] = today
                # The "Quotation viewed by customer" log note is an information
                # dedicated to the salesman and shouldn't be translated in the customer/website lgg
                context = {'lang': order_sudo.user_id.partner_id.lang or order_sudo.company_id.partner_id.lang}
                msg = _('Inquiry viewed by customer %s',
                        order_sudo.partner_id.name if request.env.user._is_public() else request.env.user.partner_id.name)
                del context
                _message_post_helper(
                    "sale.order",
                    order_sudo.id,
                    message=msg,
                    token=order_sudo.access_token,
                    message_type="notification",
                    subtype_xmlid="mail.mt_note",
                    partner_ids=order_sudo.user_id.sudo().partner_id.ids,
                )

        backend_url = f'/web#model={order_sudo._name}' \
                      f'&id={order_sudo.id}' \
                      f'&action={order_sudo._get_portal_return_action().id}' \
                      f'&view_type=form'
        values = {
            'sale_order': order_sudo,
            'message': message,
            'report_type': 'html',
            'backend_url': backend_url,
            'res_company': order_sudo.company_id,  # Used to display correct company logo
        }

        # Payment values
        if order_sudo._has_to_be_paid():
            values.update(self._get_payment_values(order_sudo))

        history_session_key = 'my_quotations_inquiry_history'

        values = self._get_page_view_values(
            order_sudo, access_token, values, history_session_key, False)

        files = []
        if order_sudo.order_line and order_sudo.is_customisable:
            product_id = order_sudo.order_line[0].product_id.id
            for file in order_sudo:
                download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                    product_id, 'technical_drawing_file', order_sudo.order_line[0].product_id.technical_drawing_file_name, 'download=true')
                if order_sudo.order_line[0].product_id.technical_drawing_file_name:
                    files.append({
                        'download_url': download_url,
                        'name': order_sudo.order_line[0].product_id.technical_drawing_file_name,
                        'file': order_sudo.order_line[0].product_id.technical_drawing_file,
                        'title': 'Technical Drawing File',
                        'type': 'file',
                        'field_name': 'technical_drawing_file'
                    })
            for fileuv in order_sudo:
                if order_sudo.order_line[0].product_id.uv_printing_file_name:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_id, 'uv_printing_file', order_sudo.order_line[0].product_id.uv_printing_file_name, 'download=true')
                    files.append({
                        'download_url': download_url,
                        'name': order_sudo.order_line[0].product_id.uv_printing_file_name,
                        'file': order_sudo.order_line[0].product_id.uv_printing_file,
                        'title': 'UV Printing File',
                        'type': 'file',
                        'field_name': 'uv_printing_file'
                    })
                if order_sudo.order_line[0].product_id.additional_notes:
                    files.append({
                        'note': order_sudo.order_line[0].product_id.additional_notes,
                        'title': 'Extra Notes',
                        'type': 'note',
                    })

        backendfiles = []
        for ord in order_sudo:
            if ord.order_line and ord.order_line[0].product_id:
                product_id = ord.order_line[0].product_id

                if product_id.pdf_file:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_id.id, 'pdf_file', product_id.pdf_file_name, 'download=true')
                    backendfiles.append({
                        'download_url': download_url,
                        'name': product_id.pdf_file_name,
                        'file': product_id.pdf_file,
                        'title': 'Data Sheet',
                        'field_name':'pdf_file',
                    })
                if product_id.drawing_fcstd_file:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_id.id, 'drawing_fcstd_file', product_id.product_step_file_name, 'download=true')
                    backendfiles.append({
                        'download_url': download_url,
                        'name': product_id.product_step_file_name,
                        'file': product_id.drawing_fcstd_file,
                        'title': 'PCB Outline',
                        'field_name': 'drawing_fcstd_file',
                    })
                if product_id.x_studio_exception_file:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_id.id, 'x_studio_exception_file', product_id.exception_file_name, 'download=true')
                    backendfiles.append({
                        'download_url': download_url,
                        'name': product_id.exception_file_name,
                        'file': product_id.x_studio_exception_file,
                        'title': 'Technical Query',
                        'field_name': 'x_studio_exception_file',
                    })
                if product_id.x_studio_exception_reply_file:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_id.id, 'x_studio_exception_reply_file', product_id.exception_reply_file_name,
                        'download=true')
                    backendfiles.append({
                        'download_url': download_url,
                        'name': product_id.exception_reply_file_name,
                        'file': product_id.x_studio_exception_reply_file,
                        'title': 'Technical Query Response',
                        'field_name': 'x_studio_exception_reply_file',
                    })
        values['files'] = files
        values['backendfiles'] = backendfiles
        service_file = []
        if order_sudo.service and order_sudo.order_line and order_sudo.order_line[0].product_template_id:
            product_tmp_id = order_sudo.order_line[0].product_template_id.product_variant_ids[0].id
            for file_service in order_sudo:
                if order_sudo.order_line[0].product_template_id.product_variant_ids[0].cnc_machining_upload_technical_drawing:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_tmp_id, 'cnc_machining_upload_technical_drawing',
                        file_service.order_line[0].product_template_id.product_variant_ids[0].cnc_machining_upload_technical_drawing_filename,
                        'download=true')
                    service_file.append({
                        'download_url': download_url,
                        'name': order_sudo.order_line[0].product_template_id.product_variant_ids[0].cnc_machining_upload_technical_drawing_filename,
                        'file': order_sudo.order_line[0].product_template_id.product_variant_ids[0].cnc_machining_upload_technical_drawing,
                        'title': 'Technical Drawing File',
                        'field_name':'cnc_machining_upload_technical_drawing'
                    })
                if order_sudo.order_line[0].product_template_id.product_variant_ids[0].cnc_uv_printing_file:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_tmp_id, 'cnc_uv_printing_file',
                        file_service.order_line[0].product_template_id.product_variant_ids[0].cnc_uv_printing_filename,
                        'download=true')
                    service_file.append({
                        'download_url': download_url,
                        'name': order_sudo.order_line[0].product_template_id.product_variant_ids[0].cnc_uv_printing_filename,
                        'file': order_sudo.order_line[0].product_template_id.product_variant_ids[0].cnc_uv_printing_file,
                        'title': 'Uv Printing File',
                        'field_name': 'cnc_uv_printing_file'
                    })
                if order_sudo.order_line[0].product_template_id.product_variant_ids[0].x_studio_exception_file:
                    if order_sudo.order_line[0].product_template_id.product_variant_ids[0].x_studio_exception_file:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_tmp_id, 'x_studio_exception_file',
                            file_service.order_line[0].product_template_id.product_variant_ids[0].x_studio_exception_file,
                            'download=true')
                        service_file.append({
                            'download_url': download_url,
                            'name': order_sudo.order_line[
                                0].product_template_id.product_variant_ids[0].exception_file_name,
                            'file': order_sudo.order_line[0].product_template_id.product_variant_ids[0].x_studio_exception_file,
                            'title': 'Technical query',
                            'field_name':'x_studio_exception_file'
                        })

                if order_sudo.order_line[0].product_template_id.product_variant_ids[0].x_studio_exception_reply_file:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_tmp_id, 'x_studio_exception_reply_file',
                        file_service.order_line[0].product_template_id.product_variant_ids[0].x_studio_exception_reply_file,
                        'download=true')
                    service_file.append({
                        'download_url': download_url,
                        'name': order_sudo.order_line[
                            0].product_template_id.product_variant_ids[0].exception_reply_file_name,
                        'file': order_sudo.order_line[0].product_template_id.product_variant_ids[0].x_studio_exception_reply_file,
                        'title': 'Technical query response',
                        'field_name': 'x_studio_exception_reply_file'
                    })

                if order_sudo.order_line[0].product_template_id.product_variant_ids[0].injection_mold_upload_technical_drawing:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_tmp_id, 'injection_mold_upload_technical_drawing',
                        file_service.order_line[0].product_template_id.product_variant_ids[0].injection_mold_upload_technical_drawing_filename,
                        'download=true')
                    service_file.append({
                        'download_url': download_url,
                        'name': order_sudo.order_line[
                            0].product_template_id.product_variant_ids[0].injection_mold_upload_technical_drawing_filename,
                        'file': order_sudo.order_line[0].product_template_id.product_variant_ids[0].injection_mold_upload_technical_drawing,
                        'title': 'Upload Technical Drawing',
                        'field_name': 'injection_mold_upload_technical_drawing'

                    })
                if order_sudo.order_line[0].product_template_id.product_variant_ids[0].injection_uv_printing_file:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_tmp_id, 'injection_uv_printing_file',
                        file_service.order_line[0].product_template_id.product_variant_ids[0].injection_uv_printing_filename,
                        'download=true')
                    service_file.append({
                        'download_url': download_url,
                        'name': order_sudo.order_line[
                            0].product_template_id.product_variant_ids[0].injection_uv_printing_filename,
                        'file': order_sudo.order_line[0].product_template_id.product_variant_ids[0].injection_uv_printing_file,
                        'title': 'Uv Printing File',
                        'field_name': 'injection_uv_printing_file'

                    })

                if order_sudo.order_line[0].product_template_id.product_variant_ids[0].metal_feb_uv_printing_file:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_tmp_id, 'metal_feb_uv_printing_file',
                        file_service.order_line[0].product_template_id.product_variant_ids[0].metal_feb_uv_printing_filename,
                        'download=true')
                    service_file.append({
                        'download_url': download_url,
                        'name': order_sudo.order_line[
                            0].product_template_id.product_variant_ids[0].metal_feb_uv_printing_filename,
                        'file': order_sudo.order_line[0].product_template_id.product_variant_ids[0].metal_feb_uv_printing_file,
                        'title': 'Uv Printing',
                        'field_name': 'metal_feb_uv_printing_file'

                    })
                if order_sudo.order_line[0].product_template_id.product_variant_ids[0].metal_feb_technical_drawings:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_tmp_id, 'metal_feb_technical_drawings',
                        file_service.order_line[0].product_template_id.product_variant_ids[0].metal_feb_technical_drawings_filename,
                        'download=true')
                    service_file.append({
                        'download_url': download_url,
                        'name': order_sudo.order_line[
                            0].product_template_id.product_variant_ids[0].metal_feb_technical_drawings_filename,
                        'file': order_sudo.order_line[0].product_template_id.product_variant_ids[0].metal_feb_technical_drawings,
                        'title': 'Upload Technical Drawing',
                        'field_name': 'metal_feb_technical_drawings'

                    })
                if order_sudo.order_line[0].product_template_id.product_variant_ids[0].enclosure_design_product_file:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_tmp_id, 'enclosure_design_product_file',
                        file_service.order_line[0].product_template_id.product_variant_ids[0].enclosure_design_product_filename,
                        'download=true')
                    service_file.append({
                        'download_url': download_url,
                        'name': order_sudo.order_line[
                            0].product_template_id.product_variant_ids[0].enclosure_design_product_filename,
                        'file': order_sudo.order_line[0].product_template_id.product_variant_ids[0].enclosure_design_product_file,
                        'title': 'Files',
                        'field_name': 'enclosure_design_product_file'

                    })
                if order_sudo.order_line[0].product_template_id.product_variant_ids[0].fdm_technical_drawings:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_tmp_id, 'fdm_technical_drawings',
                        file_service.order_line[0].product_template_id.product_variant_ids[0].fdm_technical_drawings_filename,
                        'download=true')
                    service_file.append({
                        'download_url': download_url,
                        'name': order_sudo.order_line[
                            0].product_template_id.product_variant_ids[0].fdm_technical_drawings_filename,
                        'file': order_sudo.order_line[0].product_template_id.product_variant_ids[0].fdm_technical_drawings,
                        'title': 'Upload Technical Drawing',
                        'field_name': 'fdm_technical_drawings'

                    })
                if order_sudo.order_line[0].product_template_id.product_variant_ids[0].fdm_uv_printing_file:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_tmp_id, 'fdm_uv_printing_file',
                        file_service.order_line[0].product_template_id.product_variant_ids[0].fdm_uv_printing_filename,
                        'download=true')
                    service_file.append({
                        'download_url': download_url,
                        'name': order_sudo.order_line[
                            0].product_template_id.product_variant_ids[0].fdm_uv_printing_filename,
                        'file': order_sudo.order_line[0].product_template_id.product_variant_ids[0].fdm_uv_printing_file,
                        'title': 'Uv Printing File',
                        'field_name': 'fdm_uv_printing_file'

                    })
                if order_sudo.order_line[0].product_template_id.product_variant_ids[0].projection_technical_drawings:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_tmp_id, 'projection_technical_drawings',
                        file_service.order_line[0].product_template_id.product_variant_ids[0].projection_technical_drawings_filename,
                        'download=true')
                    service_file.append({
                        'download_url': download_url,
                        'name': order_sudo.order_line[
                            0].product_template_id.product_variant_ids[0].projection_technical_drawings_filename,
                        'file': order_sudo.order_line[0].product_template_id.product_variant_ids[0].projection_technical_drawings,
                        'title': 'Upload Technical Drawing',
                        'field_name': 'projection_technical_drawings'

                    })
                if order_sudo.order_line[0].product_template_id.product_variant_ids[0].projection_uv_printing_file:
                    download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                        product_tmp_id, 'projection_uv_printing_file',
                        file_service.order_line[0].product_template_id.product_variant_ids[0].projection_uv_printing_filename,
                        'download=true')
                    service_file.append({
                        'download_url': download_url,
                        'name': order_sudo.order_line[
                            0].product_template_id.product_variant_ids[0].projection_uv_printing_filename,
                        'file': order_sudo.order_line[0].product_template_id.product_variant_ids[0].projection_uv_printing_file,
                        'title': 'Uv Printing File',
                        'field_name': 'projection_uv_printing_file'

                    })
        values['service_file'] = service_file

        return request.render('cr_web_portal.inquiry_quotation_portal_template', values)


    @http.route(['/redirect/questions/form'], type='http', auth="user", website=True)
    def create_new_service_request(self, **kw):
        service = kw.get('service')
        if service == 'enclosure_design':
            return request.render('cr_web_portal.enclosure_design_service_questions')
        elif service == 'fdm_modeling':
            return request.render('cr_web_portal.fdm_printing_service_questions')
        elif service == 'projection_printing':
            return request.render('cr_web_portal.projection_printing_service_questions')
        elif service == 'sheet_metal_fabrication':
            return request.render('cr_web_portal.sheet_metal_fabrication_service_questions')
        elif service == 'cnc_machining':
            return request.render('cr_web_portal.cnc_machining_service_questions')
        elif service == 'injection_molding':
            return request.render('cr_web_portal.injection_molding_service_questions')
        else:
            return request.redirect('/my')

    @http.route(['/my/orders/<int:order_id>'], type='http', auth="public", website=True)
    def portal_order_page(self, order_id, report_type=None, access_token=None, message=False, download=False, **kw):
        try:
            order_sudo = self._document_check_access('sale.order', order_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('html', 'pdf', 'text'):
            if order_sudo.state == 'sale':
                return self._show_report(model=order_sudo, report_type=report_type,
                                         report_ref='sale.action_report_pro_forma_invoice', download=download)
            else:
                return self._show_report(model=order_sudo, report_type=report_type,
                                         report_ref='sale.action_report_saleorder', download=download)
        if request.env.user.share and access_token:
            # If a public/portal user accesses the order with the access token
            # Log a note on the chatter.
            today = fields.Date.today().isoformat()
            session_obj_date = request.session.get('view_quote_%s' % order_sudo.id)
            if session_obj_date != today:
                # store the date as a string in the session to allow serialization
                request.session['view_quote_%s' % order_sudo.id] = today
                # The "Quotation viewed by customer" log note is an information
                # dedicated to the salesman and shouldn't be translated in the customer/website lgg
                context = {'lang': order_sudo.user_id.partner_id.lang or order_sudo.company_id.partner_id.lang}
                if order_sudo.state == 'sent':
                    msg = _('Quotation viewed by customer %s',
                            order_sudo.partner_id.name if request.env.user._is_public() else request.env.user.partner_id.name)
                elif order_sudo.state in ['sale', 'done']:
                    msg = _('Sales Order viewed by customer %s',
                            order_sudo.partner_id.name if request.env.user._is_public() else request.env.user.partner_id.name)
                else:
                    msg = _('Inquiry viewed by customer %s',
                            order_sudo.partner_id.name if request.env.user._is_public() else request.env.user.partner_id.name)
                del context
                _message_post_helper(
                    "sale.order",
                    order_sudo.id,
                    message=msg,
                    token=order_sudo.access_token,
                    message_type="notification",
                    subtype_xmlid="mail.mt_note",
                    partner_ids=order_sudo.user_id.sudo().partner_id.ids,
                )

        backend_url = f'/web#model={order_sudo._name}' \
                      f'&id={order_sudo.id}' \
                      f'&action={order_sudo._get_portal_return_action().id}' \
                      f'&view_type=form'
        sim_files = []
        extra_info = []
        service_file = []
        for ord in order_sudo:
            if ord.order_line and ord.order_line[0].product_id:
                product_id = ord.order_line[0].product_template_id.product_variant_ids[0]
                if product_id and not product_id.is_service:
                    if product_id.pdf_file:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_id.id, 'pdf_file', product_id.pdf_file_name, 'download=true')
                        sim_files.append({
                            'download_url': download_url,
                            'name': product_id.pdf_file_name,
                            'file': product_id.pdf_file,
                            'title': 'Data Sheet',
                            'field_name':'pdf_file',
                        })
                    if product_id.drawing_fcstd_file:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_id.id, 'doc_file', product_id.drawing_fcstd_file_name, 'download=true')
                        sim_files.append({
                            'download_url': download_url,
                            'name': product_id.drawing_fcstd_file_name,
                            'file': product_id.drawing_fcstd_file,
                            'title': 'PCB Outline',
                            'field_name':'doc_file',
                        })
                if product_id and product_id.is_customisable:
                    if product_id.x_studio_exception_file:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_id.id, 'x_studio_exception_file', product_id.exception_file_name, 'download=true')
                        sim_files.append({
                            'download_url': download_url,
                            'name': product_id.exception_file_name,
                            'file': product_id.x_studio_exception_file,
                            'title': 'Technical Query',
                            'field_name': 'x_studio_exception_file',
                        })
                    if product_id.x_studio_exception_reply_file:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_id.id, 'x_studio_exception_reply_file', product_id.exception_reply_file_name,
                            'download=true')
                        sim_files.append({
                            'download_url': download_url,
                            'name': product_id.exception_reply_file_name,
                            'file': product_id.x_studio_exception_reply_file,
                            'title': 'Technical Query Response',
                            'field_name': 'x_studio_exception_reply_file',
                        })
                    if product_id.technical_drawing_file:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_id.id, 'technical_drawing_file', product_id.technical_drawing_file_name,
                            'download=true')
                        extra_info.append({
                            'download_url': download_url,
                            'name': product_id.technical_drawing_file_name,
                            'file': product_id.technical_drawing_file,
                            'title': 'Technical Drawing File',
                            'field_name': 'technical_drawing_file',
                        })
                    if product_id.uv_printing_file:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_id.id, 'uv_printing_file', product_id.uv_printing_file_name,
                            'download=true')
                        extra_info.append({
                            'download_url': download_url,
                            'name': product_id.uv_printing_file_name,
                            'file': product_id.uv_printing_file,
                            'title': 'Uv Printing File',
                            'field_name': 'uv_printing_file',
                        })
                    if product_id.additional_notes:
                        extra_info.append({
                            'note': product_id.additional_notes,
                            'title': 'Additional Notes',
                            'type': 'note',
                        })

                if product_id and product_id.is_service:
                    product_tmp_id = ord.order_line[0].product_template_id.product_variant_ids[0].id
                    if ord.order_line[0].product_template_id.product_variant_ids[0].cnc_machining_upload_technical_drawing:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_tmp_id, 'cnc_machining_upload_technical_drawing',
                            ord.order_line[
                                0].product_template_id.product_variant_ids[0].cnc_machining_upload_technical_drawing_filename,
                            'download=true')
                        service_file.append({
                            'download_url': download_url,
                            'name': ord.order_line[
                                0].product_template_id.product_variant_ids[0].cnc_machining_upload_technical_drawing_filename,
                            'file': ord.order_line[0].product_template_id.product_variant_ids[0].cnc_machining_upload_technical_drawing,
                            'title': 'Technical Drawing File',
                            'field_name': 'cnc_machining_upload_technical_drawing',
                        })
                    if ord.order_line[0].product_template_id.product_variant_ids[0].cnc_uv_printing_file:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_tmp_id, 'cnc_uv_printing_file',
                            ord.order_line[0].product_template_id.product_variant_ids[0].cnc_uv_printing_filename,
                            'download=true')
                        service_file.append({
                            'download_url': download_url,
                            'name': ord.order_line[0].product_template_id.product_variant_ids[0].cnc_uv_printing_filename,
                            'file': ord.order_line[0].product_template_id.product_variant_ids[0].cnc_uv_printing_file,
                            'title': 'Uv Printing File',
                            'field_name': 'cnc_uv_printing_file',
                        })
                    if ord.order_line[0].product_template_id.product_variant_ids[0]:
                        if ord.order_line[0].product_template_id.product_variant_ids[0].x_studio_exception_file:
                            download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                                product_tmp_id, 'x_studio_exception_file',
                                ord.order_line[0].product_template_id.product_variant_ids[
                                    0].exception_file_name,
                                'download=true')
                            service_file.append({
                                'download_url': download_url,
                                'name': ord.order_line[
                                    0].product_template_id.product_variant_ids[0].exception_file_name,
                                'file': ord.order_line[0].product_template_id.product_variant_ids[
                                    0].x_studio_exception_file,
                                'title': 'Technical query',
                                'field_name': 'x_studio_exception_file',
                            })

                    if ord.order_line[0].product_template_id.product_variant_ids[
                        0].x_studio_exception_reply_file:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_tmp_id, 'x_studio_exception_reply_file',
                            ord.order_line[0].product_template_id.product_variant_ids[
                                0].exception_reply_file_name,
                            'download=true')
                        service_file.append({
                            'download_url': download_url,
                            'name': ord.order_line[
                                0].product_template_id.product_variant_ids[0].exception_reply_file_name,
                            'file': order_sudo.order_line[0].product_template_id.product_variant_ids[
                                0].x_studio_exception_reply_file,
                            'title': 'Technical query response',
                            'field_name': 'x_studio_exception_reply_file',
                        })

                    if ord.order_line[0].product_template_id.product_variant_ids[0].injection_mold_upload_technical_drawing:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_tmp_id, 'injection_mold_upload_technical_drawing_filename',
                            ord.order_line[
                                0].product_template_id.product_variant_ids[0].injection_mold_upload_technical_drawing_filename,
                            'download=true')
                        service_file.append({
                            'download_url': download_url,
                            'name': ord.order_line[
                                0].product_template_id.product_variant_ids[0].injection_mold_upload_technical_drawing_filename,
                            'file': ord.order_line[
                                0].product_template_id.product_variant_ids[0].injection_mold_upload_technical_drawing,
                            'title': 'Upload Technical Drawing',
                            'field_name': 'x_studio_exception_reply_file',
                        })
                    if ord.order_line[0].product_template_id.product_variant_ids[0].injection_uv_printing_file:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_tmp_id, 'injection_uv_printing_file',
                            ord.order_line[0].product_template_id.injection_uv_printing_filename,
                            'download=true')
                        service_file.append({
                            'download_url': download_url,
                            'name': ord.order_line[
                                0].product_template_id.product_variant_ids[0].injection_uv_printing_filename,
                            'file': ord.order_line[0].product_template_id.product_variant_ids[0].injection_uv_printing_file,
                            'title': 'Uv Printing File',
                            'field_name': 'injection_uv_printing_file',
                        })

                    if ord.order_line[0].product_template_id.product_variant_ids[0].metal_feb_uv_printing_file:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_tmp_id, 'metal_feb_uv_printing_file',
                            ord.order_line[0].product_template_id.product_variant_ids[0].metal_feb_uv_printing_filename,
                            'download=true')
                        service_file.append({
                            'download_url': download_url,
                            'name': ord.order_line[
                                0].product_template_id.product_variant_ids[0].metal_feb_uv_printing_filename,
                            'file': ord.order_line[0].product_template_id.product_variant_ids[0].metal_feb_uv_printing_file,
                            'title': 'Uv Printing',
                            'field_name': 'metal_feb_uv_printing_file',
                        })
                    if ord.order_line[0].product_template_id.product_variant_ids[0].metal_feb_technical_drawings:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_tmp_id, 'metal_feb_technical_drawings',
                            ord.order_line[0].product_template_id.product_variant_ids[0].metal_feb_technical_drawings_filename,
                            'download=true')
                        service_file.append({
                            'download_url': download_url,
                            'name': ord.order_line[
                                0].product_template_id.product_variant_ids[0].metal_feb_technical_drawings_filename,
                            'file': ord.order_line[0].product_template_id.product_variant_ids[0].metal_feb_technical_drawings,
                            'title': 'Upload Technical Drawing',
                            'field_name': 'metal_feb_technical_drawings',
                        })
                    if ord.order_line[0].product_template_id.product_variant_ids[0].enclosure_design_product_file:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_tmp_id, 'enclosure_design_product_file',
                            ord.order_line[0].product_template_id.product_variant_ids[0].enclosure_design_product_filename,
                            'download=true')
                        service_file.append({
                            'download_url': download_url,
                            'name': ord.order_line[
                                0].product_template_id.product_variant_ids[0].enclosure_design_product_filename,
                            'file': ord.order_line[0].product_template_id.product_variant_ids[0].enclosure_design_product_file,
                            'title': 'Files',
                            'field_name': 'enclosure_design_product_file',
                        })
                    if ord.order_line[0].product_template_id.product_variant_ids[0].fdm_technical_drawings:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_tmp_id, 'fdm_technical_drawings',
                            ord.order_line[0].product_template_id.product_variant_ids[0].fdm_technical_drawings_filename,
                            'download=true')
                        service_file.append({
                            'download_url': download_url,
                            'name': ord.order_line[
                                0].product_template_id.product_variant_ids[0].fdm_technical_drawings_filename,
                            'file': ord.order_line[0].product_template_id.product_variant_ids[0].fdm_technical_drawings,
                            'title': 'Upload Technical Drawing',
                            'field_name': 'fdm_technical_drawings',
                        })
                    if ord.order_line[0].product_template_id.product_variant_ids[0].fdm_uv_printing_file:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_tmp_id, 'fdm_uv_printing_file',
                            ord.order_line[0].product_template_id.product_variant_ids[0].fdm_uv_printing_filename,
                            'download=true')
                        service_file.append({
                            'download_url': download_url,
                            'name': ord.order_line[
                                0].product_template_id.product_variant_ids[0].fdm_uv_printing_filename,
                            'file': ord.order_line[0].product_template_id.product_variant_ids[0].fdm_uv_printing_file,
                            'title': 'Uv Printing File',
                            'field_name': 'fdm_uv_printing_file',
                        })
                    if ord.order_line[0].product_template_id.product_variant_ids[0].projection_technical_drawings:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_tmp_id, 'projection_technical_drawings',
                            ord.order_line[0].product_template_id.product_variant_ids[0].projection_technical_drawings_filename,
                            'download=true')
                        service_file.append({
                            'download_url': download_url,
                            'name': ord.order_line[
                                0].product_template_id.product_variant_ids[0].projection_technical_drawings_filename,
                            'file': ord.order_line[0].product_template_id.product_variant_ids[0].projection_technical_drawings,
                            'title': 'Upload Technical Drawing',
                            'field_name': 'projection_technical_drawings',
                        })
                    if ord.order_line[0].product_template_id.product_variant_ids[0].projection_uv_printing_file:
                        download_url = '/web/content/product.product/%s/%s/%s?%s' % (
                            product_tmp_id, 'projection_uv_printing_file',
                            ord.order_line[0].product_template_id.product_variant_ids[0].projection_uv_printing_filename,
                            'download=true')
                        service_file.append({
                            'download_url': download_url,
                            'name': ord.order_line[
                                0].product_template_id.product_variant_ids[0].projection_uv_printing_filename,
                            'file': ord.order_line[0].product_template_id.product_variant_ids[0].projection_uv_printing_file,
                            'title': 'Uv Printing File',
                            'field_name': 'projection_uv_printing_file',
                        })

        values = {
            'sale_order': order_sudo,
            'message': message,
            'report_type': 'html',
            'file_value_custom':sim_files,
            'extra_info_file':extra_info,
            'service_file':service_file,
            'backend_url': backend_url,
            'res_company': order_sudo.company_id,  # Used to display correct company logo
        }
        order_pp = {}

        if order_sudo.payment_term_id.is_advance_payment:
            payable_amount = order_sudo.get_payable_amount()
            if order_sudo.id not in order_pp:
                order_pp[order_sudo.id] = {}
            order_pp[order_sudo.id].update({'payable_amount': payable_amount})

        values.update({'order_pp': order_pp})
        values.update(self._get_payment_values(order_sudo))
        if values.get('providers'):
            values['providers'] = values.get('providers').filtered(lambda x: x.code != 'custom')
        if order_sudo.state in ('draft', 'sent', 'cancel'):
            history_session_key = 'my_quotations_history'
        else:
            history_session_key = 'my_orders_history'

        values = self._get_page_view_values(
            order_sudo, access_token, values, history_session_key, False)
        return request.render('sale.sale_order_portal_template', values)

    @http.route(['/my/orders', '/my/orders/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_orders(self, **kwargs):
        values = self._prepare_sale_portal_rendering_values(quotation_page=False, **kwargs)
        order_pp = {}
        for rec in values.get('orders'):
            order_pp[rec.id] = self._get_payment_values(rec)
            if rec.payment_term_id.is_advance_payment:
                payable_amount = rec.get_payable_amount()
                order_pp[rec.id].update({'payable_amount': payable_amount})
            if not rec.payment_term_id.is_advance_payment and order_pp[rec.id].get('providers'):
                order_pp[rec.id]['providers'] = order_pp[rec.id].get('providers').filtered(lambda x: x.code != 'custom')
        values.update({'order_pp': order_pp})
        request.session['my_orders_history'] = values['orders'].ids[:100]
        return request.render("sale.portal_my_orders", values)

    @http.route(['/my/quotes', '/my/quotes/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_quotes(self, **kwargs):
        values = self._prepare_sale_portal_rendering_values(quotation_page=True, **kwargs)
        order_pp = {}
        for rec in values.get('quotations'):
            order_pp[rec.id] = self._get_payment_values(rec)
            if rec.payment_term_id.is_advance_payment:
                payable_amount = rec.get_payable_amount()
                order_pp[rec.id].update({'payable_amount': payable_amount})
        values.update({'order_pp': order_pp})
        request.session['my_quotations_history'] = values['quotations'].ids[:100]
        return request.render("sale.portal_my_quotations", values)

    @http.route(['/my/invoices', '/my/invoices/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_invoices(self, page=1, date_begin=None, date_end=None, sortby=None, filterby=None, **kw):
        values = self._prepare_my_invoices_values(page, date_begin, date_end, sortby, filterby)

        # pager
        pager = portal_pager(**values['pager'])

        # content according to pager and archive selected
        invoices = values['invoices'](pager['offset'])
        request.session['my_invoices_history'] = invoices.ids[:100]
        order_pp = {}
        for rec in invoices:
            access_token = rec.access_token
            order_pp[rec.id] = self._invoice_get_page_view_values(rec, access_token)
        values.update({'order_pp': order_pp})
        values.update({
            'invoices': invoices,
            'pager': pager,
        })
        return request.render("account.portal_my_invoices", values)

    @http.route(['/my/orders/<int:order_id>/accept'], type='json', auth="public", website=True)
    def portal_quote_accept(self, order_id, access_token=None, name=None, signature=None,po_url = None,po_file_name=None,po_file_no=None):
        # get from query string if not on json param
        access_token = access_token or request.httprequest.args.get('access_token')
        if po_url != False:
            po_url = po_url.split(',')
            try:
                order_sudo = self._document_check_access('sale.order', order_id, access_token=access_token)
            except (AccessError, MissingError):
                return {'error': _('Invalid order.')}
            if order_sudo and order_sudo.payment_term_id and order_sudo.payment_term_id.is_advance_payment:
                if not signature:
                    return {'error': _('Signature is missing.')}

                try:
                    order_sudo.write({
                        'signed_by': name,
                        'signed_on': fields.Datetime.now(),
                        'signature': signature,
                    })
                    order_sudo.sudo().write({'x_studio_purchase_order_copy_filename':po_file_name})
                    order_sudo.sudo().write({'client_order_ref':po_file_no})
                    ff = request.env['ir.attachment'].sudo().create({
                        'name': po_file_name,
                        'res_model': 'sale.order',
                        'res_id': order_sudo.id,
                        'res_field': 'x_studio_purchase_order_copy',
                        'datas': po_url[1]
                    })
                    request.env.cr.commit()
                except (TypeError, binascii.Error) as e:
                    return {'error': _('Invalid signature data.')}

                _message_post_helper(
                    'sale.order',
                    order_sudo.id,
                    _('Order signed by %s', name),
                    attachments=[],
                    token=access_token,
                )

                return {
                    'force_refresh': True,
                    'redirect_url': '',
                }
            else:
                if not order_sudo._has_to_be_signed():
                    return {'error': _('The order is not in a state requiring customer signature.')}
                if not signature:
                    return {'error': _('Signature is missing.')}
                try:
                    order_sudo.write({
                        'signed_by': name,
                        'signed_on': fields.Datetime.now(),
                        'signature': signature,
                    })
                    order_sudo.sudo().write({'x_studio_purchase_order_copy_filename': po_file_name})
                    order_sudo.sudo().write({'client_order_ref': po_file_no})
                    dd = request.env['ir.attachment'].sudo().create({
                        'name': po_file_name,
                        'res_model': 'sale.order',
                        'res_id': order_sudo.id,
                        'res_field': 'x_studio_purchase_order_copy',
                        'datas': po_url[1]
                    })
                    request.env.cr.commit()
                except (TypeError, binascii.Error) as e:
                    return {'error': _('Invalid signature data.')}

                if not order_sudo._has_to_be_paid():
                    order_sudo.with_context(portal_order=True).action_confirm()
                    order_sudo._send_order_confirmation_mail()

                pdf = \
                request.env['ir.actions.report'].sudo()._render_qweb_pdf('sale.action_report_saleorder', [order_sudo.id])[
                    0]

                _message_post_helper(
                    'sale.order',
                    order_sudo.id,
                    _('Order signed by %s', name),
                    attachments=[('%s.pdf' % order_sudo.name, pdf)],
                    token=access_token,
                )

                query_string = '&message=sign_ok'
                if order_sudo._has_to_be_paid(True):
                    query_string += '#allow_payment=yes'
                return {
                    'force_refresh': True,
                    'redirect_url': order_sudo.get_portal_url(query_string=query_string),
                }

        else:
            try:
                order_sudo = self._document_check_access('sale.order', order_id, access_token=access_token)
            except (AccessError, MissingError):
                return {'error': _('Invalid order.')}
            if order_sudo and order_sudo.payment_term_id and order_sudo.payment_term_id.is_advance_payment:
                if not signature:
                    return {'error': _('Signature is missing.')}

                try:
                    order_sudo.write({
                        'signed_by': name,
                        'signed_on': fields.Datetime.now(),
                        'signature': signature,
                    })
                    request.env.cr.commit()
                except (TypeError, binascii.Error) as e:
                    return {'error': _('Invalid signature data.')}

                _message_post_helper(
                    'sale.order',
                    order_sudo.id,
                    _('Order signed by %s', name),
                    attachments=[],
                    token=access_token,
                )

                return {
                    'force_refresh': True,
                    'redirect_url': '',
                }
            else:
                if not order_sudo._has_to_be_signed():
                    return {'error': _('The order is not in a state requiring customer signature.')}
                if not signature:
                    return {'error': _('Signature is missing.')}
                try:
                    order_sudo.write({
                        'signed_by': name,
                        'signed_on': fields.Datetime.now(),
                        'signature': signature,
                    })
                    request.env.cr.commit()
                except (TypeError, binascii.Error) as e:
                    return {'error': _('Invalid signature data.')}

                if not order_sudo._has_to_be_paid():
                    order_sudo.with_context(portal_order=True).action_confirm()
                    order_sudo._send_order_confirmation_mail()

                pdf = \
                request.env['ir.actions.report'].sudo()._render_qweb_pdf('sale.action_report_saleorder', [order_sudo.id])[
                    0]

                _message_post_helper(
                    'sale.order',
                    order_sudo.id,
                    _('Order signed by %s', name),
                    attachments=[('%s.pdf' % order_sudo.name, pdf)],
                    token=access_token,
                )

                query_string = '&message=sign_ok'
                if order_sudo._has_to_be_paid(True):
                    query_string += '#allow_payment=yes'
                return {
                    'force_refresh': True,
                    'redirect_url': order_sudo.get_portal_url(query_string=query_string),
                }


    @http.route(['/order/invoices/<int:order_id>'],type='http', auth="user", website=True)
    def portal_order_invocies(self, order_id):
        values = {}
        order_id = request.env['sale.order'].sudo().browse(int(order_id))
        values.update({
            'invoices': order_id.invoice_ids,
        })
        return request.render("account.portal_my_invoices", values)

    @http.route(['/filter_industry'], type='json', auth="public", website=True)
    def filter_state(self, main_category, **kw):
        industry_id = request.env['industry.segment'].sudo().search([('main_category.id', '=', main_category)])
        if industry_id.sub_category:
            category_list = []
            for category in industry_id.sub_category:
                category_list.append((category.id, category.name))
            return dict(
                states=category_list,
            )
        return dict(states=[])

    @http.route(['/create/ticket'], type='http', auth="user", website=True)
    def portal_create_ticket(self, **kw):
        vals = {
            'name': kw.get('subject') or '',
            'ticket_type_id': int(kw.get('type_id')) or False,
            'description': kw.get('message') or '',
            'team_id': request.env['helpdesk.team'].sudo().search([], limit=1).id or False,
            'partner_id': request.env.user.partner_id.id or False,
            # 'email': request.env.user.partner_id.email or '',
            # 'phone': request.env.user.partner_id.phone or '',
        }
        ticket_id = request.env['helpdesk.ticket'].sudo().create(vals)
        if ticket_id:
            file = kw.get('attachment')
            request.env['ir.attachment'].sudo().create({
                'name': file.filename,
                'res_model': 'helpdesk.ticket',
                'res_id': ticket_id.id,
                'datas': base64.b64encode(file.read())
            })
        return request.redirect('/my/messages')
