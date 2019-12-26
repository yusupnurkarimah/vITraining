# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vit_efaktur_prefix(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'

    prefix_berikat_id = fields.Many2one(comodel_name="prefix.nsfp",string="Prefix NSFP")

class prefix_nsfp(models.Model):
    _name = 'prefix.nsfp'
    _rec_name = 'prefix_berikat'

    prefix_berikat = fields.Char(string="Prefix NSFP")