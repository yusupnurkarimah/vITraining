# -*- coding: utf-8 -*-
from odoo import http

# class VitProfitBalance(http.Controller):
#     @http.route('/vit_profit_balance/vit_profit_balance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_profit_balance/vit_profit_balance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_profit_balance.listing', {
#             'root': '/vit_profit_balance/vit_profit_balance',
#             'objects': http.request.env['vit_profit_balance.vit_profit_balance'].search([]),
#         })

#     @http.route('/vit_profit_balance/vit_profit_balance/objects/<model("vit_profit_balance.vit_profit_balance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_profit_balance.object', {
#             'object': obj
#         })