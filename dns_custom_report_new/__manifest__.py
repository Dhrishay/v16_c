# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Candidroot Solutions Pvt. Ltd.
{
    "name":"Custom report - DNS",
    "version":"16.0.0.0",
    "category": "Website",
    "author":"Candidroot Solutions pvt. ltd.",
    "website":"https://www.candidroot.com",
    "sequence":"2",
    "summary":"",
    "desription":"""
    """,
    "depends":["base", "web", "account", "sale_management"],
    "data" :[
        "views/dns_quotation_report.xml",
        "views/dns_invoice_report.xml",
        "views/dns_quotation_portal_content.xml",
        "views/res_company_view.xml"
        ],
    "assets": {
        "web.assets_frontend": [
            'dns_custom_report/static/src/scss/style.scss'
        ],
        'web.report_assets_common': [
            'dns_custom_report/static/src/scss/style.scss'

        ],
    },
    "installable": True,
    "auto_install": False,
    "application": True
}
