from odoo import api, models, fields
from datetime import date


class LibraryBook(models.Model):
    _name = "library.book"
    _inherit = ["library.book", "mail.thread"]

    isbn = fields.Char('ISBN', required=True)
    description = fields.Char('Description', required=False)
    status = fields.Selection(
        string='status',
        selection=[('not_published', 'Not Published'), ('available', 'Available'), ('borrowed', 'Borrowed'), ('lost', 'Lost')],
        help='Status',
        default='available'
    )
    current_borrower = fields.Many2one('res.partner', string='Current Borrower', tracking=True)
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

    def borrow_to(self, borrower):
        self.current_borrower = borrower
        self.status = 'borrowed'

    @api.onchange('date_release')
    def _onchange_date_release(self):
        if self.date_release.to_date() > date.today():
            self.status = 'not_published'


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

class BookLease(models.TransientModel):
    _name = "library.book_lease"
    _description = "Book Lease"

    book = fields.Many2one('library.book')
    borrower = fields.Many2one('res.partner', string='Borrower')
    return_date = fields.Date("Return Date", required=True)

    @api.model
    def create(self, values):
        created = super(BookLease, self).create(values)
        created.book = self.env.context['active_id']
        created.book.borrow_to(created.borrower)
        return created
