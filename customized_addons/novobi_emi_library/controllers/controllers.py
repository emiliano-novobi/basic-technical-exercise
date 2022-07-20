from odoo.http import request

from odoo import http


class BookController(http.Controller):
    # echo '{}' | http get http://localhost:8069/novobi_emi_library/books
    @http.route('/novobi_emi_library/books', methods=['GET'], type='json', auth='none')
    def list(self, **kw):
        books = request.env['library.book'].sudo().search([])
        return books.read(['id', 'name', 'isbn'])

    # echo '{}' | http get http://localhost:8069/novobi_emi_library/books/11
    @http.route('/novobi_emi_library/books/<int:book_id>', methods=['GET'], type='json', auth='none')
    def get_by_id(self, book_id, **kw):
        book = request.env['library.book'].sudo().browse([book_id])
        return book.read(['id', 'name', 'isbn'])

    # echo '{"name": "Book REST", "short_name": "BR", "isbn": 10 }' | http post http://localhost:8069/novobi_emi_library/books/create
    # @http.route('/novobi_emi_library/books/create/<model("novobi_library_book.library_book"):book>', methods=['POST'], auth='none')
    @http.route('/novobi_emi_library/books/create', methods=['POST'], type='json', auth='none')
    def create(self, **kw):
        request.env['library.book'].sudo().create(request.jsonrequest)
        return True
