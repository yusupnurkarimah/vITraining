# -*- coding: utf-8 -*-
import logging
from odoo import http
from odoo.http import request

logger = logging.getLogger(__name__)

class VitHasGroup(http.Controller):
    @http.route('/vit/index', type='http', auth='public', website=True)
    def index(self, **kw):
        user_obj = request.env['res.users']
        user = user_obj.browse(request.uid)
        is_admin = user.has_group('base.group_system')

        return request.render("vit_has_group.index",{
            'is_admin': is_admin 
        })

#     @http.route('/vit_has_group/vit_has_group/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_has_group.listing', {
#             'root': '/vit_has_group/vit_has_group',
#             'objects': http.request.env['vit_has_group.vit_has_group'].search([]),
#         })

#     @http.route('/vit_has_group/vit_has_group/objects/<model("vit_has_group.vit_has_group"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_has_group.object', {
#             'object': obj
#         })