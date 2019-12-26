# -*- coding: utf-8 -*-
from odoo import http

# class VitStagesInvoice(http.Controller):
#     @http.route('/vit_stages_invoice/vit_stages_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_stages_invoice/vit_stages_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_stages_invoice.listing', {
#             'root': '/vit_stages_invoice/vit_stages_invoice',
#             'objects': http.request.env['vit_stages_invoice.vit_stages_invoice'].search([]),
#         })

#     @http.route('/vit_stages_invoice/vit_stages_invoice/objects/<model("vit_stages_invoice.vit_stages_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_stages_invoice.object', {
#             'object': obj
#         })