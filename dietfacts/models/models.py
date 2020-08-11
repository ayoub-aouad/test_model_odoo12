# -*- coding: utf-8 -*-

from odoo import models, fields, api

class dietfacts(models.Model):
    _name = 'product.template'
    _inherit = ["product.template"]
    calories = fields.integer("Calories")


