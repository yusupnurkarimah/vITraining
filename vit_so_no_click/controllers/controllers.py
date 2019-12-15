# -*- coding: utf-8 -*-
from odoo import http

# class VitSoNoClick(http.Controller):
#     @http.route('/vit_so_no_click/vit_so_no_click/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_so_no_click/vit_so_no_click/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_so_no_click.listing', {
#             'root': '/vit_so_no_click/vit_so_no_click',
#             'objects': http.request.env['vit_so_no_click.vit_so_no_click'].search([]),
#         })

#     @http.route('/vit_so_no_click/vit_so_no_click/objects/<model("vit_so_no_click.vit_so_no_click"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_so_no_click.object', {
#             'object': obj
#         })