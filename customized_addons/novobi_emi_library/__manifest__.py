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
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/book_views.xml',
        'views/book_location_views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'auto_install': True
}
