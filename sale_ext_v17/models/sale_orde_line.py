from odoo import models, fields, api


class SaleOrderLine(models.Model):
     _inherit = 'sale.order.line'

     # @api.model_create_multi
     # def create(self, vals_list):
     #      print("\n\n\ncreate-----------------------------------")
     #      res = super(SaleOrderLine, self).create(vals_list)
     #      print("res----------------------------",res)
     #      print("vals_list--------------------------",vals_list)
     #      print("vals_list--------------------------",vals_list[0])
     #      if 'order_id' in vals_list[0] and 'product_id' in vals_list[0]:
     #           print("if 1111111111")
     #           order = self.env['sale.order'].browse(vals_list[0]['order_id'])
     #           print("order-------------------------",order)
     #           product_id = vals_list[0]['product_id']
     #           print("product_id---------------------",product_id)
     #           for line in order.order_line:
     #                print("line----------------------",line.product_id.id)
     #                if line.product_id.id == product_id:
     #                     print("True-----------------------")
     #                # for l in line.order_line:
     #                #      print("l--------------",l)
     #           existing_line = order.order_line.filtered(lambda l: l.product_id.id == product_id and not l.display_type)
     #           print("existing_line-----------------------------",existing_line)
     #           if existing_line:
     #                existing_line = existing_line[0]
     #                print("existing_line--------------------",existing_line)
     #                existing_line.product_uom_qty += vals_list[0].get('product_uom_qty', 1)
     #                print("existing_line--------------------", existing_line)
     #                return existing_line
     #      return super(SaleOrderLine, self).create(vals_list)