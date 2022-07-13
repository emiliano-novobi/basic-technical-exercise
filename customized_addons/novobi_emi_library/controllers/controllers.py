# -*- coding: utf-8 -*-
# from odoo import http


# class NovobiEmiLibrary(http.Controller):
#     @http.route('/novobi_emi_library/novobi_emi_library', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/novobi_emi_library/novobi_emi_library/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('novobi_emi_library.listing', {
#             'root': '/novobi_emi_library/novobi_emi_library',
#             'objects': http.request.env['novobi_emi_library.novobi_emi_library'].search([]),
#         })

#     @http.route('/novobi_emi_library/novobi_emi_library/objects/<model("novobi_emi_library.novobi_emi_library"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('novobi_emi_library.object', {
#             'object': obj
#         })
