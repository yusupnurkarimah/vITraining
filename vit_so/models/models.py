# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vit_so(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    account_analytic_id = fields.Many2one(comodel_name="account.analytic.account", string="Unit")
    analytic_tag_ids = fields.Many2many(comodel_name="account.analytic.tag", string="Location", domain=[("analytic_dimension_id","=","LOCATION")])
    business_id = fields.Many2many(comodel_name="account.analytic.tag", string="Business", domain=[("analytic_dimension_id","=","BUSINESS")])