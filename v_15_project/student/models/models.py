# -*- coding: utf-8 -*-

from odoo import models, fields, api


class student(models.Model):

    _name = 'student'
    _description = 'student'

    r_no = fields.Integer(string="Roll No")
    f_name = fields.Char(string="First Name")
    l_name = fields.Char(string="Last Name")
    email = fields.Char(string="Email")







