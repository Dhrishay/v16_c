# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from lxml import etree
from lxml.html import builder as html

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class Invite(models.TransientModel):
    _inherit = 'mail.wizard.invite'

    @api.model
    def default_get(self, fields):
        result = super(Invite, self).default_get(fields)
        if 'message' not in fields:
            return result

        user_name = self.env.user.display_name
        model = result.get('res_model')
        res_id = result.get('res_id')
        if model and res_id:
            document = self.env['ir.model']._get(model).display_name
            title = self.env[model].browse(res_id).display_name
            if model == 'sale.order' and title:
                so_id = self.env[model].browse(res_id)
                if so_id and so_id.state not in ['sale', 'done']:
                    msg_fmt = _('%(user_name)s invited you to follow Sales Inquiry document: %(title)s')
                else:
                    msg_fmt = _('%(user_name)s invited you to follow %(document)s document: %(title)s')
            else:
                msg_fmt = _('%(user_name)s invited you to follow %(document)s document: %(title)s')
        else:
            msg_fmt = _('%(user_name)s invited you to follow a new document.')

        text = msg_fmt % locals()
        message = html.DIV(
            html.P(_('Hello,')),
            html.P(text)
        )
        result['message'] = etree.tostring(message)
        return result

    def _prepare_message_values(self, document, model_name, email_from):
        if document and document._name == 'sale.order' and document.state and document.state not in ['sale', 'done']:
            return {
                'subject': _('Invitation to follow Sales Inquiry: %(document_name)s', document_name=document.display_name),
                'body': self.message,
                'record_name': document.display_name,
                'email_from': email_from,
                'reply_to': email_from,
                'model': self.res_model,
                'res_id': self.res_id,
                'reply_to_force_new': True,
                'email_add_signature': True,
            }
        else:
            return {
                'subject': _('Invitation to follow %(document_model)s: %(document_name)s', document_model=model_name,
                             document_name=document.display_name),
                'body': self.message,
                'record_name': document.display_name,
                'email_from': email_from,
                'reply_to': email_from,
                'model': self.res_model,
                'res_id': self.res_id,
                'reply_to_force_new': True,
                'email_add_signature': True,
            }
