# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartnerMyBook(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    # My Book mirrors the book author relation (same M2M table as author_ids).
    # Auto-reflects: changes on a book's authors show here immediately.
    my_book = fields.Many2many(
        'library.management',
        'library_management_author_rel',
        'partner_id',
        'book_id',
        string='My Book', # part2 rule 1
        readonly=True,
    )
