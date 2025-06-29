# -*- coding: utf-8 -*-
{
    'name': "mp_reports",

    'summary': """MechPower Reports""",

    'description': """MechPower Reports""",

    'author': "",
    'website': "",

    'category': 'Purchase',
    'version': '16.0.0',
    'license': 'OPL-1',
    'depends': ['purchase_discount'],

    'data': [
        'data/product_template_data.xml',
        'report/report_purchaseorder.xml',
        'report/report_purchaseorder_rfq.xml',
        'views/res_company_views.xml',
        'views/sale_order_views.xml',
    ],
}
