from odoo.http import request

from odoo import http


class BookController(http.Controller):
    # echo '{}' | http  http://localhost:8069/novobi_emi_library/books
    @http.route('/novobi_emi_library/books', type='json', auth='none')
    def list(self, **kw):
        books = request.env['library.book'].sudo().search([])
        return books.read(['id', 'name', 'isbn'])


    @http.route('/novobi_emi_library/books/<model("novobi_library_book.library_book"):book>', auth='public')
    def object(self, book, **kw):
        return http.request.render('novobi_emi_library.object', {
            'object': book
        })
