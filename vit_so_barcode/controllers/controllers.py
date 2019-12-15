# -*- coding: utf-8 -*-
from odoo import http

# class VitSoBarcode(http.Controller):
#     @http.route('/vit_so_barcode/vit_so_barcode/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_so_barcode/vit_so_barcode/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_so_barcode.listing', {
#             'root': '/vit_so_barcode/vit_so_barcode',
#             'objects': http.request.env['vit_so_barcode.vit_so_barcode'].search([]),
#         })

#     @http.route('/vit_so_barcode/vit_so_barcode/objects/<model("vit_so_barcode.vit_so_barcode"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_so_barcode.object', {
#             'object': obj
#         })