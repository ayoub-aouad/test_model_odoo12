# -*- coding: utf-8 -*-

from odoo import models, fields, api

class dietfacts(models.Model):
    _name = 'product.template'
    _inherit = ["product.template"]
    mx_calories = fields.Integer(string="Calories", required=False, )
    mx_protain = fields.Float(string="Protain",  required=False, )
    mx_text = fields.Text(string="Text", required=False, )


