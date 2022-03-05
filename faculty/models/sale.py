# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime



class sale(models.Model):

    _inherit = 'sale.order'
    customer_reference = fields.Char(string="Customer_reference", related='partner_id.customer_r', )
    d_o_b = fields.Date(string="Date_of_birth", related='partner_id.dob', )

    cust_image = fields.Char(string="Customer Image")






