# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vit_invoice_bill(models.Model):
    _name = 'account.invoice.line'
    _inherit = 'account.invoice.line'

    account_analytic_id = fields.Many2one(comodel_name="account.analytic.account", string="Unit")
    analytic_tag_ids = fields.Many2many(comodel_name="account.analytic.tag", string="Location", domain=[("analytic_dimension_id.name","=","LOCATION")])
    business_id = fields.Many2many(comodel_name="account.analytic.tag", string="Business", domain=[("analytic_dimension_id.name","=","BUSINESS")])

class vit_tax(models.Model):
    _name = 'account.invoice.tax'
    _inherit = 'account.invoice.tax'

    account_analytic_id = fields.Many2one(comodel_name="account.analytic.account", string="Unit")
    analytic_tag_ids = fields.Many2many(comodel_name="account.analytic.tag", string="Location", domain=[("analytic_dimension_id.name","=","LOCATION")])
    business_id = fields.Many2many(comodel_name="account.analytic.tag", string="Business", domain=[("analytic_dimension_id.name","=","BUSINESS")])

class vit_journal(models.Model):
    _name = 'account.move.line'
    _inherit = 'account.move.line'

    analytic_account_id = fields.Many2one(comodel_name="account.analytic.account", string="Unit")
    analytic_tag_ids = fields.Many2many(comodel_name="account.analytic.tag", string="Location", domain=[("analytic_dimension_id.name","=","LOCATION")])
    business_id = fields.Many2many(comodel_name="account.analytic.tag", string="Business", domain=[("analytic_dimension_id.name","=","BUSINESS")])