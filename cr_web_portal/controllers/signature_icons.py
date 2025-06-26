# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

try:
    from werkzeug.utils import send_file
except ImportError:
    from odoo.tools._vendor.send_file import send_file


try:
    from werkzeug.utils import send_file
except ImportError:
    from odoo.tools._vendor.send_file import send_file

from odoo import http, _
from odoo.exceptions import AccessError, UserError
from odoo.http import request, Response
from odoo.modules import get_resource_path
from odoo.tools import file_open, file_path, replace_exceptions
from odoo.tools.mimetypes import guess_mimetype
from odoo.tools.image import image_guess_size_from_field_name

class MechPowerWebSignatureIcons(http.Controller):

    # custom route for fetching signature icons image
    @http.route('/newsletter/<string:signature_image_name>', type='http', auth='public')
    def signature_icons_fetch(self,signature_image_name,xmlid=None, model='ir.attachment', id=None, field='raw', filename=None, filename_field='name', mimetype=None, unique=False, download=False, access_token=None, nocache=False):
        if signature_image_name:
            signature_record = request.env['signature.icons'].sudo().search([('img_file_name','=',signature_image_name)],limit=1)
            model = signature_record._name
            id = str(signature_record.id)
            field = 'signature_image'

            with replace_exceptions(UserError, by=request.not_found()):
                record = request.env['ir.binary']._find_record(xmlid, model, id and int(id), access_token)
                stream = request.env['ir.binary']._get_stream_from(record, field, filename, filename_field, mimetype)
            send_file_kwargs = {'as_attachment': download}
            if unique:
                send_file_kwargs['immutable'] = True
                send_file_kwargs['max_age'] = http.STATIC_CACHE_LONG
            if nocache:
                send_file_kwargs['max_age'] = None

            res = stream.get_response(**send_file_kwargs)

            res.headers['Content-Security-Policy'] = "default-src 'none'"

            return res
