
from odoo import models, fields, api


class organization(models.Model):
    _name = 'orphanage_management.organization'
    _description = 'organization'


    name = fields.Char(string="Emp_name")