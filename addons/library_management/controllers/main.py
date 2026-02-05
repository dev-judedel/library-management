# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class LibraryController(http.Controller):

    @http.route('/library/books', type='http', auth='public', website=True)
    def library_books(self, **kwargs):
        """Display all library books with enhanced browsing features"""
        # Fetch all active books
        books = request.env['library.management'].sudo().search([])
        
        # Get unique publishers for filter
        publishers = request.env['res.partner'].sudo().search([
            ('id', 'in', books.mapped('publisher_id').ids)
        ]).sorted('name')
        
        # Get unique authors for filter
        authors = request.env['res.partner'].sudo().search([
            ('id', 'in', books.mapped('author_ids').ids)
        ]).sorted('name')
        
        # Get date range
        dates = books.mapped('date_published')
        dates = [d for d in books.mapped('date_published') if d]
        date_range = {
            'min': min(dates) if dates else None,
            'max': max(dates) if dates else None
        }
        
        # Render enhanced template with filter data
        #return request.render('library_management.library_books_template', {
        return request.render('library_management.library_books_enhanced_template', {
            'books': books,
            'publishers': publishers,
            'authors': authors,
            'date_range': date_range,
        })

    @http.route('/mybooks', type='http', auth='user', website=True) #part2 rule 4
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
