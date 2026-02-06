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
    'website': 'https://www.example.com',
    'depends': ['base', 'web', 'website', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/library_management_demo.xml',
        'views/library_management_views.xml',
        'views/library_management_menus.xml',
        'views/library_books_template_clean.xml',  # Clean version with external CSS/JS
        #'views/library_books_template.xml',  # Old version with inline styles
        'views/library_books_enhanced_template.xml',
        'views/res_partner_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'library_management/static/src/css/library_books.css',
            'library_management/static/src/css/book_details.css',
            'library_management/static/src/js/book_details.js',
        ],
        'web.assets_backend': [
            'library_management/static/src/js/isbn_mask_backend.js',
            'library_management/static/src/js/save_toast_backend.js',
        ],
    },
    'demo': [
        'data/library_management_demo.xml',
    ],
  
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

