# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, tools, SUPERUSER_ID, registry
import uuid
import logging
from odoo.tools.misc import clean_context, split_every
import threading

_logger = logging.getLogger(__name__)

class Message(models.Model):
    _inherit = 'mail.message'

    @api.model
    def create(self, vals):
        if vals.get('model') and vals.get('model') == 'sale.order':
            if vals['body'] == 'Sales Order created':
                vals['body'] = 'Sales Inquiry created'
        res = super(Message, self).create(vals)
        helpdesk_ticket = 0
        if res.model and res.res_id and res.model == 'helpdesk.ticket' and res.subtype_id and res.subtype_id.id == self.env.ref('mail.mt_comment').id:
            helpdesk_ticket = self.env[res.model].browse(res.res_id)
            if helpdesk_ticket and res.author_id.active and helpdesk_ticket.stage_id.id in [
                self.env.ref('helpdesk.stage_cancelled').id, self.env.ref('helpdesk.stage_solved').id]:
                helpdesk_ticket.stage_id = self.env.ref('helpdesk.stage_in_progress').id
        return res


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _notify_thread_by_email(self, message, recipients_data, msg_vals=False,
                                mail_auto_delete=True,  # mail.mail
                                model_description=False, force_email_company=False, force_email_lang=False,  # rendering
                                resend_existing=False, force_send=True, send_after_commit=True,  # email send
                                subtitles=None, **kwargs):
        """ Method to send email linked to notified messages.

        :param message: ``mail.message`` record to notify;
        :param recipients_data: list of recipients information (based on res.partner
          records), formatted like
            [{'active': partner.active;
              'id': id of the res.partner being recipient to notify;
              'groups': res.group IDs if linked to a user;
              'notif': 'inbox', 'email', 'sms' (SMS App);
              'share': partner.partner_share;
              'type': 'customer', 'portal', 'user;'
             }, {...}].
          See ``MailThread._notify_get_recipients``;
        :param msg_vals: dictionary of values used to create the message. If given it
          may be used to access values related to ``message`` without accessing it
          directly. It lessens query count in some optimized use cases by avoiding
          access message content in db;

        :param mail_auto_delete: delete notification emails once sent;

        :param model_description: model description used in email notification process
          (computed if not given);
        :param force_email_company: see ``_notify_by_email_prepare_rendering_context``;
        :param force_email_lang: see ``_notify_by_email_prepare_rendering_context``;

        :param resend_existing: check for existing notifications to update based on
          mailed recipient, otherwise create new notifications;
        :param force_send: send emails directly instead of using queue;
        :param send_after_commit: if force_send, tells whether to send emails after
          the transaction has been committed using a post-commit hook;
        :param subtitles: optional list that will be set as template value "subtitles"
        """
        partners_data = [r for r in recipients_data if r['notif'] == 'email']
        if not partners_data:
            return True

        model = msg_vals.get('model') if msg_vals else message.model
        model_name = model_description or (self.env['ir.model']._get(model).display_name if model else False) # one query for display name
        recipients_groups_data = self._notify_get_recipients_classify(partners_data, model_name, msg_vals=msg_vals)

        if not recipients_groups_data:
            return True
        force_send = self.env.context.get('mail_notify_force_send', force_send)

        template_values = self._notify_by_email_prepare_rendering_context(
            message, msg_vals=msg_vals, model_description=model_description,
            force_email_company=force_email_company,
            force_email_lang=force_email_lang,
        ) # 10 queries
        if subtitles:
            template_values['subtitles'] = subtitles

        email_layout_xmlid = msg_vals.get('email_layout_xmlid') if msg_vals else message.email_layout_xmlid
        template_xmlid = email_layout_xmlid if email_layout_xmlid else 'mail.mail_notification_layout'
        base_mail_values = self._notify_by_email_get_base_mail_values(message, additional_values={'auto_delete': mail_auto_delete})

        # Clean the context to get rid of residual default_* keys that could cause issues during
        # the mail.mail creation.
        # Example: 'default_state' would refer to the default state of a previously created record
        # from another model that in turns triggers an assignation notification that ends up here.
        # This will lead to a traceback when trying to create a mail.mail with this state value that
        # doesn't exist.
        SafeMail = self.env['mail.mail'].sudo().with_context(clean_context(self._context))
        SafeNotification = self.env['mail.notification'].sudo().with_context(clean_context(self._context))
        emails = self.env['mail.mail'].sudo()

        # loop on groups (customer, portal, user,  ... + model specific like group_sale_salesman)
        notif_create_values = []
        recipients_max = 50
        for recipients_group_data in recipients_groups_data:
            # generate notification email content
            recipients_ids = recipients_group_data.pop('recipients')
            render_values = {**template_values, **recipients_group_data}
            # {company, is_discussion, lang, message, model_description, record, record_name, signature, subtype, tracking_values, website_url}
            # {actions, button_access, has_button_access, recipients}

            mail_body = self.env['ir.qweb']._render(template_xmlid, render_values, minimal_qcontext=True, raise_if_not_found=False, lang=template_values['lang'])
            if not mail_body:
                _logger.warning('QWeb template %s not found or is empty when sending notification emails. Sending without layouting.', template_xmlid)
                mail_body = message.body
            mail_body = self.env['mail.render.mixin']._replace_local_links(mail_body)

            # create email
            for recipients_ids_chunk in split_every(recipients_max, recipients_ids):
                mail_values = self._notify_by_email_get_final_mail_values(
                    recipients_ids_chunk,
                    base_mail_values,
                    additional_values={'body_html': mail_body}
                )
                new_email = SafeMail.create(mail_values)

                if new_email and recipients_ids_chunk:
                    tocreate_recipient_ids = list(recipients_ids_chunk)
                    if resend_existing:
                        existing_notifications = self.env['mail.notification'].sudo().search([
                            ('mail_message_id', '=', message.id),
                            ('notification_type', '=', 'email'),
                            ('res_partner_id', 'in', tocreate_recipient_ids)
                        ])
                        if existing_notifications:
                            tocreate_recipient_ids = [rid for rid in recipients_ids_chunk if rid not in existing_notifications.mapped('res_partner_id.id')]
                            existing_notifications.write({
                                'notification_status': 'ready',
                                'mail_mail_id': new_email.id,
                            })
                    notif_create_values += [{
                        'author_id': message.author_id.id,
                        'mail_message_id': message.id,
                        'res_partner_id': recipient_id,
                        'notification_type': 'email',
                        'mail_mail_id': new_email.id,
                        'is_read': True,  # discard Inbox notification
                        'notification_status': 'ready',
                    } for recipient_id in tocreate_recipient_ids + message.recipient_cc_ids.ids]
                emails += new_email

        if notif_create_values:
            SafeNotification.create(notif_create_values)

        # NOTE:
        #   1. for more than 50 followers, use the queue system
        #   2. do not send emails immediately if the registry is not loaded,
        #      to prevent sending email during a simple update of the database
        #      using the command-line.
        test_mode = getattr(threading.current_thread(), 'testing', False)
        if force_send and len(emails) < recipients_max and (not self.pool._init or test_mode):
            # unless asked specifically, send emails after the transaction to
            # avoid side effects due to emails being sent while the transaction fails
            if not test_mode and send_after_commit:
                email_ids = emails.ids
                dbname = self.env.cr.dbname
                _context = self._context

                @self.env.cr.postcommit.add
                def send_notifications():
                    db_registry = registry(dbname)
                    with db_registry.cursor() as cr:
                        env = api.Environment(cr, SUPERUSER_ID, _context)
                        env['mail.mail'].browse(email_ids).send()
            else:
                emails.send()

        return True

class MassMailingList(models.Model):
    _inherit = 'mailing.list'

    is_publish = fields.Boolean('Publish for Customer')