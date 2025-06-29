{
    'name': 'Website - DataTile',
    'category': 'Website/Website',
    'description': """
    """,
    'summary': """
    """,
    'author': 'Candidroot Solution Pvt. Ltd.',
    'website': 'https://candidroot.com',
    'license': 'LGPL-3',
    'version': "18.0.2.0",
    'depends': ['website', 'crm'],
    'data': [
        "security/ir.model.access.csv",
        "data/dashboard_demo_data.xml",
        "data/common_config.xml",
        "views/dashboard.xml",

        "template/header.xml",
        "template/footer.xml",
        "template/homepage.xml",

        "template/platform.xml",
        "template/solutions.xml",
        "template/cases.xml",
        "template/contact_us.xml",
        "template/about_us.xml",
        "template/legal.xml",
        "template/pricing.xml",
        "template/web_layout.xml",
        "template/dashboard_gallary.xml",
        "template/dasboards.xml",
        # "template/cookies_bar.xml",
    ],
    'assets': {
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
            "website_dt/static/src/scss/header.scss",
            "website_dt/static/src/scss/footer.scss",
            "website_dt/static/src/scss/homepage.scss",
            "website_dt/static/src/scss/solutions.scss",
            "website_dt/static/src/scss/contact_us.scss",
            "website_dt/static/src/scss/about_us.scss",
            "website_dt/static/src/scss/cases.scss",
            "website_dt/static/src/scss/platform.scss",
            "website_dt/static/src/scss/pricing.scss",
            "website_dt/static/src/scss/sanbox_access.scss",
            "website_dt/static/src/scss/dashboard_gallary.scss",
            "website_dt/static/src/scss/media_query.scss",

            "website_dt/static/src/js/homepage.js",
        ],
    },
    'installable': True,
    'application': False,
}
# -*- coding: utf-8 -*-
