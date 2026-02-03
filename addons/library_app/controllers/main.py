# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class LibraryController(http.Controller):

    @http.route('/library/books', type='http', auth='public', website=True)
    def library_books(self, **kwargs):
        """Display all library books"""
        # Fetch all active books
        books = request.env['library.app'].sudo().search([])
        
        # Render template with books data
        return request.render('library_app.library_books_template', {
            'books': books,
        })
