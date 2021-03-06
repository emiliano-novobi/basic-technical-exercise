# -*- coding: utf-8 -*-
{
    'name': "Novobi: Emi Library",
    'summary': """
        Book Library customizations
    """,
    'description': """
        Book Library customizations
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'novobi_library_book'],
    'data': [
        'data/ir_cron_data.xml',
        'security/groups.xml',
        'security/record_rules.xml',
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/book_location_views.xml',
        'views/templates.xml',
        'report/book_location_report.xml',
        'report/book_location_template.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'auto_install': True
}
