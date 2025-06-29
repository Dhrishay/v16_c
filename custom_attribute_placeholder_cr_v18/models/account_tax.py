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

    # @api.model
    # def _add_tax_details_in_base_line(self, base_line, company, rounding_method=None):
    #     print("\n\n\n_add_tax_details_in_base_line------------------customized--------------------------")
    #     """ Perform the taxes computation for the base line and add it to the base line under
    #     the 'tax_details' key. Those values are rounded or not depending of the tax calculation method.
    #     If you need to compute monetary fields with that, you probably need to call
    #     '_round_base_lines_tax_details' after this method.
    #
    #     The added tax_details is a dictionary containing:
    #     raw_total_excluded_currency:    The total without tax expressed in foreign currency.
    #     raw_total_excluded:             The total without tax expressed in local currency.
    #     raw_total_included_currency:    The total tax included expressed in foreign currency.
    #     raw_total_included:             The total tax included expressed in local currency.
    #     taxes_data:                     A list of python dictionary containing the taxes_data returned by '_get_tax_details' but
    #                                     with the amounts expressed in both currencies:
    #         raw_tax_amount_currency         The tax amount expressed in foreign currency.
    #         raw_tax_amount                  The tax amount expressed in local currency.
    #         raw_base_amount_currency        The tax base amount expressed in foreign currency.
    #         raw_base_amount                 The tax base amount expressed in local currency.
    #
    #     :param base_line:       A base line generated by '_prepare_base_line_for_taxes_computation'.
    #     :param company:         The company owning the base line.
    #     :param rounding_method: The rounding method to be used. If not specified, it will be taken from the company.
    #     """
    #     price_unit_after_discount = base_line['price_unit'] * (1 - (base_line['discount'] / 100.0))
    #     taxes_computation = base_line['tax_ids']._get_tax_details(
    #         price_unit=price_unit_after_discount,
    #         quantity=base_line['quantity'],
    #         precision_rounding=base_line['currency_id'].rounding,
    #         rounding_method=rounding_method or company.tax_calculation_rounding_method,
    #         product=base_line['product_id'],
    #         special_mode=base_line['special_mode'],
    #         manual_tax_amounts=base_line['manual_tax_amounts'],
    #     )
    #     rate = base_line['rate']
    #     tax_details = base_line['tax_details'] = {
    #         'raw_total_excluded_currency': taxes_computation['total_excluded'],
    #         'raw_total_excluded': taxes_computation['total_excluded'] / rate if rate else 0.0,
    #         'raw_total_included_currency': taxes_computation['total_included'],
    #         'raw_total_included': taxes_computation['total_included'] / rate if rate else 0.0,
    #         'taxes_data': [],
    #     }
    #     if company.tax_calculation_rounding_method == 'round_per_line':
    #         tax_details['raw_total_excluded'] = company.currency_id.round(tax_details['raw_total_excluded'])
    #         tax_details['raw_total_included'] = company.currency_id.round(tax_details['raw_total_included'])
    #     for tax_data in taxes_computation['taxes_data']:
    #         tax_amount = tax_data['tax_amount'] / rate if rate else 0.0
    #         base_amount = tax_data['base_amount'] / rate if rate else 0.0
    #         if company.tax_calculation_rounding_method == 'round_per_line':
    #             tax_amount = company.currency_id.round(tax_amount)
    #             base_amount = company.currency_id.round(base_amount)
    #         tax_details['taxes_data'].append({
    #             **tax_data,
    #             'raw_tax_amount_currency': tax_data['tax_amount'],
    #             'raw_tax_amount': tax_amount,
    #             'raw_base_amount_currency': tax_data['base_amount'],
    #             'raw_base_amount': base_amount,
    #         })
    #
    # @api.model
    # def _add_tax_details_in_base_lines(self, base_lines, company):
    #     print("\n\n\n_add_tax_details_in_base_lines------------customized-------------------------")
    #     """ Shortcut to call '_add_tax_details_in_base_line' on multiple base lines at once.
    #
    #     :param base_lines:  A list of base lines.
    #     :param company:     The company owning the base lines.
    #     """
    #     for base_line in base_lines:
    #         self._add_tax_details_in_base_line(base_line, company)
    #
