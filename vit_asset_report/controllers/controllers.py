# -*- coding: utf-8 -*-
from odoo import http

# class VitAssetReport(http.Controller):
#     @http.route('/vit_asset_report/vit_asset_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_asset_report/vit_asset_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_asset_report.listing', {
#             'root': '/vit_asset_report/vit_asset_report',
#             'objects': http.request.env['vit_asset_report.vit_asset_report'].search([]),
#         })

#     @http.route('/vit_asset_report/vit_asset_report/objects/<model("vit_asset_report.vit_asset_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_asset_report.object', {
#             'object': obj
#         })