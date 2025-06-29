# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, http, SUPERUSER_ID, _
from odoo.exceptions import AccessError, MissingError, ValidationError
from odoo.addons.web.controllers.report import ReportController
from odoo.http import request
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers import portal
import json
import logging
import werkzeug.exceptions
from werkzeug.urls import url_parse
from odoo import http
from odoo.http import content_disposition, request
from odoo.tools.misc import html_escape
from odoo.tools.safe_eval import safe_eval, time

_logger = logging.getLogger(__name__)

from odoo.addons.web.controllers.home import Home

import logging
from odoo.addons.web.controllers.home import ensure_db, Home, SIGN_UP_REQUEST_PARAMS, LOGIN_SUCCESSFUL_PARAMS
from odoo.tools import OrderedSet, escape_psql, html_escape as escape

from odoo.exceptions import UserError
from textwrap import shorten
import odoo
import odoo.modules.registry
from odoo import http
from odoo.http import request
from odoo.tools.translate import _
import re

_logger = logging.getLogger(__name__)

class CustomerPortal(portal.CustomerPortal):

    @http.route(['/my/orders/<int:order_id>/decline'], type='http', auth="public", methods=['POST'], website=True)
    def portal_quote_decline(self, order_id, access_token=None, decline_message=None, **kwargs):
        portal_user_ids = request.env.ref('base.group_portal').sudo().users.ids
        internal_user_ids = request.env.ref('base.group_user').sudo().users.ids
        is_portal = request.env.user.id in portal_user_ids
        is_inernal = request.env.user.id in internal_user_ids
        try:
            order_sudo = self._document_check_access('sale.order', order_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if order_sudo._has_to_be_signed() and decline_message:
            order_sudo._action_cancel()

            if is_portal:
                order_sudo.sudo().write({'closed_by': 'customer'})
            elif is_inernal:
                order_sudo.sudo().write({'closed_by': 'user'})
            else:
                pass
            order_sudo.sale_close_reason_id = request.env.ref('mechpower_base_extended.reject_by_customer').id
            _message_post_helper(
                'sale.order',
                order_sudo.id,
                decline_message,
                token=access_token,
            )
            redirect_url = order_sudo.get_portal_url()
        else:
            redirect_url = order_sudo.get_portal_url(query_string="&message=cant_reject")

        return request.redirect(redirect_url)


class MechReportController(ReportController):
    @http.route(['/report/download'], type='http', auth="user")
    def report_download(self, data, context=None, token=None):  # pylint: disable=unused-argument
        """This function is used by 'action_manager_report.js' in order to trigger the download of
        a pdf/controller report.

        :param data: a javascript array JSON.stringified containg report internal url ([0]) and
        type [1]
        :returns: Response with an attachment header

        """
        requestcontent = json.loads(data)
        url, type_ = requestcontent[0], requestcontent[1]
        reportname = '???'
        try:
            if type_ in ['qweb-pdf', 'qweb-text']:
                converter = 'pdf' if type_ == 'qweb-pdf' else 'text'
                extension = 'pdf' if type_ == 'qweb-pdf' else 'txt'

                pattern = '/report/pdf/' if type_ == 'qweb-pdf' else '/report/text/'
                reportname = url.split(pattern)[1].split('?')[0]

                docids = None
                if '/' in reportname:
                    reportname, docids = reportname.split('/')

                if docids:
                    # Generic report:
                    response = self.report_routes(reportname, docids=docids, converter=converter, context=context)
                else:
                    # Particular report:
                    data = url_parse(url).decode_query(cls=dict)  # decoding the args represented in JSON
                    if 'context' in data:
                        context, data_context = json.loads(context or '{}'), json.loads(data.pop('context'))
                        context = json.dumps({**context, **data_context})
                    response = self.report_routes(reportname, converter=converter, context=context, **data)

                report = request.env['ir.actions.report']._get_report_from_name(reportname)
                filename = "%s.%s" % (report.model, docids)
                if docids:
                    ids = [int(x) for x in docids.split(",") if x.isdigit()]
                    obj = request.env[report.model].browse(ids)
                    if report.print_report_name and not len(obj) > 1:
                        report_name = safe_eval(report.print_report_name, {'object': obj, 'time': time})
                        filename = "%s.%s" % (report_name, extension)
                if report.model == 'sale.order' and docids:
                    order_id = request.env['sale.order'].sudo().search([('id', '=', int(docids))])
                    if order_id and order_id.amount_total == 0:
                        raise ValidationError(_('An Inquiry/Quotation cannot be generated with a total amount of 0.\nPlease ensure all items have a valid price before proceeding.'))
                    if reportname == 'sale.report_saleorder_pro_forma' and order_id and order_id.state not in ['sale', 'done']:
                        raise ValidationError(_('Pro-forma invoices cannot be generated while in the inquiry stage.'))

                response.headers.add('Content-Disposition', content_disposition(filename))
                return response
            else:
                return
        except Exception as e:
            _logger.exception("Error while generating report %s", reportname)
            se = http.serialize_exception(e)
            error = {
                'code': 200,
                'message': "Odoo Server Error",
                'data': se
            }
            res = request.make_response(html_escape(json.dumps(error)))
            raise werkzeug.exceptions.InternalServerError(response=res) from e
