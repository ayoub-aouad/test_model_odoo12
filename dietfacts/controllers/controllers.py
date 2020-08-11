# -*- coding: utf-8 -*-
from odoo import http

# class Dietfacts(http.Controller):
#     @http.route('/dietfacts/dietfacts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dietfacts/dietfacts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dietfacts.listing', {
#             'root': '/dietfacts/dietfacts',
#             'objects': http.request.env['dietfacts.dietfacts'].search([]),
#         })

#     @http.route('/dietfacts/dietfacts/objects/<model("dietfacts.dietfacts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dietfacts.object', {
#             'object': obj
#         })