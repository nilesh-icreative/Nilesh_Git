

from odoo import models , fields , api
from odoo.exceptions import ValidationError
from datetime import *


class orphans_request(models.TransientModel):

    _name = "orphans.request"
    _description = "orphans request"

    ngo = fields.Char(string="Ngo")
    name = fields.Char(required=True)
    dob = fields.Date(string="Date Of Birth", required=True)
    g_name = fields.Char(string="Guardian Name")
    age = fields.Char(string="Age", compute="cal_dob", store=True)
    # o_organization = fields.Char(string="Organization Name")

    s1 = fields.Char(string="Address")
    s2 = fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip = fields.Char()
    country = fields.Char()

    o_organization = fields.Many2one('orphans.organization', string="Organization Name")




    @api.depends("dob")
    def cal_dob(self):
        if self.dob is not False:
            for i in self:
                today = date.today()
                i.age = today.year - i.dob.year - ((today.month - today.day) < (i.dob.month - i.dob.day))


    def val_age(self):
        if int(self.age) > 18:
            raise ValidationError("Age Must Be Below 18 !")

    def s_button(self):
        pass