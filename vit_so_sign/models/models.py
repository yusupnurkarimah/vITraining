# -*- coding: utf-8 -*-

from odoo import api, fields, models
import time
import datetime
import logging
_logger = logging.getLogger(__name__)


class sale_order(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    validated_by = fields.Many2one(comodel_name='res.users', string='Validated By', required=False, )
