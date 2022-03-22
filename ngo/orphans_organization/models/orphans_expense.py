
from odoo import models , fields , api


class orphans_expense(models.Model):

    _name = 'orphans.organization.expense'
    _description = 'orphans_expense'

    name_user = fields.Char(required=True, string="Expense User")
    #e_type = fields.Selection([('1', 'Fuel'), ('2', 'Food'), ('3', 'Electricity')], string="Expense Type")
    name = fields.Many2one('expense_type', string="Expense Type")
    currency_id = fields.Many2one("res.currency", string="Currency", default=20, readonly=True)
    e_amount = fields.Integer(string="Expense Amount", required=True)
    od_organization = fields.Many2one('res.partner', string="Organization Home", required=True)
    notes = fields.Text(string="Notes")

    @api.model
    def default_get(self, field):
        record = self.env["orphans.member"]
        active_id = self.env.context.get('active_id')
        member_rec = record.browse(active_id)
        member = member_rec.read(['name','o_organization'])
        expense_class = super(orphans_expense, self).default_get(field)

        for data in member:
            expense_class['name_user'] = data['name']
            expense_class['od_organization'] = data['o_organization'][0]

        return expense_class

    @api.onchange("e_amount")
    def onchange_amount(self):
        exp_amount = self.e_amount
        orga_fund = self.od_organization.available_fund
        amount = orga_fund - exp_amount
        self.od_organization.available_fund = amount
        print("=========================", amount)





