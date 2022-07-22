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