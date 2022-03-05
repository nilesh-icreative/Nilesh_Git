# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime



class contacts(models.Model):

    _inherit = 'res.partner'
    dob = fields.Date(string='Date_of_Birth',required=False)
    customer_r = fields.Char(string="Customer_reference")
    partner_id = fields.Many2one("res.partner", string="Partner")
    category_id = fields.Many2many("res.partner.category", string="category")




