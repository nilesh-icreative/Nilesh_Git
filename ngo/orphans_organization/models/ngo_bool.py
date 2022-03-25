
from odoo import models, fields, api

class ngo(models.Model):

    _inherit = 'res.partner'

    ngo_check = fields.Boolean()

    total_member_orphan = fields.Integer(string="Total Members")
    currency_id = fields.Many2one("res.currency", string="Currency", default=20, readonly=True)
    available_fund = fields.Integer(string="Available Funds")
    foundation_years = fields.Selection(selection="foundation_y", string="Foundation Year")
    total_capacity = fields.Integer(string="Total Capacity")
    space = fields.Integer(compute="onchange_space")

    member_list_ids = fields.One2many('orphans.member', 'o_organization')

    @api.onchange("total_capacity", "total_member_orphan")
    def onchange_space(self):
        member = self.env['orphans.member']
        record = member.search([])
        val = record.read(['o_organization'])

        list_o = []
        for i in val:
            list_o.append(i['o_organization'][0])

        orga_list = list(set(list_o))

        for j in orga_list:
            count_o = member.search_count([('o_organization', '=', j)])
            self.search([('id', '=', j)]).write({'total_member_orphan': count_o})

        for rec in self:
            s = rec.total_capacity - rec.total_member_orphan
            rec.space = s

    def foundation_y(self):
        x = [(str(i), i) for i in range(1990, 2022)]
        return x

    def s_button(self):
        pass
