# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _
from odoo.tools.mail import is_html_empty


class CrmLeadLost(models.TransientModel):
    _inherit = 'crm.lead.lost'

    def action_lost_reason_apply(self):
        self.ensure_one()
        leads = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        if not is_html_empty(self.lost_feedback):
            leads._track_set_log_message(
                '<div style="margin-bottom: 4px;"><p>%s:</p>%s<br /></div>' % (
                    _('Lost Comment'),
                    self.lost_feedback
                )
            )
        res = leads.action_set_lost(lost_reason_id=self.lost_reason_id.id)
        for lead in leads:
            for so in self.env['sale.order'].search(
                    [('state', 'in', ['draft', 'sent']), ('opportunity_id', '=', lead.id)]):
                so._action_cancel()
        return res
