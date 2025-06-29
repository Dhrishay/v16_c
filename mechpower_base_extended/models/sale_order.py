# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def default_get(self, fields):
        result = super(SaleOrder, self).default_get(fields)
        if not self._context.get('website_id'):
            result['state'] = 'inquiry'
        return result

    is_customisable = fields.Boolean('Customize Order', store=True, compute='compute_order_line')
    is_place_inquiry = fields.Boolean('Place Inquiry', store=True, compute='compute_order_line_place_inquiry')
    sale_close_reason_id = fields.Many2one('sale.close.reason', string='Cancellation Reason')
    feasibility_status = fields.Selection([
        ('feasible', 'Feasible'),
        ('feasible_with_modification', 'Feasible With Modification'),
        ('not_feasible', 'Not Feasible'),
    ], string='Feasibility Status', tracking=True)
    state = fields.Selection(
        selection=[
            ('draft', "Draft"),
            ('inquiry', "Inquiry"),
            ('engineering_review', "Engineering Review"),
            ('data_feedback', "Data Feedback"),
            ('prepared_for_pricing', "Prepared for Pricing"),
            ('sent', "Quotation Sent"),
            ('sale', "Sales Order"),
            ('done', "Locked"),
            ('cancel', "Cancelled"),
        ],
        string="Status",
        readonly=True, copy=False, index=True,
        tracking=3,
        default='draft')
    customer_file_ids = fields.One2many('customer.files', 'order_id', string='Customer_files')

    additional_notes = fields.Text("Additional Notes")
    technical_drawing_file = fields.Binary('Technical Drawing', store=True)
    technical_drawing_file_name = fields.Char("Technical Drawing")
    uv_printing_file = fields.Binary('Uv Printing File', store=True)
    uv_printing_file_name = fields.Char("Uv Printing File")
    is_uv_printing = fields.Boolean('UV Printing (Flat Surface)')
    service = fields.Selection([
        ('enclosure_design', 'Enclosure Design'),
        ('fdm_modeling', '3D Printing (FDM)'),
        ('projection_printing', '3D Printing (Projection)'),
        ('sheet_metal_fabrication', 'Sheet Metal Fabrication'),
        ('cnc_machining', 'CNC Machining'),
        ('injection_molding', 'Injection Molding'),
    ])
    show_custom_state = fields.Boolean(compute='compute_custom_state')

    inquiry_date = fields.Datetime(string='Inquiry Date')
    quotation_date = fields.Datetime(string='Quotation Date')
    confirm_order_date = fields.Datetime(default=False, string='Confirm Order Date', required=False)
    state_date = fields.Datetime('Date')
    x_studio_date_of_delivery = fields.Datetime('Estimated Ship Date',tracking=1)
    paid_amount = fields.Float('Paid Amount', compute='compute_paid_and_due_amount')

    def compute_paid_and_due_amount(self):
        for rec in self:
            if rec.transaction_ids:
                rec.paid_amount = sum(rec.transaction_ids.filtered(lambda x: x.state == 'done').mapped('amount'))
            else:
                rec.paid_amount = 0

    def open_action_transaction(self):
        self.ensure_one()
        return {
            'name': _("Payments for %s", self.name),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'target': 'current',
            'domain': [('id', 'in', self.transaction_ids.mapped('payment_id').ids)],
            'res_model': 'account.payment',
            'res_id': self.id,
        }

    @api.onchange('x_studio_date_of_delivery')
    def onchange_x_studio_date_of_delivery(self):
        if self.x_studio_date_of_delivery and self.confirm_order_date and self.x_studio_date_of_delivery < self.confirm_order_date:
            raise ValidationError(_('Shipping date cannot be before the order date. Please select a valid shipping date.'))

    @api.depends('is_customisable', 'service')
    def compute_custom_state(self):
        for rec in self:
            if rec.is_customisable or (rec.service and rec.service != 'italtronic_enclosure'):
                rec.show_custom_state = True
            else:
                rec.show_custom_state = False

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if res.sale_close_reason_id:
            res.sale_close_reason_id = False
        if res.state == 'inquiry':
            res.inquiry_date = fields.Datetime.now()
            res.state_date = fields.Datetime.today()
            res.partner_id.last_inquiry_date = fields.Datetime.today()
        elif res.state == 'sent':
            res.quotation_date = fields.Datetime.now()
            res.state_date = fields.Datetime.today()
        elif res.state in ['done', 'sale']:
            res.confirm_order_date = fields.Datetime.now()
            res.state_date = fields.Datetime.today()
            res.partner_id.last_order_date = fields.Datetime.today()
        if not res.state_date:
            res.state_date = fields.Datetime.today()
        return res

    def write(self, vals):
        res = super().write(vals)
        if vals.get('state') and vals.get('state') == 'inquiry':
            self.inquiry_date = fields.Datetime.now()
            self.state_date = fields.Datetime.today()
            self.partner_id.last_inquiry_date = fields.Datetime.today()
        elif vals.get('state') and vals.get('state') == 'sent':
            self.quotation_date = fields.Datetime.now()
            self.state_date = fields.Datetime.today()
        elif vals.get('state') and vals.get('state') in ['done', 'sale']:
            self.confirm_order_date = fields.Datetime.now()
            self.state_date = fields.Datetime.today()
            self.partner_id.last_order_date = fields.Datetime.today()
        if 'is_uv_printing' in vals and not vals.get('is_uv_printing'):
            self.uv_printing_file = False
            self.uv_printing_file_name = False
        return res

    @api.depends('order_line')
    def compute_order_line(self):
        for rec in self:
            temp = rec.is_customisable
            if len(rec.order_line) > 0:
                rec.is_customisable = temp
            else:
                rec.is_customisable = False

    @api.depends('order_line')
    def compute_order_line_place_inquiry(self):
        for rec in self:
            temp = rec.is_place_inquiry
            if len(rec.order_line) > 0:
                rec.is_place_inquiry = temp
            else:
                rec.is_place_inquiry = False

    def action_cancel(self):
        if self.env.user.has_group('base.group_user'):
            return {
                'name': _('Cancellation Reason'),
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'sale.close.reason.wizard',
                'view_id': self.env.ref("mechpower_base_extended.sale_close_reason_view_form").id,
                'target': 'new',
            }
        else:
            return super().action_cancel()

    # action for those SO which is in cancel or sent state covert in to Inquiry state
    def action_draft(self):
        orders = self.filtered(lambda s: s.state in ['draft', 'cancel', 'sent'])
        for order in orders:
            order.write({
                'state': 'inquiry',
                'name': order.quotation_no,
                'sale_close_reason_id': False,
                'signature': False,
                'signed_by': False,
                'signed_on': False,
            })

    # set expire quotation cancel (cron)
    def _cron_cancel_expire_quotation(self):
        today = fields.Date.today()
        so_ids = self.env['sale.order'].search(
            [('state', 'in', ['draft', 'sent', 'inquiry']), ('validity_date', '<=', today)])
        for so in so_ids:
            so.sale_close_reason_id = self.env.ref('mechpower_base_extended.offer_is_expired').id
            so._action_cancel()

    # set public user quotation cancel (cron)
    def _cron_cancel_public_user_quotation(self):
        today = fields.Date.today()
        public_user_id = self.env.ref('base.public_user')
        so_ids = self.env['sale.order'].search([('partner_id', '=', public_user_id.partner_id.id)])
        for so in so_ids:
            days = (today - so.create_date.date()).days
            if days and days > 1:
                so.sale_close_reason_id = self.env.ref('mechpower_base_extended.public_user_quotation_reason').id
                so._action_cancel()

    def action_confirm(self):
        if not self.env.context.get('portal_order'):
            if self.is_customisable or (self.service and self.service != 'italtronic_enclosure'):
                if not self.feasibility_status and not self.env.context.get('website_order'):
                    raise ValidationError(_("Please enter the feasibility status before confirming this order."))
            if self.validity_date <= fields.Date.today():
                raise ValidationError(_("The quotation has expired."))
            elif self.feasibility_status == 'not_feasible':
                raise ValidationError(_("Orders cannot be confirmed without a feasibility status."))
            elif self.amount_total == 0:
                raise ValidationError(_("Orders cannot be confirmed with a total amount of 0."))
            else:
                sale_no = self.env["ir.sequence"].next_by_code(
                    "sale.order")
                self.write({"name": sale_no})
                return super().action_confirm()
        else:
            sale_no = self.env["ir.sequence"].next_by_code(
                "sale.order")
            self.write({"name": sale_no})
            return super().action_confirm()

    def set_state_engineering_review(self):
        # if self.feasibility_status == 'not_feasible':
        #     raise ValidationError(_("You cannot be changed state when feasibility status is Not Feasible."))
        self.state = 'engineering_review'

    def set_prepared_for_pricing(self):
        if self.is_customisable or self.is_place_inquiry or (self.service and self.service != 'italtronic_enclosure'):
            if not self.feasibility_status:
                raise ValidationError(_("Please enter the feasibility status."))
            elif self.feasibility_status == 'not_feasible':
                raise ValidationError(_("You cannot be changed state when feasibility status is Not Feasible."))
        self.state = 'prepared_for_pricing'

    def set_data_feedback(self):
        self.state = 'data_feedback'

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        if self.env.context.get('mark_so_as_sent'):
            self.filtered(
                lambda o: o.state in ['draft', 'inquiry', 'engineering_review', 'prepared_for_pricing']).with_context(
                tracking_disable=True).write({'state': 'sent'})
        return super(SaleOrder, self.with_context(
            mail_post_autofollow=self.env.context.get('mail_post_autofollow', True),
            lang=self.partner_id.lang,
        )).message_post(**kwargs)

    def action_quotation_send(self):
        if self.amount_total == 0:
            raise ValidationError(_("Documents cannot be sent with a total amount of 0."))
        if self.is_customisable or (self.service and self.service != 'italtronic_enclosure'):
            if not self.feasibility_status:
                raise ValidationError(_("Please enter the feasibility status before confirming this order."))
        return super().action_quotation_send()


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('price_unit')
    def onchange_price_line(self):
        if self and self.order_id and self.order_id.feasibility_status == 'not_feasible':
            raise ValidationError(
                _("Price modification is not permitted when the inquiry status is marked as not feasible.."))
