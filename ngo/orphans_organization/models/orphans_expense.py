
from odoo import models , fields , api
from odoo.exceptions import ValidationError

class orphans_expense(models.Model):

    _name = 'orphans.organization.expense'
    _description = 'orphans_expense'

    name_user = fields.Char(required=True, string="Expense User")
    name = fields.Many2one('expense_type', string="Expense Type", required=True)
    currency_id = fields.Many2one("res.currency", string="Currency", default=20, readonly=True)
    e_amount = fields.Integer(string="Expense Amount", required=True)
    od_organization = fields.Many2one('res.partner', string="Organization Home", required=True)
    notes = fields.Text(string="Notes")

    @api.constrains('e_amount')
    def amount_check(self):
        if self.e_amount <= 0:
            raise ValidationError("Please Enter Amount!")

    @api.model
    def default_get(self, field):
        record = self.env["orphans.member"]
        active_id = self.env.context.get('active_id')
        member_rec = record.browse(active_id)
        member = member_rec.read(['name', 'o_organization'])
        expense_class = super(orphans_expense, self).default_get(field)

        for data in member:
            expense_class['name_user'] = data['name']
            expense_class['od_organization'] = data['o_organization'][0]

        return expense_class

    @api.model_create_multi
    def create(self, val):
        super_donation = super(orphans_expense, self).create(val)

        for rec in val:
            expense_amount = rec["e_amount"]
            # print("=========dd=====\n",donation_amount)

            orga_record = self.env['res.partner']
            record = orga_record.browse(rec['od_organization'])
            record_set = record.read(['available_fund'])

            for i in record_set:
                fund = i['available_fund']
                amount = fund - expense_amount
                record.write({'available_fund': amount})
                # print("=========ffff============",amount)

        return super_donation





