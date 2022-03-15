
from odoo import models, fields, api

class ngo(models.Model):

    _inherit = 'res.partner'

    ngo_check = fields.Boolean()

    total_member_orphan = fields.Integer(string="Total Orphan Members")
    currency_id = fields.Many2one("res.currency", string="Currency", default=20, readonly=True)
    available_fund = fields.Integer(string="Available Funds")
    foundation_years = fields.Selection(selection="foundation_y", string="Foundation Year")
    total_capacity = fields.Integer(string="Total Capacity")

    def foundation_y(self):
        x = [(str(i), i) for i in range(1990, 2022)]
        return x