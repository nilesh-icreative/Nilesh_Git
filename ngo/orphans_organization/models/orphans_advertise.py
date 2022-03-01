
from odoo import models , fields , api

class orphans_advertise(models.Model):

    _name = 'orphans.advertise'
    _description = 'orphans_advertise'

    o_organization = fields.Char(string="Organization Home")
    avl_seats = fields.Integer(string="Available Seats")
    exp_dates = fields.Date(string="Expired Dates")
    facilities = fields.Html(string="Facilities")

    s1 = fields.Char(string="Address")
    s2 = fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip = fields.Char()
    country = fields.Char()


    def s_button(self):
        pass




