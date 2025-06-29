# -*- coding: utf-8 -*-

from odoo import models, tools, fields
from datetime import datetime, timedelta


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    priority = fields.Selection(default=False)


class HelpdeskTeam(models.Model):
    _inherit = 'helpdesk.team'

    def _compute_success_rate(self):
        for rec in self:
            total_ticket = self.env['helpdesk.ticket'].search_count([('team_id', '=', rec.id)])
            solved_ticket = self.env['helpdesk.ticket'].search_count(
                [('team_id', '=', rec.id), ('stage_id', '=', self.env.ref('helpdesk.stage_solved').id)])
            if total_ticket and solved_ticket:
                rec.success_rate = ((solved_ticket * 100) / total_ticket)
            else:
                rec.success_rate = 0

    def action_view_success_rate(self):
        action = self.action_view_ticket()
        action['domain'] = [('team_id', '=', self.id), ('stage_id', '=', self.env.ref('helpdesk.stage_solved').id)]
        return action

    def _compute_ticket_closed(self):
        for rec in self:
            first_day_of_month = datetime.today().replace(day=1).strftime('%Y-%m-%d')
            last_day_of_month = datetime.today().replace(day=1).replace(month=datetime.today().month + 1) - timedelta(
                days=1)
            last_day_of_month = last_day_of_month.strftime('%Y-%m-%d')
            solved_ticket = self.env['helpdesk.ticket'].search_count(
                [('team_id', '=', rec.id), ('stage_id', '=', self.env.ref('helpdesk.stage_solved').id),
                 ('close_date', '>=', first_day_of_month),
                 ('close_date', '<=', last_day_of_month)])
            rec.ticket_closed = solved_ticket

    def action_view_closed_ticket(self):
        action = self.action_view_ticket()
        first_day_of_month = datetime.today().replace(day=1).strftime('%Y-%m-%d')
        last_day_of_month = datetime.today().replace(day=1).replace(month=datetime.today().month + 1) - timedelta(
            days=1)
        last_day_of_month = last_day_of_month.strftime('%Y-%m-%d')
        action['domain'] = [('team_id', '=', self.id), ('stage_id', '=', self.env.ref('helpdesk.stage_solved').id),
                            ('close_date', '>=', first_day_of_month),
                            ('close_date', '<=', last_day_of_month)]
        return action

    def _compute_open_ticket_count(self):
        open_stage_ids = [self.env.ref('helpdesk.stage_new').id, self.env.ref('helpdesk.stage_in_progress').id, self.env.ref('helpdesk.stage_on_hold').id]
        for team in self:
            team.open_ticket_count = self.env['helpdesk.ticket'].search_count([('stage_id', 'in', open_stage_ids),  ('team_id', 'in', self.ids)])

    def action_view_open_ticket(self):
        action = self.action_view_ticket()
        open_stage_ids = [self.env.ref('helpdesk.stage_new').id, self.env.ref('helpdesk.stage_in_progress').id, self.env.ref('helpdesk.stage_on_hold').id]
        action['domain'] =[('stage_id', 'in', open_stage_ids)]
        return action

    def _compute_unassigned_tickets(self):
        for team in self:
            team.unassigned_tickets = self.env['helpdesk.ticket'].search_count([('user_id', '=', False), ('team_id', 'in', team.ids)])

    def _compute_urgent_ticket(self):
        open_stage_ids = [self.env.ref('helpdesk.stage_new').id, self.env.ref('helpdesk.stage_in_progress').id,
                          self.env.ref('helpdesk.stage_on_hold').id]
        for team in self:
            team.urgent_ticket = self.env['helpdesk.ticket'].search_count([('team_id', 'in', team.ids), ('stage_id', 'in', open_stage_ids), ('priority', '=', '3')])

    def action_view_urgent(self):
        action = self.action_view_ticket()
        open_stage_ids = [self.env.ref('helpdesk.stage_new').id, self.env.ref('helpdesk.stage_in_progress').id,
                          self.env.ref('helpdesk.stage_on_hold').id]
        action['domain'] = [('team_id', 'in', self.ids), ('stage_id', 'in', open_stage_ids), ('priority', '=', '3')]
        return action