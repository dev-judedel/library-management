# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryManagement(models.Model):
    _name = 'library.management'
    _description = 'Library Management'
    _rec_name = 'title'

    # Fields as per requirements
    #rule 2
    image = fields.Image(string='Cover')
    title = fields.Char(string='Title' , default='Field') # aalisin ung true pag need makita ung rules 7.1
    isbn = fields.Char(string='ISBN')
    active = fields.Boolean(string='Active', default=True)
    date_published = fields.Date(string='Date Published')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many(
        'res.partner',
        'library_management_author_rel',
        'book_id',
        'partner_id',
        string='Authors',
    )
    webpage_link = fields.Char(string='Wikipage Link') # additional field for webpage link part 2

    # Method to check ISBN (called by button)
    # Validation method for ISBN
    #Create a function that will check/validate IF 
    # ISBN is a number and is 13 digit 
    #Then follow the validation instruction at number 7.
    def action_check_isbn(self):
        """Check ISBN validation when button is clicked"""
        self.ensure_one()
        self._validate_isbn()
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Success',
                'message': 'ISBN is valid!',
                'type': 'success',
                'sticky': False,
            }
        }

  
    def _validate_isbn(self):
        """Validate ISBN format and length"""
        for record in self:
            # Check if ISBN is empty
            #7.2
            # raise ValidationError if you attempted to press Check ISBN button or saving the record and the ISBN field is empty ,
            # raise a message “Please provide an ISBN for <bookname>
            if not record.isbn:
                raise ValidationError(f"Please provide an ISBN for {record.title}")
            
            # Check if ISBN contains only digits
            #7.3
            if not record.isbn.isdigit():
                raise ValidationError("ISBN must be a digit")
            #7.3
            # Check if ISBN is exactly 13 digits
            if len(record.isbn) != 13:
                raise ValidationError("ISBN must be 13 digit")

    # Validation for required title
    #7.1 conflict sa required=True sa title field need to remove ung true pag need makita ung rules 7.1
    @api.constrains('title')
    def _check_title(self):
        """Validate that title is provided"""
        for record in self:
            if not record.title or not record.title.strip():
                raise ValidationError("Please provide a book name")

    # Override create to validate ISBN on save
    @api.model_create_multi
    def create(self, vals_list):
        """Override create to validate ISBN"""
        records = super(LibraryManagement, self).create(vals_list)
        for record in records:
            #if record.isbn:  # Only validate if ISBN is provided
                record._validate_isbn()
        return records

    # Override write to validate ISBN on update
    def write(self, vals):
        """Override write to validate ISBN"""
        result = super(LibraryManagement, self).write(vals)
        if 'isbn' in vals:
            for record in self:
                #if record.isbn:  # Only validate if ISBN is provided
                    record._validate_isbn()
        return result
