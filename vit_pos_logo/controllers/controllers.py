# -*- coding: utf-8 -*-
from odoo import http

# class VitPosLogo(http.Controller):
#     @http.route('/vit_pos_logo/vit_pos_logo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_pos_logo/vit_pos_logo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_pos_logo.listing', {
#             'root': '/vit_pos_logo/vit_pos_logo',
#             'objects': http.request.env['vit_pos_logo.vit_pos_logo'].search([]),
#         })

#     @http.route('/vit_pos_logo/vit_pos_logo/objects/<model("vit_pos_logo.vit_pos_logo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_pos_logo.object', {
#             'object': obj
#         })