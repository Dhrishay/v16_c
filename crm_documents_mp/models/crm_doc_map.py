from odoo import models, fields, api

class CrmDocMap(models.Model):
    _name = 'crm.doc.map'
    _description = 'CRM Documents Mapping'

    name = fields.Char(string='Name', required=True)
    folder_id = fields.Many2one('documents.folder',ondelete="cascade", tracking=True)
    document_ids = fields.One2many('documents.document', 'crm_id', string='CRM Documents')

    _sql_constraints = [
        ("uniq_type_of_document", "unique(name)", "Type Of Document Must Be Unique")
    ]