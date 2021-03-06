import datetime

from odoo.tests.common import TransactionCase


class BookTest(TransactionCase):
    def setUp(self):
        super(BookTest, self).setUp()

        self.vlad_the_impaler = self.env['res.partner'].create({'name': 'Vlad the Impaler'})
        self.location1 = self.env['library.book_location'].create({'name': 'Location 1'})

    def test_create_book(self):
        book = self.env['library.book'].create({
            'name': 'Book 1000',
            'short_name': 'B1000',
            'isbn': 1000,
            'author_ids': self.vlad_the_impaler,
            'location': self.location1.id
        })

        self.assertTrue(book.id is not None)

    def test_persist_lost(self):
        book = self.env['library.book'].create({
            'name': 'Book 1000',
            'short_name': 'B1000',
            'isbn': 1000,
            'author_ids': self.vlad_the_impaler,
            'location': self.location1.id,
            'current_borrower': self.vlad_the_impaler.id,
            'return_date': datetime.date.today()
        })

        lost_book = self.env['library.book'].search([
            ('isbn', '=', 1000)
        ])
        lost_book.mark_as_lost()

        persisted_lost_book = self.env['library.book'].search([
            ('isbn', '=', 1000)
        ])
        self.assertTrue(persisted_lost_book.is_lost())

    def test_mark_as_lost_should_clear_lease(self):
        book = self.env['library.book'].create({
            'name': 'Book 1000',
            'short_name': 'B1000',
            'isbn': 1000,
            'author_ids': self.vlad_the_impaler,
            'location': self.location1.id,
            'current_borrower': self.vlad_the_impaler.id,
            'return_date': datetime.date.today()
        })
        book.mark_as_lost()

        lost_book = self.env['library.book'].search([
            ('isbn', '=', 1000)
        ])
        self.assertFalse(lost_book.current_borrower)
        self.assertFalse(lost_book.return_date)
