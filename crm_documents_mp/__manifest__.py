# -*- coding: utf-8 -*-
{
    'name': "MP CRM Documents Link",
    'summary': """MP CRM Documents Link""",

    'description': """
        MP CRM Documents Link
    """,

    'version': '16.0.1',
    'qweb': [
    ],
    'depends': ['documents', 'crm'],

    'data': [
        'security/ir.model.access.csv',
        'views/crm_doc_map_views.xml',
        'views/crm_lead_views.xml',
    ],
    'demo': [
    ],

}
