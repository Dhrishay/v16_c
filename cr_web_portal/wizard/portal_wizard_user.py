

import logging

from odoo.tools.translate import _
from odoo.tools import email_normalize
from odoo.exceptions import UserError

from odoo import api, fields, models, Command


_logger = logging.getLogger(__name__)


class PortalWizardUser(models.TransientModel):
    _inherit = 'portal.wizard.user'

    # add
    def action_grant_access(self):

        self.ensure_one()
        self._assert_user_email_uniqueness()

        if self.is_portal or self.is_internal:
            raise UserError(_('The partner "%s" already has the portal access.', self.partner_id.name))

        group_portal = self.env.ref('base.group_portal')
        group_public = self.env.ref('base.group_public')

        self._update_partner_email()
        user_sudo = self.user_id.sudo()

        if not user_sudo:
            # create a user if necessary and make sure it is in the portal group
            company = self.partner_id.company_id or self.env.company
            user_sudo = self.sudo().with_company(company.id)._create_user()

        if not user_sudo.active or not self.is_portal:
            user_sudo.write({'active': True, 'groups_id': [(4, group_portal.id), (3, group_public.id)]})
            # prepare for the signup process
            user_sudo.partner_id.signup_prepare()

        if self.partner_id:
            incomplete_registration_tag_id = self.env.ref('cr_web_portal.incomplete_registration_tag').sudo()
            if incomplete_registration_tag_id:
                self.partner_id.category_id = [(4, incomplete_registration_tag_id.id)]

        self.with_context(active_test=True)._send_email()

        return self.action_refresh_modal()

    def action_revoke_access(self):
        """Remove the user of the partner from the portal group.

        If the user was only in the portal group, we archive it.
        """
        self.ensure_one()
        if not self.is_portal:
            raise UserError(_('The partner "%s" has no portal access or is internal.', self.partner_id.name))

        group_portal = self.env.ref('base.group_portal')
        group_public = self.env.ref('base.group_public')

        self._update_partner_email()

        # Remove the sign up token, so it can not be used
        self.partner_id.sudo().signup_token = False

        if self.partner_id:
            partner = self.partner_id
            incomplete_registration_tag_id = self.env.ref('cr_web_portal.incomplete_registration_tag').sudo()
            if partner and incomplete_registration_tag_id:
                partner.category_id = [(5,0, [incomplete_registration_tag_id.id])]

            mailing_contact_id = self.env["mailing.contact"].sudo().search([('email', '=', partner.email)], limit=1)
            mail_list_id = self.env.ref('mechpower_base_extended.never_connected_customer_mailing_list').sudo().id
            if mailing_contact_id and mail_list_id and mail_list_id in mailing_contact_id.list_ids.ids:
                mailing_contact_id.list_ids = [(3, mail_list_id)]

        user_sudo = self.user_id.sudo()

        # remove the user from the portal group
        if user_sudo and user_sudo.has_group('base.group_portal'):
            user_sudo.write({'groups_id': [(3, group_portal.id), (4, group_public.id)], 'active': False})

        return self.action_refresh_modal()