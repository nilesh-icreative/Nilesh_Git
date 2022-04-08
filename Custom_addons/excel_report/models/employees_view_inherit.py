
from odoo import models, fields


class Employees(models.TransientModel):
    """ Employee View wizards"""

    _name = 'employees'
    _description = 'employee'

    name = fields.Char()
