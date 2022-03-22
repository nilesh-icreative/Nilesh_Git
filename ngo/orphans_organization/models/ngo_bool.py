
from odoo import models, fields, api

class ngo(models.Model):

    _inherit = 'res.partner'

    ngo_check = fields.Boolean()

    total_member_orphan = fields.Integer(string="Total Members")
    currency_id = fields.Many2one("res.currency", string="Currency", default=20, readonly=True)
    available_fund = fields.Integer(string="Available Funds")
    foundation_years = fields.Selection(selection="foundation_y", string="Foundation Year")
    total_capacity = fields.Integer(string="Total Capacity")
    space = fields.Integer()

    @api.onchange("total_capacity", "total_member_orphan")
    def onchange_space(self):
        s = self.total_capacity - self.total_member_orphan
        self.space = s

    def foundation_y(self):
        x = [(str(i), i) for i in range(1990, 2022)]
        return x

    def s_button(self):
        pass
