
from odoo.exceptions import ValidationError
from odoo import models, fields, api

class smart(models.Model):

     _name = 'related_field.smart'
     _description = 'related'

     name = fields.Many2one(comodel_name='smart_button')
     r_no = fields.Char(string="Roll No", related='name.dep')





