# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, tools
import uuid


class AccountMove(models.Model):
    _inherit = 'account.move'

    is_scrap = fields.Boolean('Is Scrap',default=False)
    tag_ids = fields.Many2many(
        comodel_name='crm.tag',
        relation='invoice_tag_rel', column1='invoice_id', column2='tag_id',
        string="Tags")

    service = fields.Selection([
        ('enclosure_design', 'Enclosure Design'),
        ('fdm_modeling', '3D Printing (FDM)'),
        ('projection_printing', '3D Printing (Projection)'),
        ('sheet_metal_fabrication', 'Sheet Metal Fabrication'),
        ('cnc_machining', 'CNC Machining'),
        ('injection_molding', 'Injection Molding'),
        ('uv_printing', 'UV Printing'),
        ('italtronic_enclosure', 'Italtronic'),
        ('customized_italtronics','Customized Italtronics')
    ], string="Service/ Product")

    def get_invoiceline_product(self):
        delivery_line = self.env['delivery.carrier'].sudo().search([('is_published','=',True)]).mapped('product_id').ids
        invoice_lines = self.invoice_line_ids.filtered(lambda line: line.product_id.id not in delivery_line)
        return [line.product_id.name for line in invoice_lines] if invoice_lines else False

    def get_invoiceline_product_qty(self):
        delivery_line = self.env['delivery.carrier'].sudo().search([('is_published','=',True)]).mapped('product_id').ids
        invoice_lines = self.invoice_line_ids.filtered(lambda line: line.product_id.id not in delivery_line)

        return sum([int(line.quantity) for line in invoice_lines]) if invoice_lines else False

    def get_portal_order_status(self):
        if self.env['sale.order'].search([('invoice_ids', 'in', self.ids)]):
            so_id = self.env['sale.order'].search([('invoice_ids', 'in', self.ids)], limit=1)
            if so_id.invoice_status == 'invoiced':
                return 'Fully Invoiced'
            if so_id.invoice_status == 'to invoice':
                return 'To Invoice'
            if so_id.invoice_status == 'no':
                return 'Nothing to Invoice'
        return False