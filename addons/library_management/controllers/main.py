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

    @http.route('/book/<int:book_id>', type='http', auth='public', website=True)
    def book_details(self, book_id, **kwargs):
        """Display detailed information about a specific book"""
        # Fetch the book by ID
        book = request.env['library.management'].sudo().browse(book_id)
        
        # Check if book exists
        if not book.exists():
            return request.render('website.404')
        
        # Get related books by same authors (limit to 4)
        related_books = request.env['library.management'].sudo().search([
            ('author_ids', 'in', book.author_ids.ids),
            ('id', '!=', book_id),
        ], limit=4)
        
        # Render book details template
        return request.render('library_management.library_book_details_template', {
            'book': book,
            'related_books': related_books,
        })
