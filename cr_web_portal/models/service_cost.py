# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class ServiceCost(models.Model):
    _name = 'service.cost'
    _description = 'Service Cost'

    name = fields.Char()
    service = fields.Selection([
        ('enclosure_design', 'Enclosure Design'),
        ('fdm_modeling', 'FDM'),
        ('projection_printing', 'Projection'),
        ('sheet_metal_fabrication', 'Sheet Metal Fabrication'),
        ('cnc_machining', 'CNC Machining'),
        ('injection_molding', 'Injection Molding'),
        ('uv_printing', 'UV Printing'),
        ('italtronic_enclosure', 'Italtronic'),
        ('delivery', 'Delivery')
    ], string="Service")
    package_factor = fields.Float(string="Packaging Factor")
    logi_factor = fields.Float(string="Factor of logistic partner")
    rate = fields.Float(string="Rate")
    min_rate = fields.Float(string="Minimum rate")
    material_ids = fields.One2many('service.materials', 'service_id', string='Materials')
    print_quality_ids =  fields.One2many('service.print.quality', 'service_id', string='Print Quality')
    infill_ids =  fields.One2many('service.infill', 'service_id', string='InFill')
    no_of_sides_ids = fields.One2many('service.number.of.sides', 'service_id', string='Sides')


class ServiceMaterials(models.Model):
    _name = 'service.materials'
    _description = 'Service Materials'

    service_id = fields.Many2one('service.cost')
    name = fields.Char('Name')
    density = fields.Float('Density (g/cm)')
    rate_per_kg = fields.Float('Rate INR/kg')
    factor_support = fields.Float('Factor for supports')
    rate_per_gram = fields.Float('Rate INR/gram', compute='compute_rate_per_gram')
    is_default_value = fields.Boolean('Default  Value')

    @api.depends('rate_per_kg')
    def compute_rate_per_gram(self):
        for rec in self:
            rec.rate_per_gram = rec.rate_per_kg / 1000

    @api.constrains('is_default_value')
    def _check_default_value(self):
        for rec in self:
            existing_ids = self.search([('service_id', '=', rec.service_id.id), ('is_default_value', '=', True)])
            if len(existing_ids.ids) > 1:
                raise ValidationError("You Can Set Only One Default Value.")


class ServicePrintQuality(models.Model):
    _name = 'service.print.quality'
    _description = 'Service Print Quality'
    _rec_name = 'thickness'

    service_id = fields.Many2one('service.cost')
    thickness = fields.Float('Thickness')
    rate = fields.Float('Rate')
    is_default_value = fields.Boolean('Default  Value')

    @api.constrains('is_default_value')
    def _check_default_value(self):
        for rec in self:
            existing_ids = self.search([('service_id', '=', rec.service_id.id), ('is_default_value', '=', True)])
            if len(existing_ids.ids) > 1:
                raise ValidationError("You Can Set Only One Default Value.")


class ServiceInFill(models.Model):
    _name = 'service.infill'
    _description = 'Service InFill'
    _rec_name = 'percent'

    service_id = fields.Many2one('service.cost')
    percent = fields.Float('Percent %')
    rate = fields.Float('Rate')
    is_default_value = fields.Boolean('Default  Value')

    @api.constrains('is_default_value')
    def _check_default_value(self):
        for rec in self:
            existing_ids = self.search([('service_id', '=', rec.service_id.id), ('is_default_value', '=', True)])
            if len(existing_ids.ids) > 1:
                raise ValidationError("You Can Set Only One Default Value.")

class ServiceNoSides(models.Model):
    _name = 'service.number.of.sides'
    _description = 'Service Number Of Sides'
    _rec_name = 'no_sides'

    service_id = fields.Many2one('service.cost')
    no_sides = fields.Integer('No. of sides')
    factor = fields.Float('Factor %')
    min_price = fields.Float('Min')
