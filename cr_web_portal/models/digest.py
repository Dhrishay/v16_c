# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, tools
from markupsafe import Markup
from datetime import datetime, date
from markupsafe import Markup
from werkzeug.urls import url_join
from odoo.exceptions import AccessError
from odoo.addons.base.models.ir_mail_server import MailDeliveryException
import logging
_logger = logging.getLogger(__name__)

class DigestDigest(models.Model):
    _inherit = 'digest.digest'

    kpi_res_users_registered = fields.Boolean(string='New Registered Users')
    kpi_res_users_registered_value = fields.Integer(string='New Registered Users Value',compute='_compute_kpi_res_users_registered_value')
    kpi_crm_opportunities_created = fields.Boolean(string='New Opportunities')
    kpi_crm_opportunities_created_value = fields.Integer(string='New Opportunities Value',compute='_compute_kpi_crm_opportunities_created_value')
    kpi_inquiry_created = fields.Boolean(string='New Inquiry')
    kpi_inquiry_created_value = fields.Integer(string='New Inquiry Value',compute='_compute_kpi_inquiry_created_value')
    kpi_offer_created = fields.Boolean(string='New Offers')
    kpi_offer_created_value = fields.Integer(string='New Offers Value',compute='_compute_kpi_offer_created_value')
    kpi_all_offer_total_amount = fields.Boolean('All Offer Total Amount')
    kpi_all_offer_total_amount_value = fields.Monetary(compute='_compute_kpi_all_offer_total_amount_value')
    kpi_sale_order_confirmed = fields.Boolean(string='Sale Order Confirmed')
    kpi_sale_order_confirmed_value = fields.Integer(string='Sale Order Confirmed Value',compute='_compute_kpi_sale_order_confirmed_value')
    kpi_sale_order_confirmed_amount = fields.Boolean(string='Total Sale Order Confirmed Amount')
    kpi_sale_order_confirmed_amount_value = fields.Monetary(compute='_compute_kpi_sale_order_confirmed_amount_value')
    kpi_sale_order_delivery_done = fields.Boolean(string='Sale Order Delivery Done')
    kpi_sale_order_delivery_done_value = fields.Integer(compute='_compute_kpi_sale_order_delivery_done_value')
    kpi_sale_order_delivery_done_amount = fields.Boolean(string='Total Sale Order Delivery Done Amount ')
    kpi_sale_order_delivery_done_amount_value = fields.Monetary(compute='_compute_kpi_sale_order_delivery_done_value')

    def _compute_kpis_actions(self, company, user):
        res = super(DigestDigest, self)._compute_kpis_actions(company, user)
        res['kpi_res_users_registered'] = 'base.action_res_users&menu_id=%s' % self.env.ref('base.menu_users').id
        res['kpi_crm_opportunities_created'] = 'crm.crm_lead_action_pipeline&menu_id=%s' % self.env.ref('crm.crm_menu_root').id
        res['kpi_inquiry_created'] = 'sale.action_quotations_with_onboarding&menu_id=%s' % self.env.ref('sale.sale_menu_root').id
        res['kpi_offer_created'] = 'sale.action_orders&menu_id=%s' % self.env.ref('sale.sale_menu_root').id
        res['kpi_all_offer_total_amount'] = 'sale.report_all_channels_sales_action&menu_id=%s' % self.env.ref('sale.sale_menu_root').id
        res['kpi_sale_order_delivery_done_amount'] = 'sale.report_all_channels_sales_action&menu_id=%s' % self.env.ref('sale.sale_menu_root').id
        res['kpi_sale_order_confirmed'] = 'sale.action_orders&menu_id=%s' % self.env.ref('sale.sale_menu_root').id
        res['kpi_sale_order_delivery_done'] = 'sale.action_orders&menu_id=%s' % self.env.ref('sale.sale_menu_root').id
        res['kpi_sale_order_confirmed_amount'] = 'sale.report_all_channels_sales_action&menu_id=%s' % self.env.ref('sale.sale_menu_root').id
        return res
    def _compute_kpi_sale_order_delivery_done_value(self):
        if not self.env.user.has_group('sales_team.group_sale_salesman_all_leads'):
            raise AccessError(_("Do not have access, skip this data for user's digest email"))
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            confirmed_so = self.env['sale.order'].sudo().search([
                ('state', 'in', ['sale','done']),
                ('company_id', '=', company.id)
            ])
            delivery_done = 0
            so_order_line_amount = 0.00
            if confirmed_so:
                for so in confirmed_so:
                    if so.picking_ids:
                        delivery_confirm = so.picking_ids
                        so_shouldbe_confirmed = False
                        for delivery in delivery_confirm:
                            if delivery.date_done:
                                if delivery.date_done >= datetime.strptime(start,'%Y-%m-%d %H:%M:%S') and delivery.date_done <= datetime.strptime(end,'%Y-%m-%d %H:%M:%S'):
                                    if not so_shouldbe_confirmed:
                                        so_shouldbe_confirmed = True
                                        delivery_lines = delivery.move_line_ids
                                        for delivery_line in delivery_lines:
                                            for line in so.order_line:
                                                if line.product_id.id == delivery_line.product_id.id:
                                                    if line.product_uom_qty > line.product_uom_qty - line.qty_delivered:
                                                        line_sub_total = line.price_unit * line.qty_delivered
                                                        so_order_line_amount = so_order_line_amount + line_sub_total
                        if so_shouldbe_confirmed:
                            delivery_done = delivery_done + 1
            record.kpi_sale_order_delivery_done_value = delivery_done
            record.kpi_sale_order_delivery_done_amount_value = so_order_line_amount
    def _compute_kpi_sale_order_confirmed_amount_value(self):
        if not self.env.user.has_group('sales_team.group_sale_salesman_all_leads'):
            raise AccessError(_("Do not have access, skip this data for user's digest email"))
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            new_so_confirm = self.env['sale.order'].search([
                ('confirm_order_date', '>=', start),
                ('confirm_order_date', '<=', end),
                ('state', 'in', ['sale','done']),
                ('company_id', '=', company.id)
            ])
            all_so_line_untaxed_amount = 0.00
            if new_so_confirm:
                for so in new_so_confirm:
                    for order_line in so.order_line:
                        if not order_line.is_delivery:
                            all_so_line_untaxed_amount = all_so_line_untaxed_amount + order_line.price_subtotal
                record.kpi_sale_order_confirmed_amount_value = all_so_line_untaxed_amount
            else:
                record.kpi_sale_order_confirmed_amount_value = all_so_line_untaxed_amount

    def _compute_kpi_sale_order_confirmed_value(self):
        if not self.env.user.has_group('sales_team.group_sale_salesman_all_leads'):
            raise AccessError(_("Do not have access, skip this data for user's digest email"))
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            new_so_confirm = self.env['sale.order'].search([
                ('confirm_order_date', '>=', start),
                ('confirm_order_date', '<=', end),
                ('state', 'in', ['sale','done']),
                ('company_id', '=', company.id)
            ])
            if new_so_confirm:
                record.kpi_sale_order_confirmed_value = len(new_so_confirm.ids) if len(new_so_confirm) > 1 else 1
            else:
                record.kpi_sale_order_confirmed_value = 0
    def _compute_kpi_all_offer_total_amount_value(self):
        if not self.env.user.has_group('sales_team.group_sale_salesman_all_leads'):
            raise AccessError(_("Do not have access, skip this data for user's digest email"))
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            all_offers = self.env['sale.order'].sudo().search([
                ('quotation_date', '>=', start),
                ('quotation_date', '<=', end),
                ('state', 'in', ['sent']),
                ('company_id', '=', company.id)])
            all_so_line_untaxed_amount = 0.00
            if all_offers:
                for offer in all_offers:
                    for order_line in offer.order_line:
                        if not order_line.is_delivery:
                            all_so_line_untaxed_amount = all_so_line_untaxed_amount + order_line.price_subtotal
                record.kpi_all_offer_total_amount_value = all_so_line_untaxed_amount
            else:
                record.kpi_all_offer_total_amount_value = all_so_line_untaxed_amount


    @api.model
    def _cron_send_daily_digest_email(self):
        digests = self.search([('next_run_date', '<=', fields.Date.today()), ('state', '=', 'activated'),('periodicity','=','daily')])
        for digest in digests:
            try:
                digest.action_send()
            except MailDeliveryException as e:
                _logger.warning(
                    'MailDeliveryException while sending digest %d. Digest is now scheduled for next cron update.',
                    digest.id)

    @api.model
    def _cron_send_digest_email(self):
        digests = self.search([('next_run_date', '<=', fields.Date.today()), ('state', '=', 'activated'),('periodicity','=','weekly')])
        for digest in digests:
            try:
                digest.action_send()
            except MailDeliveryException as e:
                _logger.warning(
                    'MailDeliveryException while sending digest %d. Digest is now scheduled for next cron update.',
                    digest.id)

    def _compute_kpi_offer_created_value(self):
        if not self.env.user.has_group('sales_team.group_sale_salesman_all_leads'):
            raise AccessError(_("Do not have access, skip this data for user's digest email"))
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            new_offer_created = self.env['sale.order'].search([
                ('create_date', '>=', start),
                ('create_date', '<=', end),
                ('state', 'in', ['sent']),
                ('company_id', '=', company.id)
            ])
            if new_offer_created:
                record.kpi_offer_created_value = len(new_offer_created.ids) if len(new_offer_created) > 1 else 1
            else:
                record.kpi_offer_created_value = 0

    def _compute_kpi_inquiry_created_value(self):
        if not self.env.user.has_group('sales_team.group_sale_salesman_all_leads'):
            raise AccessError(_("Do not have access, skip this data for user's digest email"))
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            new_inquiry_created = self.env['sale.order'].search([
                ('create_date', '>=', start),
                ('create_date', '<=', end),
                ('state', 'in', ['inquiry','engineering_review', 'prepared_for_pricing', 'data_feedback']),
                ('company_id', '=', company.id)
            ])
            if new_inquiry_created:
                record.kpi_inquiry_created_value = len(new_inquiry_created.ids) if len(new_inquiry_created) > 1 else 1
            else:
                record.kpi_inquiry_created_value = 0
    def _compute_kpi_res_users_registered_value(self):
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            user_connected = self.env['res.users'].search_count([('company_id', '=', company.id), ('create_date', '>=', start), ('create_date', '<=', end)])
            record.kpi_res_users_registered_value = user_connected

    def _compute_kpi_crm_opportunities_created_value(self):
        if not self.env.user.has_group('sales_team.group_sale_salesman'):
            raise AccessError(_("Do not have access, skip this data for user's digest email"))
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            opportunities_created = self.env['crm.lead'].search_count([
                ('type', '=', 'opportunity'),
                ('create_date', '>=', start),
                ('create_date', '<=', end),
                ('company_id', '=', company.id)
            ])
            if opportunities_created:
                record.kpi_crm_opportunities_created_value = opportunities_created if opportunities_created > 1 else 1
            else:
                record.kpi_crm_opportunities_created_value = 0
    def _compute_preferences(self, company, user):
        """ Give an optional text for preferences, like a shortcut for configuration.

        :return string: html to put in template
        """
        preferences = []
        if self._context.get('digest_slowdown'):
            _dummy, new_perioridicy_str = self._get_next_periodicity()
            preferences.append(
                _("We have noticed you did not connect these last few days. We have automatically switched your preference to %(new_perioridicy_str)s Digests.",
                  new_perioridicy_str=new_perioridicy_str)
            )
        elif self.periodicity == 'daily' and user.has_group('base.group_erp_manager'):
            preferences.append(Markup(
                '<p>%s<br /><a href="%s" target="_blank" style="color:#38ad3a; font-weight: bold;">%s</a></p>') % (
                                   _('Prefer a broader overview ?'),
                                   f'/digest/{self.id:d}/set_periodicity?periodicity=weekly',
                                   _('Switch to weekly Digests')
                               ))
        if user.has_group('base.group_erp_manager'):
            preferences.append(Markup(
                '<p>%s<br /><a href="%s" target="_blank" style="color:#38ad3a; font-weight: bold;">%s</a></p>') % (
                                   _('Want to customize this email?'),
                                   f'/web#view_type=form&model={self._name}&id={self.id:d}',
                                   _('Choose the metrics you care about')
                               ))

        return preferences

    def _action_send_to_user(self, user, tips_count=1, consume_tips=True):
        unsubscribe_token = self._get_unsubscribe_token(user.id)

        rendered_body = self.env['mail.render.mixin']._render_template(
            'digest.digest_mail_main',
            'digest.digest',
            self.ids,
            engine='qweb_view',
            add_context={
                'title': self.name,
                'top_button_label': _('Connect'),
                'top_button_url': self.get_base_url(),
                'company': user.company_id,
                'user': user,
                'unsubscribe_token': unsubscribe_token,
                'tips_count': tips_count,
                'formatted_date': datetime.today().strftime('%B %d, %Y'),
                'display_mobile_banner': True,
                'kpi_data': self._compute_kpis(user.company_id, user),
                'tips': self._compute_tips(user.company_id, user, tips_count=tips_count, consumed=consume_tips),
                'preferences': self._compute_preferences(user.company_id, user),
            },
            post_process=True,
            options={'preserve_comments': True}
        )[self.id]
        full_mail = self.env['mail.render.mixin']._render_encapsulate(
            'digest.digest_mail_layout',
            rendered_body,
            add_context={
                'company': user.company_id,
                'user': user,
            },
        )
        # create a mail_mail based on values, without attachments
        unsub_url = url_join(self.get_base_url(),
                             f'/digest/{self.id}/unsubscribe?token={unsubscribe_token}&user_id={user.id}&one_click=1')
        mail_values = {
            'auto_delete': True,
            'author_id': self.env.user.partner_id.id,
            'body_html': full_mail,
            'email_from': (
                self.company_id.partner_id.email_formatted
                or self.env.user.email_formatted
                or self.env.ref('base.user_root').email_formatted
            ),
            'email_to': user.email_formatted,
            # Add headers that allow the MUA to offer a one click button to unsubscribe (requires DKIM to work)
            'headers': {
                'List-Unsubscribe': f'<{unsub_url}>',
                'List-Unsubscribe-Post': 'List-Unsubscribe=One-Click',
                'X-Auto-Response-Suppress': 'OOF',  # avoid out-of-office replies from MS Exchange
            },
            'state': 'outgoing',
            'subject': '%s: %s' % (user.company_id.name, self.name),
        }
        self.env['mail.mail'].sudo().create(mail_values).send()
        return True




