# -*- coding: utf-8 -*-

from odoo import models, fields, api




class order_line(models.Model):

    _inherit = 'sale.order.line'

    cust_image = fields.Char(string="Customer Image")






