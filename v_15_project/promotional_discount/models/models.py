from odoo import models, fields, api


class Promotional_Discount(models.Model):
    _name = 'promotional.discount'
    _description = 'promotional.discount'

    discount_type = fields.Selection([('per', 'Percentage'), ('fa', 'Fixed Amount')])
    name = fields.Char()
    discount = fields.Char(compute="_compute_percent", store=True)
    min_order_amount = fields.Integer(string="Amount", default='100')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    # per_symbol = fields.Char(compute="_compute_percent", store=True)

    @api.depends('discount_type')
    def _compute_percent(self):
        for rec in self:
            if rec.discount_type == 'per':
                self.discount = str()+'%'
            elif rec.discount_type == 'fa':
                self.discount = '$'
