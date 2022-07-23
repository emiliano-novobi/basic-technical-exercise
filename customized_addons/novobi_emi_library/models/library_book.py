from datetime import date
from odoo import api, models, fields
from odoo.exceptions import ValidationError

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

    @api.constrains('isbn')
    def _check_unique_isbn(self):
        other_books_with_same_isbn = self.search([('id', '!=', self.id), ('isbn', '=', self.isbn)])

        if len(other_books_with_same_isbn) > 0:
            raise ValidationError(f"Existing ISBN {self.isbn} for this book: {other_books_with_same_isbn[0].name}")

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

    def mark_as_lost(self):
        self.status = 'lost'
        self.current_borrower = False
        self.return_date = False

    def is_lost(self):
        return self.status == 'lost'

    @api.onchange('date_release')
    def _onchange_date_release(self):
        if self.date_release is False:
            return

        if self.date_release > date.today():
            self.status = 'not_published'
