
from odoo import models , fields , api
from odoo.exceptions import ValidationError
import re

class orphans_donation(models.Model):

    _name = 'orphans.organization.donation'
    _description = 'orphans_donation'

    name = fields.Char(required=True, string="Donor Name")
    o_organization = fields.Many2one('res.partner', required=True, string="Organization Home", domain=[('ngo_check', '=', True)])
    currency_id = fields.Many2one("res.currency", string="Currency", default=20, readonly=True)
    amount = fields.Integer(string="Amount", required=True)
    phone = fields.Char(string="Phone No", required=True, default="")
    email = fields.Char(string="Email", required=True, default="")

    s1 = fields.Char(string="Address")
    s2 = fields.Char()
    city = fields.Char()
    state = fields.Many2one('res.country.state')
    zip = fields.Char()
    country = fields.Many2one('res.country')

    @api.constrains('phone')
    def phone_check(self):
        for rec in self:
            if rec.phone and len(rec.phone) != 10:
                raise ValidationError("Must Be 10 Digits!")
            elif(rec.phone and not str(rec.phone).isdigit()):
                raise ValidationError("Only Enter Number!")

    @api.constrains('email')
    def email_check(self):
        if self.email:
            match = re.match('^[_a-z]+[0-9-]*(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',self.email)
            if match == None:
                raise ValidationError("Not a Valid Email")

    @api.constrains('amount')
    def amount_check(self):
        if self.amount <= 0:
            raise ValidationError("Please Enter Amount!")

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

    @api.model_create_multi
    def create(self, val):
        super_donation = super(orphans_donation, self).create(val)

        for rec in val:
            donation_amount = rec["amount"]
            #print("=========dd=====\n",donation_amount)

            orga_record = self.env['res.partner']
            record = orga_record.browse(rec['o_organization'])
            record_set = record.read(['available_fund'])

            for i in record_set:
                fund = i['available_fund']
                amount = fund + donation_amount
                record.write({'available_fund': amount})
                #print("=========ffff============",amount)

        return super_donation

    def s_button(self):
        pass


