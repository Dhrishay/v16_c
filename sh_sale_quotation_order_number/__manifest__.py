# -*- coding: utf-8 -*-
{
    "name": "Separate Quotation No.",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "version": "16.0.1",
    "license": "OPL-1",
    "category": "Sales",
    "summary": """
separate quotation number,
seperate sale order number,
seperate sales order,
separate quotations app,
partition of sales order,
disjoint so module odoo
""",
    "description": """
Separate Quotation No. So easy to manage quotation and sale order no.
separate quotations app, partition of sales order, disjoint so module odoo
""",
    "depends": ["sale_management"],
    "data": [
        "data/sh_sale_quotation_order_number_demo.xml",
        "views/sale_views.xml",
        "reports/sale_reports.xml",
    ],
    "images": ["static/description/background.png", ],
    "auto_install": False,
    "installable": True,
    "application": True,
    "price": 15,
    "currency": "EUR"
}
