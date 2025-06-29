# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.tools.float_utils import float_round as round
from odoo.exceptions import UserError, ValidationError
from odoo.addons.account_tax_python.models.account_tax import AccountTaxPython

import math
import logging


def compute_all(self, price_unit, currency=None, quantity=1.0, product=None, partner=None, is_refund=False,
                handle_price_include=True, include_caba_tags=False):
    print("\n\n\ncompute_all------------------------accounttax--------------------------------------------")

    temp_dict_value = self._context.get('total_lines', 1)
    taxes = self.filtered(lambda r: r.amount_type != 'code')
    company = self.env.company
    if product and product._name == 'product.template':
        product = product.product_variant_id
    for tax in self.filtered(lambda r: r.amount_type == 'code'):
        localdict = self._context.get('tax_computation_context', {})
        localdict.update(
            {'total_lines': temp_dict_value, 'price_unit': price_unit, 'quantity': quantity, 'product': product,
             'partner': partner, 'company': company})
        safe_eval(tax.python_applicable, localdict, mode="exec", nocopy=True)
        if localdict.get('result', False):
            taxes += tax
    return super(AccountTaxPython, taxes).compute_all(price_unit, currency, quantity, product, partner,
                                                      is_refund=is_refund, handle_price_include=handle_price_include,
                                                      include_caba_tags=include_caba_tags)
AccountTaxPython.compute_all = compute_all


class AccountTax(models.Model):
    _inherit = 'account.tax'


    def _compute_amount(self, base_amount, price_unit, quantity=1.0, product=None, partner=None, custom=None):
        print("\n\n\n_compute_amount---------------------------tax---------------------------------------")
        """ Returns the amount of a single tax. base_amount is the actual amount on which the tax is applied, which is
            price_unit * quantity eventually affected by previous taxes (if tax is include_base_amount XOR price_include)
        """


        self.ensure_one()
        total_lines = self._context.get('total_lines', 1)
        if not custom:
            office_cost_feature = self.env['ir.config_parameter'].sudo().get_param(
                'custom_attribute_placeholder_cr.office_cost') or False

            cost_percentage = self.env['ir.config_parameter'].sudo().get_param(
                'custom_attribute_placeholder_cr.percentage') or False

            max_amount = self.env['ir.config_parameter'].sudo().get_param(
                'custom_attribute_placeholder_cr.max_amount') or False

            cost_percent = float(cost_percentage)
            maximum_amount = float(max_amount)
            # cost = 0.0
            base_amount = base_amount
            cost = base_amount * cost_percent / 100
            if office_cost_feature and cost_percentage:
                if cost > maximum_amount:
                    max_amount =  maximum_amount / (total_lines)
                    base_amount = base_amount + max_amount
                else:
                    # cost = base_amount + base_amount * cost_percent / 100
                    base_amount = base_amount + cost

            if self.amount_type == 'fixed':
                # Use copysign to take into account the sign of the base amount which includes the sign
                # of the quantity and the sign of the price_unit
                # Amount is the fixed price for the tax, it can be negative
                # Base amount included the sign of the quantity and the sign of the unit price and when
                # a product is returned, it can be done either by changing the sign of quantity or by changing the
                # sign of the price unit.
                # When the price unit is equal to 0, the sign of the quantity is absorbed in base_amount then
                # a "else" case is needed.
                if base_amount:
                    return math.copysign(quantity, base_amount) * self.amount
                else:
                    return quantity * self.amount

            price_include = self._context.get('force_price_include', self.price_include)

            # base * (1 + tax_amount) = new_base
            if self.amount_type == 'percent' and not price_include:
                return base_amount * self.amount / 100
            # <=> new_base = base / (1 + tax_amount)
            if self.amount_type == 'percent' and price_include:
                return base_amount - (base_amount / (1 + self.amount / 100))
            # base / (1 - tax_amount) = new_base
            if self.amount_type == 'division' and not price_include:
                return base_amount / (1 - self.amount / 100) - base_amount if (1 - self.amount / 100) else 0.0
            # <=> new_base * (1 - tax_amount) = base
            if self.amount_type == 'division' and price_include:
                return base_amount - (base_amount * (self.amount / 100))
            # default value for custom amount_type
            return 0.0

        else:

            self.ensure_one()

            if self.amount_type == 'fixed':
                # Use copysign to take into account the sign of the base amount which includes the sign
                # of the quantity and the sign of the price_unit
                # Amount is the fixed price for the tax, it can be negative
                # Base amount included the sign of the quantity and the sign of the unit price and when
                # a product is returned, it can be done either by changing the sign of quantity or by changing the
                # sign of the price unit.
                # When the price unit is equal to 0, the sign of the quantity is absorbed in base_amount then
                # a "else" case is needed.
                if base_amount:
                    return math.copysign(quantity, base_amount) * self.amount
                else:
                    return quantity * self.amount

            price_include = self._context.get('force_price_include', self.price_include)

            # base * (1 + tax_amount) = new_base
            if self.amount_type == 'percent' and not price_include:
                return base_amount * self.amount / 100
            # <=> new_base = base / (1 + tax_amount)
            if self.amount_type == 'percent' and price_include:
                return base_amount - (base_amount / (1 + self.amount / 100))
            # base / (1 - tax_amount) = new_base
            if self.amount_type == 'division' and not price_include:
                return base_amount / (1 - self.amount / 100) - base_amount if (1 - self.amount / 100) else 0.0
            # <=> new_base * (1 - tax_amount) = base
            if self.amount_type == 'division' and price_include:
                return base_amount - (base_amount * (self.amount / 100))
            # default value for custom amount_type
            return 0.0
