from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    background_image = fields.Image('Background Image', attachment=True, store=True)
    background_image_path = fields.Char('Background Image Path')

    @api.onchange('background_image')
    def _onchange_background_image(self):
        print("\n\n\n_onchange_background_image----------------------------------------------------")
        if self.background_image:
            attachment = self.env['ir.attachment'].search([('res_model', '=', self._name),
                                                           ('res_id', '=', self.id),
                                                           ('name', '=', 'background_image')], limit=1)
            if attachment:
                self.background_image_path = attachment.store_fname

    @api.model_create_multi
    def create(self, vals):
        print("\n\n\ncreate--------------------------------------")
        if 'background_image' in vals:
            # Store the background image path after it's uploaded
            image_data = vals.get('background_image')
            # Simulating finding the image path (this part will be more complex depending on the storage)
            attachment = self.env['ir.attachment'].create({
                'name': 'background_image',
                'type': 'binary',
                'datas': image_data,
                'res_model': self._name,
                'res_id': vals.get('id', False),
            })
            vals['background_image_path'] = attachment.store_fname  # Set the path here
        return super(ResCompany, self).create(vals)

    def write(self, vals):
        print("\n\n\nwrite--------------------------------------------------------")
        if 'background_image' in vals:
            # Similar logic as create, but for updates
            image_data = vals.get('background_image')
            attachment = self.env['ir.attachment'].search([('res_model', '=', self._name),
                                                           ('res_id', '=', self.id),
                                                           ('name', '=', 'background_image')], limit=1)
            if attachment:
                attachment.write({
                    'datas': image_data,
                })
                vals['background_image_path'] = attachment.store_fname
        return super(ResCompany, self).write(vals)



