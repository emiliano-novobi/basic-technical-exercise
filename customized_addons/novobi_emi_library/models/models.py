# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class novobi_emi_library(models.Model):
#     _name = 'novobi_emi_library.novobi_emi_library'
#     _description = 'novobi_emi_library.novobi_emi_library'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields


class LibraryBook(models.Model):
    _inherit = "library.book"

    isbn = fields.Char('ISBN', required=True)
    description = fields.Char('Description', required=True)
    status = fields.Selection(
        string='status',
        selection=[('not_published', 'Not Published'), ('available', 'Available'), ('borrowed', 'Borrowed'), ('lost', 'Lost')],
        help='Status',
        default='available'
    )
    current_borrower = fields.Many2one("res.partner", string="Current Borrower")
    return_date = fields.Date("Return Date")
    location = fields.Many2one("book.location", string="Location")

class BookLocation(models.Model):
    _name = "book.location"
    _description = "Book Location"

    name = fields.Char('Name')
    books = fields.One2many('library.book', 'location', string="Books")
    total_available_books = fields.Integer()
