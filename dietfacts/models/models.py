# -*- coding: utf-8 -*-

from odoo import models, fields, api

class dietfacts_product_template(models.AbstractModel):#this module is an inherit model that add and modify in a existing model
    _name = 'product.mx'
    
    _inherit = ["product.template"]
    _description = "MX_inherit_MODEL1"
    mx_calories = fields.Integer(string="Mx_Calories", required=True, )
    mx_protain = fields.Float(string="Mx_Protain",  required=True, )
    mx_text = fields.Text(string="Mx_Text",required=True,)
    mx_dietfact = fields.Boolean(string="Mx Dietfact", )

class Mx_inherited_Model(models.AbstractModel):
    _name = 'sale.mx'
    _inherit = ['sale.order']
    mx_text = fields.Text(string="Text",required=False, )

class dietfacts_res_users_info(models.Model):
    _name = 'users.mx'

    _description = 'MX_res_Model'
    mx_name = fields.Char(string="Mx_Users", required=False, )
    mx_datetime = fields.Datetime(string="Mx_DateTime", required=True, )
    mx_users_ids = fields.Many2one(comodel_name="res.users", string="MxUsers_Ids", required=False, )
    mx_comment = fields.Text(string="Mx_Comment", required=False, )
    mx_items_ids = fields.One2many(comodel_name="users.mxitem", inverse_name="mx_users_id", string="MX_items_Ids", required=False, )

class dietfacts_res_users_items(models.Model):
    _name = "users.mxitem"

    mx_users_id = fields.Many2one(comodel_name="users.mx", string="Mx_Users_Id", required=False, )
    mx_item_id = fields.Many2one(comodel_name="product.template", string="Mx_item_id", required=False, )
    mx_serving = fields.Float(string="Mx_Servings", required=False)
    mx_notes = fields.Text(string="Mx_Notes", required=False, )
    mx_calorie = fields.Text(string="Mx_Calories", required=False)