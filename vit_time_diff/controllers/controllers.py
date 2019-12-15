# -*- coding: utf-8 -*-
from odoo import http

# class VitTimeDiff(http.Controller):
#     @http.route('/vit_time_diff/vit_time_diff/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_time_diff/vit_time_diff/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_time_diff.listing', {
#             'root': '/vit_time_diff/vit_time_diff',
#             'objects': http.request.env['vit_time_diff.vit_time_diff'].search([]),
#         })

#     @http.route('/vit_time_diff/vit_time_diff/objects/<model("vit_time_diff.vit_time_diff"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_time_diff.object', {
#             'object': obj
#         })