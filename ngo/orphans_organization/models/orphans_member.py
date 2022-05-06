from odoo import models, fields, api
from datetime import *


class orphans_member(models.Model):

    _name = 'orphans.member'
    _description = 'orphans_member'

    ngo = fields.Char(string="Ngo")
    name = fields.Char(required=True)
    dob = fields.Date(string="Date Of Birth", required=True)
    g_name = fields.Char(string="Guardian Name")
    age = fields.Char(string="Age", compute="cal_dob", store=True)
    o_organization = fields.Many2one(
        'res.partner', required=True, string="Organization Home",
        domain=[('ngo_check', '=', True)]
    )

    s1 = fields.Char(string="Address")
    s2 = fields.Char()
    city = fields.Char()
    state = fields.Many2one('res.country.state')
    zip = fields.Char()
    country = fields.Many2one('res.country')
    designation = fields.Selection(
        [('manager', 'Manager'), ('member', 'Member')]
    )

    @api.depends("dob")
    def cal_dob(self):
        if self.dob:
            for i in self:
                today = date.today()
                i.age = today.year - i.dob.year - (
                    (today.month - today.day) < (i.dob.month - i.dob.day)
                )

    @api.onchange("state")
    def check_country(self):
        if self.state:
            for rec in self:
                rec.country = rec.state.country_id

    def requests(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'orphans.request',
            'name': 'Orphans Request window',
            'view_mode': 'tree',
            'domain': [('o_organization', '=', self.o_organization.id)],
        }
