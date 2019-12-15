# -*- coding: utf-8 -*-
from odoo import http

# class VitRfqPo(http.Controller):
#     @http.route('/vit_rfq_po/vit_rfq_po/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_rfq_po/vit_rfq_po/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_rfq_po.listing', {
#             'root': '/vit_rfq_po/vit_rfq_po',
#             'objects': http.request.env['vit_rfq_po.vit_rfq_po'].search([]),
#         })

#     @http.route('/vit_rfq_po/vit_rfq_po/objects/<model("vit_rfq_po.vit_rfq_po"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_rfq_po.object', {
#             'object': obj
#         })