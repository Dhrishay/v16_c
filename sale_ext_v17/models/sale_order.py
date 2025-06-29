from odoo import fields, models, api
from odoo.exceptions import UserError



class SaleOrder(models.Model):
     _inherit = 'sale.order'

     discount_apply = fields.Boolean(string='Discount Applied', default=False)

     # Task 1: create a 50% discount invoice from sale order with down payment
     # def action_confirm(self):
     #      print("\n\n\naction_confirm-----------------------")
     #      res = super(SaleOrder, self).action_confirm()
     #      for order in self:
     #           if order.amount_total > 0:
     #                order._create_50_percent_downpayment()
     #      return res
     #
     # def _create_50_percent_downpayment(self):
     #      print("\n\n\n_create_50_percent_downpayment-------------------")
     #      dw = self.env['sale.advance.payment.inv'].with_context(active_ids=self.ids).create({
     #           'advance_payment_method': 'percentage',
     #           'amount': 50.0
     #      })
     #      result = dw.create_invoices()
     #      print("result--------------------",result)
     #      invoice_ids = self.env['account.move'].search([
     #           ('invoice_origin', '=', self.name),
     #           ('move_type', '=', 'out_invoice'),
     #           ('state', '=', 'draft')
     #      ])
     #      for invoice in invoice_ids:
     #           invoice.action_post()

     # Task 2 Merge sale order line if prooducts is same

     # def merge_product(self):
     #      print("\n\n\nmerge_product------------------------------")
     #      order_lines = self.order_line
     #      print("order_lines--------------------------",order_lines)
     #      product_qty = {}
     #      for line in order_lines:
     #           print("order------------------",line)
     #           if line.product_id in product_qty:
     #                product_qty[line.product_id] += line.product_uom_qty
     #           else:
     #                product_qty[line.product_id] = line.product_uom_qty
     #      print("product_qty---------------------",product_qty)
     #      remove_product = self.env['sale.order.line']
     #      merge_product_lst = []
     #      for product, qty in product_qty.items():
     #           print("product--------------------",product)
     #           # print("qty--------------------",qty)
     #           line_to_merge = order_lines.filtered(lambda l: l.product_id.id == product.id)
     #           print("line_to_merge-----------------------",line_to_merge)
     #           print("line_to_merge-----------------------",line_to_merge[0])
     #           if len(line_to_merge) > 1 and line_to_merge[0].product_id.id == product.id:
     #                print("if------------------")
     #                merge_product_lst.append(line_to_merge[0].product_id.id)
     #                print("merge_product_lst----------------------",merge_product_lst)
     #                merge_line = line_to_merge[0]
     #                print("merge_line-------111---------------",merge_line)
     #                merge_line.product_uom_qty = qty
     #                print("merge_line-------222---------------",merge_line)
     #                remove_product += line_to_merge[1:]
     #      remove_product.unlink()

     # def merge_products(self):
     #      print("\n\n\nmerge_products----------------------------------")
     #      order_lines = self.order_line
     #      # print("order_lines--------------",order_lines)
     #      product_qty = {}
     #      # print("product_qty======================",product_qty)
     #      for line in order_lines:
     #           # print("line------------------",line)
     #           # print("product_qty===========111===========", product_qty)
     #           # print("line.product_id===========111===========", line.product_id)
     #           if line.product_id in product_qty:
     #                # print("if----------------")
     #                product_qty[line.product_id] += line.product_uom_qty
     #           else:
     #                # print("Else--------------")
     #                product_qty[line.product_id] = line.product_uom_qty
     #      print("product_qty----------------------------",product_qty)
     #      self.order_line.unlink()
     #      new_lines = []
     #      for product, qty in product_qty.items():
     #           print("product-----------------------",product)
     #           print("qty-----------------------",qty)
     #           new_lines.append((0, 0,{
     #                'product_id': product.id,
     #                'product_uom_qty': qty
     #           }))
     #      self.order_line = new_lines

     # Task 3 Apply discount

     # @api.onchange('order_line')
     # def _onchange_discount_applied(self):
     #      print("\n\n\n_onchange_discount_applied---------------------")
     #      self._apply_discount_logic()
     #
     # @api.model_create_multi
     # def create(self, vals_list):
     #      print("\n\n\ncreate-----------------------------")
     #      res = super().create(vals_list)
     #      res._apply_discount_logic_on_records()
     #      return res
     #
     # def write(self, vals):
     #      print("\n\n\nwrite0-----------------------------")
     #      res = super().write(vals)
     #      self._apply_discount_logic_on_records()
     #      return res
     #
     # def _apply_discount_logic(self):
     #      print("\n\n\n_onchange_discount_applied----------------------------")
     #      for order in self:
     #           total = sum(line.price_unit * line.product_uom_qty for line in order.order_line)
     #           if total > 1000 and not order.discount_apply:
     #                order.order_line.write({'discount': 10.0})
     #                order.discount_apply = True
     #           elif total <= 1000 and order.discount_apply:
     #                order.order_line.write({'discount': 0.0})
     #                order.discount_apply = False

     # @api.model_create_multi
     # def create(self, vals_list):
     #      print("\n\n\ncreate------------------------------")
     #      res = super().create(vals_list)
     #      print("res-----------------------------", res)
     #      total = sum(line.price_unit * line.product_uom_qty for line in res.order_line)
     #      print("total-----------------------------",total)
     #      if total > 1000 and not self.discount_apply:
     #           print("if 111111111111111111111")
     #           res.order_line.write({'discount': 10.0})
     #           res.discount_apply = True
     #      elif total <= 1000 and res.discount_apply:
     #           res.order_line.write({'discount': 0.0})
     #           res.discount_apply = False
     #      return res
     #
     # def write(self, vals):
     #      print("\n\n\nwrite----------------------------------")
     #      res = super().write(vals)
     #      # self._apply_discount_logic_on_records()
     #      total = sum(line.price_unit * line.product_uom_qty for line in self.order_line)
     #      print("total------------------------",total)
     #      if total > 1000:
     #           self.order_line.write({'discount': 10.0})
     #           # self.discount_apply = True
     #      elif total <= 1000:
     #           self.order_line.write({'discount': 0.0})
     #      return res

     # Task 4: Override the action_confirm method to send an email or do additional checks.

     def action_confirm(self):
          print("\n\n\naction_confirm------------------------------")
          for order in self:
               if not order.partner_id.email:
                    raise UserError("Enter the customer email")
               template = self.env.ref("sale_ext.mail_template_sale_order_confirmed")


