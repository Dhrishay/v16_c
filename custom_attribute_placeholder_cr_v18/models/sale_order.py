# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, _
import json
from odoo.tools.misc import formatLang


class SaleOrder(models.Model):
	_inherit = "sale.order"
	
	cost = fields.Float("Cost")
	sale_tax = fields.Float("Sale tax")

	# done
	@api.depends('order_line.price_total')
	def _compute_amounts(self):
		print("\n\n\ndef _compute_amounts(self):------------------2nd-------------------------------")
		"""
        Compute the total amounts of the SO.
        """
		office_cost_feature = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.office_cost') or False

		cost_percentage = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.percentage') or False

		max_amount = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.max_amount') or False

		cost_percent = float(cost_percentage)
		maximum_amount = float(max_amount)

		extra_amount = 0
		for order in self:
			amount_untaxed = amount_tax = 0.0
			for line in order.order_line:
				amount_untaxed += line.price_subtotal
				amount_tax += line.price_tax
			if office_cost_feature and cost_percentage:
				amount_cost_perc = amount_untaxed * cost_percent / 100
				extra_amount = maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc
			order.update({
				'amount_untaxed': amount_untaxed ,
				'amount_tax': amount_tax,
				'amount_total': amount_untaxed + amount_tax + extra_amount,
			})

	@api.depends('order_line.tax_id', 'order_line.price_unit', 'amount_total', 'amount_untaxed')
	def _compute_tax_totals_json(self):
		print("\n\n\n_compute_tax_totals_json--------------------------------------------------")
		total_lines = len(self.order_line.filtered(lambda line: line.tax_id))
		context_dict = {'total_lines': total_lines}

		def compute_taxes(order_line):
			price = order_line.price_unit * (1 - (order_line.discount or 0.0) / 100.0)
			order = order_line.order_id
			return order_line.tax_id._origin.with_context(context_dict).compute_all(price, order.currency_id, order_line.product_uom_qty,
														 product=order_line.product_id,
														 partner=order.partner_shipping_id)

		account_move = self.env['account.move']
		for order in self:
			tax_lines_data = account_move._prepare_tax_lines_data_for_totals_from_object(order.order_line, compute_taxes)
			tax_totals = account_move._get_tax_totals(order.partner_id, tax_lines_data, order.amount_total,
													  order.amount_untaxed, order.currency_id)
			order.tax_totals_json = json.dumps(tax_totals)



		office_cost_feature = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.office_cost') or False

		cost_percentage = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.percentage') or False

		max_amount = self.env['ir.config_parameter'].sudo().get_param('custom_attribute_placeholder_cr.max_amount') or False

		cost_percent = float(cost_percentage)
		maximum_amount = float(max_amount)

		for rec in self:
			currency = rec.company_id.currency_id
			tax_totals_json_dict = json.loads(rec.tax_totals_json)
			amount_total = tax_totals_json_dict['amount_total']
			amount_untaxed = tax_totals_json_dict['amount_untaxed']
			list_dict = {}

			# OFFICE COST PERCENT CALCULATION BASED ON THE UNTAXED AMOUNT
			if office_cost_feature and cost_percentage:
				final_deducted_amount = tax_totals_json_dict['amount_total']
				tax_totals_json_dict['deducted_amount'] = final_deducted_amount
				tax_totals_json_dict['formatted_deducted_amount'] = formatLang(self.env, final_deducted_amount, currency_obj=currency)

				formated_percentage = int(cost_percent) if cost_percent.is_integer() else cost_percent
				tax_totals_json_dict['cost_feature'] = True

				rec.cost = tax_totals_json_dict['amount_untaxed'] + tax_totals_json_dict['amount_untaxed'] * cost_percent / 100

				amount_cost_perc = tax_totals_json_dict['amount_untaxed'] * cost_percent / 100
				total_tax_amount = tax_totals_json_dict['amount_total'] - tax_totals_json_dict['amount_untaxed']
				total_tax_amount_perc = total_tax_amount * cost_percent / 100
				if amount_cost_perc > maximum_amount:
					amount_cost_perc = maximum_amount

				custom_tax_amount = amount_cost_perc + amount_untaxed + total_tax_amount_perc
				# PASSING NEW DICTINORY IN TO THE SUBTOTAL PORTION
				office_cost_string = "Office Cost " + str(formated_percentage) + '%'
				if amount_cost_perc > maximum_amount:

					mod_amount_untaxed = tax_totals_json_dict['amount_untaxed']
					maximum_limit = maximum_amount
					mod_cost_percent = cost_percent
					# mod_amount_untaxed = maximum_amount

					final_tax_amount = (mod_amount_untaxed + maximum_limit) * mod_cost_percent / 100
					list_dict = {
						"tax_group_name": office_cost_string,
						"tax_group_amount": maximum_amount,
						"tax_group_base_amount": amount_untaxed,
						"formatted_tax_group_amount": formatLang(self.env, maximum_amount,
																 currency_obj=currency),
						"formatted_tax_group_base_amount": tax_totals_json_dict['formatted_amount_untaxed'],
					}
					# tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0][
					# 	'tax_group_amount'] = final_tax_amount
					# tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0][
					# 	'formatted_tax_group_amount'] = formatLang(self.env, final_tax_amount,
					# 											   currency_obj=currency)
					tax_totals_json_dict['groups_by_subtotal1'] = {'Untaxed Amount1': []}
					tax_totals_json_dict['groups_by_subtotal1']['Untaxed Amount1'].append(list_dict)

				else:
					list_dict = {
						"tax_group_name": office_cost_string,
						"tax_group_amount": amount_cost_perc,
						"tax_group_base_amount": amount_untaxed,
						"formatted_tax_group_amount": formatLang(self.env, amount_cost_perc,
																 currency_obj=currency),
						"formatted_tax_group_base_amount": tax_totals_json_dict['formatted_amount_untaxed'],

					}
					tax_totals_json_dict['groups_by_subtotal1'] = {'Untaxed Amount1': []}
					tax_totals_json_dict['groups_by_subtotal1']['Untaxed Amount1'].append(list_dict)
				# IF SUBTOTAL WITH TAX THEN THIS CONDITION WILL BE EXCECUTE
				# THIS CODE WILL BE INCRESE THE TAX WITH OFFICE COST PERCENTAGE
				if tax_totals_json_dict.get('groups_by_subtotal', False):
					if tax_totals_json_dict.get('groups_by_subtotal', False).get('Untaxed Amount', False):
						if tax_totals_json_dict.get('groups_by_subtotal', False).get('Untaxed Amount', False)[0].get(
								'tax_group_amount', False):
							# TAX + OFFICE TAX CALCULATION
							# TAX GROUP AMOUNT + COST PERCENTAGE
							# CUSTOM FORMATE FOR ORIGINAL INVOICE
							tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0][
								'formatted_tax_group_base_amount_custom'] = formatLang(self.env, tax_totals_json_dict[
								'groups_by_subtotal']['Untaxed Amount'][0]['tax_group_amount'],
																					   currency_obj=currency)

							tax = tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0]['tax_group_amount']

							old_tax_group_base_amount = tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0][
								'tax_group_base_amount']

							new_tax_base_amount = old_tax_group_base_amount + (
								maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc)


							tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0][
								'formatted_tax_group_base_amount'] = formatLang(self.env, new_tax_base_amount,
																				currency_obj=currency)

							total_tax = 0.0
							for taxes in tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount']:
								if taxes.get('tax_group_amount', False):
									total_tax += float(taxes.get('tax_group_amount'))

							# FINAL TOTAL CALCULATION
							# tax_totals_json_dict['amount_total'] = amount_untaxed + (maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc) + tax_totals_json_dict['groups_by_subtotal']['Untaxed Amount'][0]['tax_group_amount']
							# tax_totals_json_dict['amount_total'] = amount_untaxed + (
							# 	maximum_amount if amount_cost_perc > maximum_amount else amount_cost_perc) + total_tax
							# tax_totals_json_dict['formatted_amount_total'] = formatLang(self.env, tax_totals_json_dict[
							# 	'amount_total'],
							# 															currency_obj=currency)
				# else:
				# 	tax_totals_json_dict['amount_total'] = custom_tax_amount
				# 	tax_totals_json_dict['formatted_amount_total'] = formatLang(self.env,
				# 																tax_totals_json_dict['amount_total'],
				# 																currency_obj=currency)

				rec.tax_totals_json = json.dumps(tax_totals_json_dict)


	def action_quotation_send(self):
		print("\n\n\naction_quotation_send------------------------------------------------")
		''' Opens a wizard to compose an email, with relevant mail template loaded by default '''
		self.ensure_one()
		template_id = self._find_mail_template()
		lang = self.env.context.get('lang')
		new_email_temp_id = self.env.ref('custom_attribute_placeholder_cr.email_template_edi_sale_custom')
		template = self.env['mail.template'].browse(new_email_temp_id.id)
		if template.lang:
			lang = template._render_lang(self.ids)[self.id]
		ctx = {
			'default_model': 'sale.order',
			'default_res_id': self.ids[0],
			'default_use_template': bool(new_email_temp_id.id),
			'default_template_id': new_email_temp_id.id,
			'default_composition_mode': 'comment',
			'mark_so_as_sent': True,
			'custom_layout': "mail.mail_notification_paynow",
			'proforma': self.env.context.get('proforma', False),
			'force_email': True,
			'model_description': self.with_context(lang=lang).type_name,
		}
		return {
			'type': 'ir.actions.act_window',
			'view_mode': 'form',
			'res_model': 'mail.compose.message',
			'views': [(False, 'form')],
			'view_id': False,
			'target': 'new',
			'context': ctx,
		}

	def _compute_custom_tax(self):
		print("\n\n\n_compute_custom_tax----------------------------------------")
		currency = self.env.company.currency_id

		# For the computation of move lines, we could have a negative base value.
		# In this case, compute all with positive values and negate them at the end.

		total_tax = 0.0
		amount_total = 0.0
		amount_untaxed = 0.0

		basic_taxes = {}
		for line in self.order_line:
			price_unit = line.price_unit
			quantity = line.product_uom_qty
			base = currency.round(price_unit * quantity)
			amount_untaxed += base
			amount_total += base
			sign = 1
			if currency.is_zero(base):
				sign = self._context.get('force_sign', 1)
			elif base < 0:
				sign = -1
			if base < 0:
				base = -base
			for tax in line.tax_id:
				product = None
				partner = None
				quantity = 1
				total_tax += tax.with_context(force_price_include=False)._compute_amount(base, sign * price_unit, quantity, product, partner, custom=True)
		amount_total = amount_untaxed + total_tax

		basic_taxes['mod_total_tax'] = total_tax
		basic_taxes['mod_total_tax_format'] = formatLang(self.env, total_tax, currency_obj=currency)

		basic_taxes['mod_amount_total'] = amount_total

		basic_taxes['mod_amount_total_format'] = formatLang(self.env, amount_total, currency_obj=currency)

		basic_taxes['mod_amount_untaxed'] = amount_untaxed

		basic_taxes['mod_amount_untaxed_format'] = formatLang(self.env, amount_untaxed, currency_obj=currency)

		''

		return basic_taxes

