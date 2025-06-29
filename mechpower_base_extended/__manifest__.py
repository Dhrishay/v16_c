# -*- coding: utf-8 -*-
{
    'name': "MechPower Base Extended",
    'summary': """MechPower Base Extended""",

    'description': """
        MechPower Base Extended
    """,

    'version': '16.0.1',
    'qweb': [
    ],
    'depends': ['base', 'mrp', 'sale', 'account', 'delivery', 'stock', 'helpdesk', 'project', 'website_blog','portal', 'crm', 'purchase_stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/demo.xml',
        'data/data.xml',
        'data/helpdesk_mail_template.xml',
        'data/sigup_mail_template.xml',
        'views/res_users.xml',
        'views/res_partner_views.xml',
        'views/custom_report.xml',
        'views/close_reason.xml',
        'views/sale_order.xml',
        'views/stock_picking.xml',
        'views/customer_files.xml',
        'views/project.xml',
        'views/quality.xml',
        'views/blog_post.xml',
        'views/template.xml',
        'views/helpdesk_ticket.xml',
        'views/crm_lost_reason.xml',
        'views/crm_lead.xml',
        'views/ir_mail_server.xml',
        'views/purchase_order_view.xml',
        'wizard/sale_close_reason_wizard_views.xml',
        'wizard/partner_mail_list_wizard.xml',
    ],
    'demo': [
    ],
    'assets': {
        'mail.assets_messaging': [
            # 'mechpower_base_extended/static/src/models/*.js',
        ],
        "web.assets_backend": [
            "mechpower_base_extended/static/src/js/hide_action_archive_form.js",
            "mechpower_base_extended/static/src/js/hide_action_archive_list.js",
            "mechpower_base_extended/static/src/scss/style.scss",
        ],
        "web.assets_frontend": [
            "mechpower_base_extended/static/src/js/snippet_animation.js",
        ]
    },
}
