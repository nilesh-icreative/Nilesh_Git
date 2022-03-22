from odoo import models , fields , api

class expense_type(models.Model):

    _name = 'expense_type'
    _description = 'expense_type'

    name = fields.Char(string="Expense Type")
