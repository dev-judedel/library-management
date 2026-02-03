# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class LibraryController(http.Controller):

    @http.route('/library/books', type='http', auth='public', website=True)
    def library_books(self, **kwargs):
        """Display all library books"""
        # Fetch all active books
        books = request.env['library.management'].sudo().search([])
        
        # Render template with books data
        return request.render('library_management.library_books_template', {
            'books': books,
        })

    @http.route('/mybooks', type='http', auth='user', website=True)
    def my_books(self, **kwargs):
        """Display books authored by the logged-in user's contact"""
        partner = request.env.user.partner_id
        books = request.env['library.management'].sudo().search([
            ('author_ids', 'in', partner.id),
        ])
        return request.render('library_management.library_my_books_template', {
            'books': books,
            'partner': partner,
        })
