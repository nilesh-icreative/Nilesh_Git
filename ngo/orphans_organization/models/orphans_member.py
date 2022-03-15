
from odoo import models , fields , api

class orphans_member(models.Model):

    _name = 'orphans.member'
    _description = 'orphans_member'

    ngo = fields.Char(string="Ngo")
    name = fields.Char(required=True, default="")
    dob = fields.Date(string="Date Of Birth", required=True)
    g_name = fields.Char(string="Guardian Name")
    age = fields.Char(string="Age")
    o_organization = fields.Many2one('orphans.organization', string="Organization Name")

    s1 = fields.Char(string="Address")
    s2 = fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip = fields.Char()
    country = fields.Char()

    def s_button(self):
        pass




