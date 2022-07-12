# Copyright © 2022 Novobi, LLC
# See LICENSE file for full copyright and licensing details.

{
    "name": "Novobi: Library Book",
    "summary": "Novobi: Library Book",
    "version": "15.0.1",
    "category": "Tools",
    "website": "https://novobi.com",
    "author": "Novobi, LLC",
    "license": "OPL-1",
    "depends": [
        "base", "mail"
    ],
    "excludes": [],
    "data": [
        # ============================== DATA =================================
        'data/mail_template_data.xml',

        # ============================== VIEWS ================================
        'views/library_book_views.xml',

        # ============================== SECURITY ================================
        'security/library_book_groups.xml',
        'security/ir.model.access.csv',

        # ============================== REPORT =============================
        'report/book_reports.xml',
        'report/book_templates.xml',
        # ============================== WIZARDS =============================  
        #           
    ],
    "application": True,
    "installable": True,
}
