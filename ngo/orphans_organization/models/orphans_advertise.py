
from odoo import models , fields , api

class orphans_advertise(models.Model):

    _name = 'orphans.advertise'
    _description = 'orphans_advertise'

    image = fields.Binary(related="dona_organization.image_1920")
    dona_organization = fields.Many2one('res.partner', string="Organization Home", required=True, domain=[('ngo_check', '=', True)])
    avl_seats = fields.Integer(string="Available Seats")
    exp_dates = fields.Date(string="Expired Dates", required=True,)
    facilities = fields.Html(string="Facilities")

    address = fields.Text(compute="read_address")

    @api.onchange("dona_organization")
    def read_address(self):
        if self.dona_organization:
            for rec in self:
                s1 = rec.dona_organization.street
                s2 = rec.dona_organization.street2
                city = rec.dona_organization.city
                state = rec.dona_organization.state_id.name
                pin = rec.dona_organization.zip
                country = rec.dona_organization.country_id.name
                self.address = s1 + ", " + s2 + "\n" + city + " " + state + " " + pin +"\n"+ country

    @api.model
    def default_get(self, field):
        record = self.env['orphans.member']
        active_id = self.env.context.get("active_id")
        member_r = record.browse(active_id)
        member = member_r.read(['o_organization'])
        print("====================",member)
        donation_class = super(orphans_advertise, self).default_get(field)

        for rec in member:
            donation_class['dona_organization'] = rec['o_organization']

        return donation_class

    @api.onchange("state")
    def check_country(self):
        if self.state:
            for rec in self:
                rec.country = rec.state.country_id

    def s_button(self):
        pass
