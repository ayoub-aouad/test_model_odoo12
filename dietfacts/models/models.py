# -*- coding: utf-8 -*-

from odoo import models, fields, api

class dietfacts_product_template(models.Model):#this module is an inherit model that add and modify in a existing model
    _name = 'product.template'
    _inherit = ["product.template"]
    _description = "MX_inherit_MODEL1"
    mx_calories = fields.Integer(string="Mx_Calories", required=False, )
    mx_protain = fields.Float(string="Mx_Protain",  required=False, )
    mx_text = fields.Text(string="Mx_Text", required=False, )
    #mx_dietitem= fields.Boolean(string="Mx_dietitem",  )
class dietfacts_res_users_info(models.Model):
    _name = 'mx.res.users'

    _description = 'MX_res_Model'

    mx_name = fields.Char(string="Mx_Users", required=False, )
    mx_datetime = fields.Datetime(string="Mx_DateTime", required=True, )
    mx_users_id = fields.Many2one(comodel_name="res.users", string="Mx_Users_Id", required=False, )
    mx_comment = fields.Text(string="Mx_Comment", required=False, )
