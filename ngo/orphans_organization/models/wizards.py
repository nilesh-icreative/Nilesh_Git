

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
    state1 = fields.Many2one('res.country.state')
    zip = fields.Char()
    country = fields.Many2one('res.country')
    o_organization = fields.Many2one('res.partner', required=True, string="Organization Name", domain=[('ngo_check', '=', True)])

    status = fields.Selection([('req', 'Request Sent'), ('apr', 'Approved')], default="req")

    @api.model
    def default_get(self, field):
        record = self.env['res.partner']
        act_id = self.env.context.get("active_id")
        brow = record.browse(act_id)
        name_read = brow.read(['id'])
        # print("==========================",name_read)
        val = super(orphans_request, self).default_get(field)

        for r in name_read:
            val["o_organization"] = r["id"]

        return val

    @api.depends("dob")
    def cal_dob(self):
        if self.dob is not False:
            for i in self:
                today = date.today()
                i.age = today.year - i.dob.year - ((today.month - today.day) < (i.dob.month - i.dob.day))


    def val_age(self):
        if int(self.age) > 18:
            raise ValidationError("Age Must Be Below 18 !")

    @api.onchange("state1")
    def check_country(self):
        if self.state1:
            for rec in self:
                rec.country = rec.state1.country_id

    def create_rec(self):
        member = self.env['orphans.member']

        for rec in self:
            val = {
                'name': rec.name,
                'g_name': rec.g_name,
                'dob': rec.dob,
                'o_organization': rec.o_organization.id,
                'age': rec.age,
                's1': rec.s1,
                's2': rec.s2,
                'city': rec.city,
                'state': rec.state1.id,
                'zip': rec.zip,
                'country': rec.country.id,
                'designation': 'member',
            }
        member.create(val)
        self.status = "apr"
