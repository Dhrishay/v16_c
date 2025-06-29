from odoo import models, fields, _
from odoo.tools import format_date
from datetime import datetime
class StockPicking(models.Model):
    _inherit = 'stock.picking'

    box_size = fields.Char('Box Size')
    package_weight = fields.Float('Package Weight')
    is_mail_sent = fields.Boolean(default=False,help="Specify Delivery Order Done Mail Sent Or Not")

    def calculate_weight(self):
        for picking in self:
            for move in picking.move_ids:
                move._cal_move_weight()

    def _sent_mail_delivery_done(self):
        date_from = datetime.now().strftime('%Y-%m-%d 00:00:00')
        date_to = datetime.now().strftime('%Y-%m-%d 23:59:59')
        deliveries = self.search([('date_done','>=',date_from),('date_done','<',date_to),('picking_type_id.code','=','outgoing'),('state','=','done'),('carrier_tracking_ref','!=',False),('is_mail_sent','=',False)])
        if deliveries:
            delivery_template_id = self.env.ref('mechpower_base_extended.mail_template_data_delivery_confirmation_mp').id
            for rec in deliveries:
                rec.with_context(force_send=True).message_post_with_template(delivery_template_id,email_layout_xmlid='mail.mail_notification_light')
                rec.is_mail_sent = True