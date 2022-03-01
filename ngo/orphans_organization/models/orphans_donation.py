
from odoo import models , fields , api

class orphans_donation(models.Model):

    _name = 'orphans.organization.donation'
    _description = 'orphans_donation'

    name = fields.Char(required=True , string="Doner Name")
    # o_organization = fields.Char(string="Orphans Home")
    o_organization = fields.Many2one('orphans.organization', string="Organization Home")
    amount = fields.Integer(string="Amount", required=True)
    phone = fields.Integer(string="Phone No")
    email = fields.Char(string="Email")

    s1 = fields.Char(string="Address")
    s2 = fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip = fields.Char()
    country = fields.Char()

    def s_button(self):
        pass



