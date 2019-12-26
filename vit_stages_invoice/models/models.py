# -*- coding: utf-8 -*-

from odoo import models, fields, api

class stages_invoice(models.Model):
    _name = 'vit_stages_invoice.stage'

    name = fields.Char(string='Name', required=True,)
    usage = fields.Selection(
        string='Usage',
        selection=[
            ('in invoice', 'in invoice'), 
            ('out invoice', 'out invoice')],)

class stages(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'
    
    stages = fields.Many2one(string='Stages', comodel_name='vit_stages_invoice.stage', domain=[('type', '=', "out invoice")])
    