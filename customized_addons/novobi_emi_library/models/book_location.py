from odoo import api, models, fields


class BookLocation(models.Model):
    _name = "library.book_location"
    _description = "Book Location"

    name = fields.Char('Name')
    books = fields.One2many('library.book', 'location', string="Books")
    total_available_books = fields.Integer()
    total_books = fields.Integer(compute='_compute_total_books')

    @api.depends('books')
    def _compute_total_books(self):
        self.total_books = len(self.books)
