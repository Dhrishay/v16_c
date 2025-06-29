{
    'name': 'Execute Query',
    'category': 'Tools',
    'version': '18.0.0.0',
    'author': "Candidroot Solutions Pvt. Ltd.",
    'website': 'https://www.candidroot.com/',
    'summary': 'Run custom SQL queries directly from the Odoo interface',
    'depends': ['base',  'base_setup'],
    'description': """
        This module allows developers and administrators to run raw SQL queries safely from within the Odoo backend interface.
        Features:
        - Execute read and write queries on database tables
        - Useful for debugging and administrative tasks
        - Provides a pop-up interface to run SQL scripts
        - Requires developer mode enabled
        """,
    'sequence': 35,
    'assets': {
        'web.assets_frontend': [
            'execute_query_cr/static/src/**/*',
        ],
        'web._assets_core': [
            'execute_query_cr/static/src/**/*',
        ],
        'web.assets_backend':[
             'execute_query_cr/static/src/**/*',
        ]
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
