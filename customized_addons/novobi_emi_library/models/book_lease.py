from odoo import api, models, fields

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

    def notify_expired(self):
        print('Notifying about lease expiration')
