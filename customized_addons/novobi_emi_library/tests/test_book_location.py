from odoo.tests.common import TransactionCase

class BookLocationTest(TransactionCase):
    def setUp(self):
        super(BookLocationTest, self).setUp()

        self.vlad_the_impaler = self.env['res.partner'].create({'name': 'Vlad the Impaler'})
        self.location1 = self.env['library.book_location'].create({'name': 'Location 1'})

    def test_adding_book_should_increase_total_book_count(self):
        book = self.env['library.book'].create({
            'name': 'Book 1000',
            'short_name': 'B1000',
            'isbn': 1000,
            'author_ids': self.vlad_the_impaler,
            'location': self.location1.id
        })

        self.assertEquals(1, self.location1.total_books)
