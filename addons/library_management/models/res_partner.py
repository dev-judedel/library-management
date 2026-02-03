# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Reverse Many2many - shows all books where this partner is an author
    my_book_ids = fields.Many2many(
        'library.management',
        'library_management_author_rel',
        'partner_id',
        'book_id',
        string='My Book',
    )
