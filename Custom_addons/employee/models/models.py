

from odoo import models, fields, api


class employee(models.Model):
    _name = 'employee.employee'
    _description = 'employee.employee'

    name = fields.Char(string="Emp_name")
    age = fields.Integer(string="Emp_age")
    address = fields.Text(string="Emp_address")

    gender = fields.Selection([('m','Male'),('f','Female'),('o','Other')],string="Gender")
    image = fields.Binary(string="Upload_CV")
    dob = fields.Date(string="Emp_dob")

   # customer_reference = fields.Char(string="Customer_reference", related='partner_id.customer_r', )

