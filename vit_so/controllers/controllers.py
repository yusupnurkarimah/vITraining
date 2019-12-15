# -*- coding: utf-8 -*-
from odoo import http

# class VitSo(http.Controller):
#     @http.route('/vit_so/vit_so/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_so/vit_so/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_so.listing', {
#             'root': '/vit_so/vit_so',
#             'objects': http.request.env['vit_so.vit_so'].search([]),
#         })

#     @http.route('/vit_so/vit_so/objects/<model("vit_so.vit_so"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_so.object', {
#             'object': obj
#         })