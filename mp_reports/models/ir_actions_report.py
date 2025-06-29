# -*- coding: utf-8 -*-
from collections import OrderedDict
from zlib import error as zlib_error
try:
    from PyPDF2.errors import PdfStreamError, PdfReadError
except ImportError:
    from PyPDF2.utils import PdfStreamError, PdfReadError

from odoo import models, _
from odoo.exceptions import UserError
from odoo.tools import pdf


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    def _render_qweb_pdf(self, report_ref, res_ids=None, data=None):
        if report_ref == 'sale.report_saleorder_pro_forma':
            so = self.env['sale.order'].browse(res_ids)
            if any(s.state in ['draft', 'sent', 'cancel'] for s in so):
                raise UserError(_("Please confirm Sale Order to download PRO-FORMA."))
            so.write({'is_proforma_downloaded': True})
        return super()._render_qweb_pdf(report_ref, res_ids=res_ids, data=data)
