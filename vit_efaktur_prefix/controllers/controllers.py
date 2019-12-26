# -*- coding: utf-8 -*-
from odoo import http

# class VitEfakturPrefix(http.Controller):
#     @http.route('/vit_efaktur_prefix/vit_efaktur_prefix/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_efaktur_prefix/vit_efaktur_prefix/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_efaktur_prefix.listing', {
#             'root': '/vit_efaktur_prefix/vit_efaktur_prefix',
#             'objects': http.request.env['vit_efaktur_prefix.vit_efaktur_prefix'].search([]),
#         })

#     @http.route('/vit_efaktur_prefix/vit_efaktur_prefix/objects/<model("vit_efaktur_prefix.vit_efaktur_prefix"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_efaktur_prefix.object', {
#             'object': obj
#         })