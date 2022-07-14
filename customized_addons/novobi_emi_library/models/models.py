from odoo import models, fields


class LibraryBook(models.Model):
    _inherit = "library.book"

    isbn = fields.Char('ISBN', required=True)
    description = fields.Char('Description', required=False)
    status = fields.Selection(
        string='status',
        selection=[('not_published', 'Not Published'), ('available', 'Available'), ('borrowed', 'Borrowed'), ('lost', 'Lost')],
        help='Status',
        default='available'
    )
    current_borrower = fields.Many2one('res.partner', string='Current Borrower')
    return_date = fields.Date("Return Date")
    location = fields.Many2one("library.book_location", string="Location")

    def lease(self):
        return {
            'name': 'Lease',
            'view_mode': 'form',
            'res_model': 'library.book_lease',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': self.env.context,
        }


class BookLocation(models.Model):
    _name = "library.book_location"
    _description = "Book Location"

    name = fields.Char('Name')
    books = fields.One2many('library.book', 'location', string="Books")
    total_available_books = fields.Integer()


class BookLease(models.TransientModel):
    _name = "library.book_lease"
    _description = "Book Lease"

    book = fields.Many2one('library.book')
    borrower = fields.Many2one('res.partner', string='Borrower')
    return_date = fields.Date("Return Date", required=True)
