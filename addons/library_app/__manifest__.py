# -*- coding: utf-8 -*-
{
    'name': 'Library Management',
    'version': '1.0',
    'category': 'Library',
    'summary': 'Manage library books and records',
    'description': """
        Library Management System
        =========================
        This module allows you to:
        * Add and manage books
        * Track book details (ISBN, authors, publisher)
        * Validate ISBN format
        * Display books on website
    """,
    'author': 'Your Name',
    'website': '',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_app_views.xml',
        'views/library_app_menus.xml',
        'views/library_books_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
