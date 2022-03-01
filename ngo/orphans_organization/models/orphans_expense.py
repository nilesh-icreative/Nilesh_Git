
from odoo import models , fields , api

class orphans_expense(models.Model):

    _name = 'orphans.organization.expense'
    _description = 'orphans_expense'

    name = fields.Char(required=True , string="Expense User")
    e_type = fields.Selection([('1', 'Fuel'), ('2', 'Food'), ('3', 'Electricity')], string="Expense Type")
    e_amount = fields.Integer(string="Expense Amount")
    # o_organization = fields.Char(string="Organization Home")
    o_organization = fields.Many2one('orphans.organization', string="Organization Home")
    notes = fields.Char(string="Notes")

    def s_button(self):
        pass




