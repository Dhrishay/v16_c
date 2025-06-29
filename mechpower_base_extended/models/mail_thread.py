# Copyright 2023 Camptocamp
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, _


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    def _notify_get_recipients_classify(self, recipient_data, model_name, msg_vals=None):
        """ Classify recipients to be notified of a message in groups to have
        specific rendering depending on their group. For example users could
        have access to buttons customers should not have in their emails.
        Module-specific grouping should be done by overriding ``_notify_get_recipients_groups``
        method defined here-under.

        :param recipient_data: list of recipients information (based on res.partner
          records). See ``MailThread._notify_get_recipients()``;

        :return list: list of groups formatted for notification processing like
            [{'active': True,
              'actions': [],
              'button_access': {},
              'has_button_access': False,
              'recipients': [11],},
             {'active': True,
              'actions': [],
              'button_access': {'title': 'View Simple Chatter Model',
                                'url': '/mail/view?model=mail.test.simple&res_id=1497'},
              'has_button_access': True,
              'recipients': [4, 5, 6],},
             {'active': True,
              'actions': [],
              'button_access': {'title': 'View Simple Chatter Model',
                                'url': '/mail/view?model=mail.test.simple&res_id=1497'},
              'has_button_access': True,
              'recipients': [10, 11, 12],}
            ]
        """
        # keep a local copy of msg_vals as it may be modified to include more information about groups or links
        local_msg_vals = dict(msg_vals) if msg_vals else {}
        groups = self._notify_get_recipients_groups(msg_vals=local_msg_vals)
        access_link = self._notify_get_action_link('view', **local_msg_vals)
        if model_name:
            if self and self._name == 'sale.order' and self.name.startswith('INQ'):
                view_title = _('View Inquiry')
            else:
                view_title = _('View %s', model_name)
        else:
            view_title = _('View')

        # fill group_data with default_values if they are not complete
        for group_name, group_func, group_data in groups:
            is_thread_notification = self._notify_get_recipients_thread_info(msg_vals=msg_vals)['is_thread_notification']
            group_data.setdefault('active', True)
            group_data.setdefault('actions', list())
            group_data.setdefault('has_button_access', is_thread_notification)
            group_data.setdefault('notification_is_customer', False)
            group_data.setdefault('notification_group_name', group_name)
            group_data.setdefault('recipients', list())
            group_button_access = group_data.setdefault('button_access', {})
            group_button_access.setdefault('url', access_link)
            group_button_access.setdefault('title', view_title)

        # classify recipients in each group
        for recipient in recipient_data:
            for group_name, group_func, group_data in groups:
                if group_data['active'] and group_func(recipient):
                    group_data['recipients'].append(recipient['id'])
                    break

        # filter out groups without recipients
        return [group_data for _group_name, _group_func, group_data in groups
                if group_data['recipients']]