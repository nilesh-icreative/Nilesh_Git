# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime



class faculty(models.Model):

    _name = 'faculty.faculty'
    _description = 'faculty.faculty'

    faculty_name = fields.Char()
    faculty_age = fields.Integer()
    name = fields.Char(string="qualification",required=True)
    dob = fields.Date(string="DOB",required=True,help="Date of Birth")
    today = fields.Date(default=datetime.now())
    subject = fields.Char()
    add = fields.Char(string="Address",required=True,size=20)
    salary = fields.Float(digits=(4,2))
    bool = fields.Boolean(default=True)
    bool1=fields.Boolean()
    file = fields.Binary()
    select1 = fields.Selection([('a', 'A')])
    select = fields.Selection(string="Gander",selection=[('m','Male'),('f','Female'),('o','Other')])
    refer = fields.Reference([('faculty.faculty', 'select')])
    refer_s = fields.Reference(selection=[('faculty.faculty', 'String_string')])
    refer_f = fields.Selection(selection="mylist",string='bca')
    html_wid = fields.Html()
    value = fields.Integer()
    user = fields.Many2one('res.users')
    user_comodel = fields.Many2one(comodel_name='res.users')
#    user_delegate = fields.Many2one(comodel_name='res.faculty', delegate=True)
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()



class TestModel(models.Model):
    _inherit = 'faculty.faculty'
    select = fields.Selection(selection_add=[('b', 'B'), ('c', 'C')])

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    def mylist(self):
        return [(1,'gu'),(2,'ssc'),(3,'hsc')]