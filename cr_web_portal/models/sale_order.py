# -*- coding: utf-8 -*-
from odoo.http import request
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

AVAILABLE_PRIORITIES = [
    ('0', 'Normal'),
    ('1', 'Low'),
    ('2', 'Medium'),
    ('3', 'High')
]
import random

from odoo.fields import Command
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    closed_by = fields.Selection([('user', 'User'), ('customer', 'Customer')], string='Lost By')
    close_reason_id = fields.Many2one("sale.order.close.reason", string="Lost Reason", copy=False, tracking=True)
    service = fields.Selection([
        ('enclosure_design', 'Enclosure Design'),
        ('fdm_modeling', '3D Printing (FDM)'),
        ('projection_printing', '3D Printing (Projection)'),
        ('sheet_metal_fabrication', 'Sheet Metal Fabrication'),
        ('cnc_machining', 'CNC Machining'),
        ('injection_molding', 'Injection Molding'),
        ('uv_printing', 'UV Printing'),
        ('italtronic_enclosure', 'Italtronic'),
        ('customized_italtronics', 'Customized Italtronics')
    ], string=" Service/ Product")
    priority = fields.Selection(AVAILABLE_PRIORITIES, "Probability", default='1')

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.partner_id and (not self.partner_id.industry_main_category or not self.partner_id.industry_sub_category or not self.partner_id.lead_source):
            raise ValidationError(_('Please update your category segmentation.'))

    # def setup_so(self):
    #     orders = self.search([('invoice_ids','!=',False)])
    #
    #     for o in orders:
    #         for inv in o.invoice_ids:
    #             inv.sudo().write({
    #                 'service' : o.service if o.service else False,
    #                 'tag_ids' : [(6, 0, o.tag_ids.ids)] if o.tag_ids else False
    #             })

    def write(self, vals):
        res = super().write(vals)
        if self.invoice_ids:
            if 'service' in vals:
                for invoice in self.invoice_ids:
                    invoice.sudo().write({
                        'service': self.service,
                    })

            if 'tag_ids' in vals:
                for invoice in self.invoice_ids:
                    invoice.sudo().write({
                        'tag_ids': [(6, 0, self.tag_ids.ids)],
                    })
        return res

    def action_quotation_sent(self):
        """ Mark the given draft quotation(s) as sent.

        :raise: UserError if any given SO is not in draft state.
        """
        if self.filtered(lambda so: so.state not in ['draft','inquiry','engineering_review','prepared_for_pricing']):
            raise UserError(_("Only inquiry can be marked as sent directly."))

        for order in self:
            order.message_subscribe(partner_ids=order.partner_id.ids)

        self.write({'state': 'sent'})

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if 'partner_id' in vals:
            partner_id = self.env['res.partner'].sudo().search([('id','=',vals['partner_id'])])
            if partner_id and partner_id.email and self.env.user.has_group('base.group_user'):
                same_partner = self.env['res.partner'].sudo().search([('email', '=', partner_id.email), ('id', '!=', partner_id.id)])
                if same_partner:
                    raise ValidationError("The email address '%s' is already used by another contact." % partner_id.email)
                else:
                    user_id = self.env['res.users'].sudo().search([('partner_id','=',partner_id.id)])
                    if not user_id:
                        portal_wizard = self.env['portal.wizard'].sudo().with_context(active_ids=[partner_id.id]).create({})
                        portal_user = portal_wizard.user_ids
                        if len(portal_user) > 1:
                            new_u = False
                            for u_rec in portal_user:
                                if u_rec.partner_id.id == partner_id.id and partner_id.email:
                                    new_u = u_rec
                                else:
                                    u_rec.sudo().unlink()
                            if new_u:
                                new_u.email = partner_id.email
                                new_u.action_grant_access()

                        elif len(portal_user) == 1:
                            portal_user.email = partner_id.email
                            portal_user.action_grant_access()

        if not res.source_id:
            res.source_id = self.env.ref('cr_web_portal.utm_source_by_mech_power').id
        if res.opportunity_id:
            res.tag_ids = [(4, tag.id) for tag in res.opportunity_id.tag_ids]
            if res.opportunity_id.service:
                res.service = res.opportunity_id.service
        return res

    def _notify_get_recipients_groups(self, msg_vals=None):
        """ Give access button to users and portal customer as portal is integrated
        in sale. Customer and portal group have probably no right to see
        the document so they don't have the access button. """
        groups = super()._notify_get_recipients_groups(msg_vals=msg_vals)
        if not self:
            return groups

        self.ensure_one()
        if self._context.get('proforma'):
            for group in [g for g in groups if g[0] in ('portal_customer', 'portal', 'follower', 'customer')]:
                group[2]['has_button_access'] = False
            return groups
        local_msg_vals = dict(msg_vals or {})

        # portal customers have full access (existence not granted, depending on partner_id)
        try:
            customer_portal_group = next(group for group in groups if group[0] == 'portal_customer')
        except StopIteration:
            pass
        else:
            access_opt = customer_portal_group[2].setdefault('button_access', {})
            is_tx_pending = self.get_portal_last_transaction().state == 'pending'
            if self._has_to_be_signed(include_draft=True):
                if self._has_to_be_paid():
                    access_opt['title'] = _("View Quotation") if is_tx_pending else _("Sign & Pay Quotation")
                elif self.is_customisable or self.service:
                    access_opt['title'] = _("View Inquiry")
                else:
                    access_opt['title'] = _("Accept & Sign Quotation")
            elif self.is_customisable or self.service:
                access_opt['title'] = _("View Inquiry")
            elif self._has_to_be_paid(include_draft=True) and not is_tx_pending:
                access_opt['title'] = _("Accept & Pay Quotation")
            elif self.state in ('draft', 'sent'):
                access_opt['title'] = _("View Quotation")

        # enable followers that have access through portal
        follower_group = next(group for group in groups if group[0] == 'follower')
        follower_group[2]['active'] = True
        follower_group[2]['has_button_access'] = True
        access_opt = follower_group[2].setdefault('button_access', {})
        if self.state in ('draft', 'sent'):
            access_opt['title'] = _("View Quotation")
        else:
            access_opt['title'] = _("View Order")
        access_opt['url'] = self._notify_get_action_link('view', **local_msg_vals)
        if self and self._name == 'sale.order' and self.name.startswith('INQ'):
            access_opt['title'] = _('View Inquiry')
        return groups

    def _compute_access_url(self):
        super()._compute_access_url()
        for order in self:
            if order.state in ['inquiry', 'engineering_review', 'prepared_for_pricing', 'data_feedback']:
                order.access_url = f'/my/inquiry/quotes/{order.id}'
            else:
                order.access_url = f'/my/orders/{order.id}'

    def _get_report_base_filename(self):
        self.ensure_one()
        if self.state in ['inquiry', 'engineering_review', 'prepared_for_pricing', 'data_feedback']:
            return 'Inquiry %s' % (self.name)
        elif self.state in ['sale']:
            return 'PRO-FORMA - %s' % (self.name)
        else:
            return '%s %s' % (self.type_name, self.name)

    def _check_carrier_quotation(self, force_carrier_id=None, keep_carrier=False):
        self.ensure_one()
        DeliveryCarrier = self.env['delivery.carrier']

        if self.only_services:
            self._remove_delivery_line()
            return True
        else:
            self = self.with_company(self.company_id)
            # attempt to use partner's preferred carrier
            if not force_carrier_id and self.partner_shipping_id.property_delivery_carrier_id and not keep_carrier:
                force_carrier_id = self.partner_shipping_id.property_delivery_carrier_id.id

            carrier = force_carrier_id and DeliveryCarrier.browse(force_carrier_id) or self.carrier_id
            available_carriers = self._get_delivery_methods()
            if carrier:
                if carrier not in available_carriers:
                    carrier = DeliveryCarrier
                else:
                    # set the forced carrier at the beginning of the list to be verfied first below
                    available_carriers -= carrier
                    available_carriers = carrier + available_carriers
            if force_carrier_id or not carrier or carrier not in available_carriers:
                for delivery in available_carriers:
                    verified_carrier = delivery._match_address(self.partner_shipping_id)
                    if verified_carrier:
                        carrier = delivery
                        break
                self.write({'carrier_id': carrier.id})
            self._remove_delivery_line()
            if carrier and not self.is_customisable:
                res = carrier.rate_shipment(self)
                if res.get('success'):
                    self.set_delivery_line(carrier, res['price'])
                    self.delivery_rating_success = True
                    self.delivery_message = res['warning_message']
                else:
                    self.set_delivery_line(carrier, 0.0)
                    self.delivery_rating_success = False
                    self.delivery_message = res['error_message']

        return bool(carrier)

    def _verify_updated_quantity(self, order_line, product_id, new_qty, **kwargs):
        self.ensure_one()
        if not self.is_place_inquiry:
            product = self.env['product.product'].browse(product_id)
            if product.type == 'product' and not product.allow_out_of_stock_order:
                product_qty_in_cart, available_qty = self._get_cart_and_free_qty(
                    line=order_line, product=product, **kwargs
                )
                old_qty = order_line.product_uom_qty if order_line else 0
                added_qty = new_qty - old_qty
                total_cart_qty = product_qty_in_cart + added_qty
                if available_qty < total_cart_qty:
                    return new_qty,''
            return new_qty, ''
        else:
            return new_qty, ''

    def _cart_update(self, product_id, line_id=None, add_qty=0, set_qty=0, **kwargs):
            """ Add or set product quantity, add_qty can be negative """
            self.ensure_one()
            self = self.with_company(self.company_id)

            if self.state != 'draft':
                request.session.pop('sale_order_id', None)
                request.session.pop('website_sale_cart_quantity', None)
                raise UserError(_('It is forbidden to modify a sales order which is not in draft status.'))

            product = self.env['product.product'].browse(product_id).exists()
            if 'allowd_for_customised' not in kwargs:
                if add_qty and (not product or not product._is_add_to_cart_allowed()):
                    raise UserError(_("The given product does not exist therefore it cannot be added to cart."))
            else:
                kwargs.pop('allowd_for_customised')

            if line_id is not False:
                order_line = self._cart_find_product_line(product_id, line_id, **kwargs)[:1]
            else:
                order_line = self.env['sale.order.line']

            try:
                if add_qty:
                    add_qty = int(add_qty)
            except ValueError:
                add_qty = 1

            try:
                if set_qty:
                    set_qty = int(set_qty)
            except ValueError:
                set_qty = 0

            quantity = 0
            if set_qty:
                quantity = set_qty
            elif add_qty is not None:
                if order_line:
                    quantity = order_line.product_uom_qty + (add_qty or 0)
                else:
                    quantity = add_qty or 0

            if quantity > 0:
                quantity, warning = self._verify_updated_quantity(
                    order_line,
                    product_id,
                    quantity,
                    **kwargs,
                )
            else:
                # If the line will be removed anyway, there is no need to verify
                # the requested quantity update.
                warning = ''

            order_line = self._cart_update_order_line(product_id, quantity, order_line, **kwargs)
            if self.is_place_inquiry:
                return {
                    'line_id': order_line.id,
                    'quantity': quantity,
                    'option_ids': list(
                        set(order_line.option_line_ids.filtered(lambda l: l.order_id == order_line.order_id).ids)),
                    'warning': warning,
                }
            if (
                    order_line
                    and order_line.price_unit == 0
                    and self.website_id.prevent_zero_price_sale
                    and product.detailed_type not in self.env['product.template']._get_product_types_allow_zero_price()
            ):
                raise UserError(_(
                    "The given product does not have a price therefore it cannot be added to cart.",
                ))

            return {
                'line_id': order_line.id,
                'quantity': quantity,
                'option_ids': list(
                    set(order_line.option_line_ids.filtered(lambda l: l.order_id == order_line.order_id).ids)),
                'warning': warning,
            }
    def _compute_note(self):
        # use_invoice_terms = self.env['ir.config_parameter'].sudo().get_param('account.use_invoice_terms')
        # if not use_invoice_terms:
        #     return
        for order in self:
            order.note = _('')
            # order = order.with_company(order.company_id)
            # if order.terms_type == 'html' and self.env.company.invoice_terms_html:
            # baseurl = html_keep_url(order._get_note_url() + '/terms')
            # context = {'lang': order.partner_id.lang or self.env.user.lang}
            # order.note = _('Terms & Conditions: %s', baseurl)
            #     del context
            # elif not is_html_empty(self.env.company.invoice_terms):
            #     order.note = order.with_context(lang=order.partner_id.lang).env.company.invoice_terms


    def _cart_accessories(self):
        """ Suggest accessories based on 'Accessory Products' of products in cart """
        products = self.website_order_line.product_id
        all_accessory_products = self.env['product.product']
        chunks = []
        for line in self.website_order_line.filtered('product_id'):
            accessory_products = line.product_id.accessory_product_ids
            if accessory_products:
                # Do not read ptavs if there is no accessory products to filter
                combination = line.product_id.product_template_attribute_value_ids + line.product_no_variant_attribute_value_ids
                all_accessory_products |= accessory_products.filtered(
                    lambda product:
                    product not in products and
                    (not product.company_id or product.company_id == line.company_id) and
                    product._is_variant_possible(parent_combination=combination)
                    and (
                            not self.website_id.prevent_zero_price_sale
                            or product._get_contextual_price()
                    )
                )
            chunks = self.chunked_records(all_accessory_products, 4)
        return chunks

    def chunked_records(self, products, chunk_size=4):
        """Split recordset into chunks of `chunk_size`"""
        return [products[i: i + chunk_size] for i in range(0, len(products), chunk_size)]

    def can_reorder(self):
        if self.order_line:
            is_without_customizable_product = not any(line.product_id.default_code.startswith('CFGX') for line in self.order_line if line.product_id and line.product_id.default_code)
            reorderable_orederline_ids = []
            if self.order_line:
                reorderable_orederline_ids = self.order_line.filtered(lambda x: not x.is_delivery and not x.is_downpayment and not x.display_type and float(x.qty_delivered) > 0.00 )
            is_price_zero = True
            for line in self.order_line:
                price_list_items = request.env['product.pricelist.item'].sudo().search(
                    [('product_id', '=', int(line.product_id.id))], order='id asc')
                if len(price_list_items) > 0:
                    for l_items in price_list_items:
                        if l_items.fixed_price == 0.0:
                            is_price_zero = False
                else:
                    is_price_zero = False

            return is_price_zero and is_without_customizable_product and len(reorderable_orederline_ids) > 0
        else:
            return False

    def get_orderline_product(self):
        order_lines = self.order_line.filtered(lambda x: not x.is_delivery and not x.is_downpayment and not x.display_type)
        return [so_line.product_id.name for so_line in order_lines] if order_lines else False

    def get_reorderable_orederline(self):
        orderline_ids = []
        if self.order_line:
            for line in self.order_line:
                if line.product_id and line.product_id.default_code:
                    price_list_items = request.env['product.pricelist.item'].sudo().search([('product_id', '=', int(line.product_id.id))], order='id asc')
                    is_price_zero = True
                    if len(price_list_items) > 0:
                        for l_items in price_list_items:
                            if l_items.fixed_price == 0.0:
                                is_price_zero = False
                    else:
                        is_price_zero = False

                    if not line.product_id.default_code.startswith('CFGX') and is_price_zero:
                        orderline_ids.append(line.id)
            if orderline_ids:
                orderlines = self.env['sale.order.line'].sudo().search([('id','in',orderline_ids)])
                return orderlines.filtered(lambda x: not x.is_delivery and not x.is_downpayment and not x.display_type and float(x.qty_delivered) > 0.00 )
            else:
                return False
        else:
            return False

    def _find_mail_template(self):
        self.ensure_one()
        if self.env.context.get('proforma'):
            return self.env.ref('cr_web_portal.email_template_pro_forma_invoice', raise_if_not_found=False)
        elif self.state not in ('sale', 'done'):
            if self.payment_term_id.is_advance_payment:
                return self.env.ref('sale.email_template_edi_sale', raise_if_not_found=False)
            else:
                return self.env.ref('cr_web_portal.email_template_edi_sale_without_advance_payment', raise_if_not_found=False)
        else:
            return self._get_confirmation_template()

    def get_payable_amount(self):
        delivery_amount = sum(self.order_line.filtered(lambda x: x.is_delivery).mapped('price_subtotal'))
        for record in self.payment_term_id:
            percent_ids = record.line_ids.filtered(lambda x: x.value == 'percent')
            if percent_ids:
                percentage = percent_ids[0].value_amount
                payable_amount = ((self.amount_total - delivery_amount) * percentage) / 100
                return {
                    'min': round(float(payable_amount), 2),
                    'max': round(float(self.amount_total), 2),
                    'amount': round(float(payable_amount), 2)
                }
        return {
            'min': round(float(self.amount_total), 2),
            'max': round(float(self.amount_total), 2),
            'amount': round(float(self.amount_total), 2)
        }

    def _prepare_invoice(self):
        self.ensure_one()

        return {
            'ref': self.client_order_ref or '',
            'move_type': 'out_invoice',
            'narration': self.note,
            'currency_id': self.currency_id.id,
            'campaign_id': self.campaign_id.id,
            'medium_id': self.medium_id.id,
            'source_id': self.source_id.id,
            'team_id': self.team_id.id,
            'partner_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'fiscal_position_id': (self.fiscal_position_id or self.fiscal_position_id._get_fiscal_position(
                self.partner_invoice_id)).id,
            'invoice_origin': self.name,
            'invoice_payment_term_id': self.payment_term_id.id,
            'invoice_user_id': self.user_id.id,
            'payment_reference': self.reference,
            'transaction_ids': [Command.set(self.transaction_ids.ids)],
            'company_id': self.company_id.id,
            'invoice_line_ids': [],
            'user_id': self.user_id.id,
            'service': self.service if self.service and 'add_tags_service' in self.env.context and self.env.context.get('add_tags_service') else False,
            'tag_ids': [(6, 0,self.tag_ids.ids)] if self.tag_ids and 'add_tags_service' in self.env.context and self.env.context.get('add_tags_service') else False
        }

    def get_without_delivery_amount(self):
        return sum(self.order_line.filtered(lambda x: not x.is_delivery and x.price_subtotal).mapped('price_subtotal')) or 0.00

    def is_remaining_amount(self):
        remaining_amount = self.amount_total - self.paid_amount
        if remaining_amount > 0 and self.transaction_ids.filtered(lambda x:x.state == 'done'):
            return round(float(remaining_amount), 2)
        else:
            return False

    def get_portal_order_status(self):
        is_service_order = any((line.product_id.is_enclosure_service or
                                line.product_id.is_fdm_service or
                                line.product_id.is_projection_service or
                                line.product_id.is_metal_feb_service or
                                line.product_id.is_cnc_machining_service or
                                line.product_id.is_injection_mold_service)for line in self.order_line)
        if is_service_order:
            if self.state == 'inquiry':
                return 'Inquiry'
            elif self.state == 'engineering_review':
                if self.feasibility_status == 'feasible':
                   return 'Feasible'
                if self.feasibility_status == 'feasible_with_modification':
                    return 'Not Feasible'
                if self.feasibility_status == 'not_feasible':
                    'Feasible with Modification'
            elif self.state == 'data_feedback':
                return 'Data Feedback'
            elif self.state == 'prepared_for_pricing':
                return 'Prepared for Pricing'
            elif self.state == 'sent':
                return 'Quotation Sent'
            else:
                return False
        else:
            if self.picking_ids and self.picking_ids.filtered(lambda x: x.state != 'cancel'):
                picking_ids = self.picking_ids.filtered(lambda x: x.state != 'cancel')
                done_picking_ids = picking_ids.filtered(lambda x: x.state == 'done')
                ready_picking_ids = picking_ids.filtered(lambda x: x.state == 'assigned')
                waiting_picking_ids = picking_ids.filtered(lambda x: x.state == 'confirmed')
                if not done_picking_ids and (ready_picking_ids or waiting_picking_ids):
                    return 'Started'
                if done_picking_ids and (ready_picking_ids or waiting_picking_ids):
                    return 'Partially Dispatched'
                if done_picking_ids and not ready_picking_ids and not waiting_picking_ids:
                    return 'Fully Dispatched'
                else:
                    return 'Not Dispatched'
            else:
                return 'Not Dispatched'
        return False

    def _get_delivery_methods(self):
        # searching on website_published will also search for available website (_search method on
        # computed field)
        is_service_order = all((line.product_id.is_enclosure_service or
                                line.product_id.is_fdm_service or
                                line.product_id.is_projection_service or
                                line.product_id.is_metal_feb_service or
                                line.product_id.is_cnc_machining_service or
                                line.product_id.is_injection_mold_service) for line in self.order_line.filtered(lambda x: not x.is_delivery and not x.is_downpayment and not x.display_type))
        if is_service_order:
            return self.env['delivery.carrier'].sudo().search([
                ('website_published', '=', True),('id', '=', self.env.ref('delivery.free_delivery_carrier').id)])
        else:
            return self.env['delivery.carrier'].sudo().search([
                ('website_published', '=', True), ('id', '!=', self.env.ref('delivery.free_delivery_carrier').id)
            ]).filtered(lambda carrier: carrier._is_available_for_order(self))