
from odoo import models, fields, api
from datetime import date


class contacts_age(models.Model):
    """ Contacts View Inherit """

    _inherit = 'res.partner'

    dob = fields.Date(string="DOB")
    con_age = fields.Integer(string="Age", compute="calculate_age", store=True)

    @api.depends("dob")
    def calculate_age(self):
        """ Calculate Age """
        for rec in self:
            if rec.dob:
                today = date.today()
                rec.con_age = today.year - rec.dob.year - (
                    (today.month - today.day) < (rec.dob.month - rec.dob.day))
