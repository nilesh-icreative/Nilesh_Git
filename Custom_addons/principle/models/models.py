# -*- coding: utf-8 -*-

from odoo import models, fields, api


class principle(models.Model):
    _name = 'principle.principle'
    _description = 'principle.principle'

    name = fields.Char(string="Principle_Name")
    age = fields.Integer(string="principle_Age")
    binary = fields.Binary(string='Upload Image')
    gender = fields.Selection(selection=[('m','Male'),('f','Female'),('o','Othere')])
    p_dob = fields.Date(string="principle_dob")
    principle_Address = fields.Text()
    area = fields.Char()
    value = fields.Integer(string="pincode")

    description = fields.Text(string="Collage_Address")



#    @api.depends('value')
#    def _value_pc(self):
#        for record in self:
#            record.value2 = float(record.value) / 100
#