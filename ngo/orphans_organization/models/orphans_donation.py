
from odoo import models , fields , api

class orphans_donation(models.Model):

    _name = 'orphans.organization.donation'
    _description = 'orphans_donation'

    name = fields.Char(required=True , string="Doner Name")
    # o_organization = fields.Char(string="Orphans Home")
    o_organization = fields.Many2one('res.partner', required=True, string="Organization Home", domain=[('ngo_check', '=', True)])
    currency_id = fields.Many2one("res.currency", string="Currency", default=20, readonly=True)
    amount = fields.Integer(string="Amount", required=True)
    phone = fields.Char(string="Phone No")
    email = fields.Char(string="Email")

    s1 = fields.Char(string="Address")
    s2 = fields.Char()
    city = fields.Char()
    state = fields.Many2one('res.country.state')
    zip = fields.Char()
    country = fields.Many2one('res.country')


    @api.onchange("state")
    def check_country(self):
        if self.state:
            for rec in self:
                rec.country = rec.state.country_id

    @api.model
    def default_get(self, field):
        record = self.env['res.partner']
        act_id = self.env.context.get("active_id")
        brow = record.browse(act_id)
        name_read = brow.read(['id'])
        # print("==========================",name_read)
        val = super(orphans_donation, self).default_get(field)

        for r in name_read:
            val["o_organization"] = r["id"]

        return val

    @api.onchange("amount")
    def onchange_amount(self):
        d_amount = self.amount
        donation_fund = self.o_organization.available_fund
        amount = donation_fund + d_amount
        self.o_organization.available_fund = amount
        print("=========================", amount)

    def s_button(self):
        pass






