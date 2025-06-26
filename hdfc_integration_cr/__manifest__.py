{
    'name': 'HDFC Payment Acquirer',
    'version': '16.0.0.1',
    'summary': 'Payment Acquirer: HDFC Integration With Odoo',
    'description': """CandidRoot Solutions with a feature that introduce new 'Payment Acquirer' method named 'HDFC'. you can configure 'HDFC Merchant Code and 'HDFC Access Key and HDFC Working Key'. it is one of the payment acquirer like Stripe, PayUmoney, Paypal etc.""",
    'depends': ['payment', 'account', 'website_sale'],
    'images': '/hdfc_integration_cr/static/src/img/activation.png',
    "data": [
        "views/payment_provider_views.xml",
        "views/hdfc_templates.xml",
        "data/payment_provider_data.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
}
