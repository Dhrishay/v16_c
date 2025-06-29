# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import itertools
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _get_matrix(self, product_template):
        print("\n\n\n_get_matrix-----------------------------------------------------------------------")
        """Return the matrix of the given product, updated with current SOLines quantities.

        :param product.template product_template:
        :return: matrix to display
        :rtype dict:
        """
        def has_ptavs(line, sorted_attr_ids):
            # TODO instead of sorting on ids, use odoo-defined order for matrix ?
            ptav = line.product_template_attribute_value_ids.ids
            pnav = line.product_no_variant_attribute_value_ids.ids
            pav = pnav + ptav
            pav.sort()
            return pav == sorted_attr_ids
        matrix = product_template._get_template_matrix(
            company_id=self.company_id,
            currency_id=self.currency_id,
            display_extra_price=True,
            pricelist_id=self.pricelist_id
        )
        if self.order_line:
            lines = matrix['matrix']
            order_lines = self.order_line.filtered(lambda line: line.product_template_id == product_template)
            for line in lines:
                for cell in line:
                    if not cell.get('name', False):
                        line = order_lines.filtered(lambda line: has_ptavs(line, cell['ptav_ids']))
                        if line:
                            cell.update({
                                'qty': sum(line.mapped('product_uom_qty'))
                            })
        return matrix


class AttributeValue(models.Model):
    _inherit = 'product.template.attribute.value'

    is_placeholder = fields.Boolean("Display Dynamic Placeholder")


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_template_matrix(self, **kwargs):
        print("\n\n\n_get_template_matrix--------------------template-----------------------------------------")
        self.ensure_one()
        company_id = kwargs.get('company_id', None) or self.company_id or self.env.company
        currency_id = kwargs.get('currency_id', None) or self.currency_id
        display_extra = kwargs.get('display_extra_price', False)
        attribute_lines = self.valid_product_template_attribute_line_ids

        Attrib = self.env['product.template.attribute.value']
        first_line_attributes = attribute_lines[0].product_template_value_ids._only_active()
        attribute_ids_by_line = [line.product_template_value_ids._only_active().ids for line in attribute_lines]

        header = [{"name": self.display_name}] + [
            attr._grid_header_cell(
                fro_currency=self.currency_id,
                to_currency=currency_id,
                company=company_id,
                display_extra=display_extra
            ) for attr in first_line_attributes]

        result = [[]]
        for pool in attribute_ids_by_line:
            result = [x + [y] for y in pool for x in result]
        args = [iter(result)] * len(first_line_attributes)
        rows = itertools.zip_longest(*args)

        matrix = []
        for row in rows:
            row_attributes = Attrib.browse(row[0][1:])
            row_header_cell = row_attributes._grid_header_cell(
                fro_currency=self.currency_id,
                to_currency=currency_id,
                company=company_id,
                display_extra=display_extra)
            result = [row_header_cell]

            for cell in row:
                combination = Attrib.browse(cell)

                sale_order_pricelist_id = kwargs.get('pricelist_id', False)

                placeholder = False
                for i in combination:
                    if i.is_placeholder:
                        placeholder = True

                pricelist_item_ids = self.env['product.pricelist.item']
                for product in self.product_variant_ids:
                    if combination.ids == product.product_template_attribute_value_ids.ids and placeholder and sale_order_pricelist_id:

                        pricelist_item_ids = self.env['product.pricelist.item'].search([
                            ('product_tmpl_id', '=', self.id), ('product_id', '=', product.id),
                            ('pricelist_id', '=', sale_order_pricelist_id.id)
                        ])

                if pricelist_item_ids:
                    qty = min(pricelist_item_ids.mapped('min_quantity'))
                    is_possible_combination = self._is_combination_possible(combination)
                    cell.sort()
                    result.append({
                        "ptav_ids": cell,
                        "qty": '',
                        'placeholder_qty': qty,
                        "is_possible_combination": is_possible_combination
                    })
                else:
                    is_possible_combination = self._is_combination_possible(combination)
                    cell.sort()
                    result.append({
                        "ptav_ids": cell,
                        "qty": 0,
                        "placeholder_qty": '',
                        "is_possible_combination": is_possible_combination
                    })
            matrix.append(result)

        return {
            "header": header,
            "matrix": matrix,
        }
