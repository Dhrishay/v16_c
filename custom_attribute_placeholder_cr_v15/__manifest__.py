# -*- coding:utf-8 -*-

{
    'name': "Custom Attribute Placeholder Cr",
    'description': """ Custom Attribute Placeholder Cr  """,
    'category': 'Product',
    'version': '15.0.0',
    'depends': ['product_matrix', 'sale_product_matrix', 'sale_management', 'account', 'account_tax_python'],
    'data': [
        'reports/report_menu.xml',
        'data/pro_forma_mail_attachment.xml',
        'data/mail_template_sale.xml',
        'data/mail_template_invoice.xml',
        'views/product_attribute_value.xml',
        'views/account_settings_view.xml',
        'reports/invoice_simple_report.xml',
        'reports/sale_order_simple_report.xml',
        'reports/pro_forma_invoice_simple_report.xml',
        'reports/sale_order.xml',
        'reports/account_invoice.xml'
    ],
    "author": "CandidRoot Solutions",
    "website": "https://candidroot.com/",
    'assets': {
        'web.assets_backend': [
            'custom_attribute_placeholder_cr/static/src/css/placeholder_text_change.css'
        ],
        'web.assets_qweb': [
            'custom_attribute_placeholder_cr/static/src/xml/product_matrix.xml',
            'custom_attribute_placeholder_cr/static/src/xml/account_tax_totals.xml',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}