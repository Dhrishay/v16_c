# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Candidroot Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    office_cost = fields.Boolean("Office Costs", default=False, config_parameter='custom_attribute_placeholder_cr.office_cost')
    percentage = fields.Float("Percentage", config_parameter='custom_attribute_placeholder_cr.percentage')
    max_amount = fields.Float("Maximum amount", config_parameter='custom_attribute_placeholder_cr.max_amount')
    # done
    @api.constrains('percentage')
    def _check_percentage(self):
        # print("\n\n\n_check_percentage---------------------------------------")
        for rec in self:
            if rec and rec.percentage > 100:
                raise ValidationError("Please define a percentage upto 100")
