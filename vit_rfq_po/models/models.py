# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vit_rfq_po(models.Model):
    _name = 'purchase.order.line'
    _inherit = 'purchase.order.line'

    account_analytic_id = fields.Many2one(comodel_name="account.analytic.account", string="Unit")
    analytic_tag_ids = fields.Many2many(comodel_name="account.analytic.tag", string="Location", domain=[("analytic_dimension_id","=","LOCATION")])
    business_id = fields.Many2many(comodel_name="account.analytic.tag", string="Business", domain=[("analytic_dimension_id","=","BUSINESS")])