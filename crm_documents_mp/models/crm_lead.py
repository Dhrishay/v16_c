from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = "crm.lead"

    document_ids = fields.One2many('documents.document', 'crm_id', string='CRM Documents')
