from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Promotional_Discount(models.Model):
    _name = 'promotional.discount'
    _description = 'promotional.discount'

    discount_type = fields.Selection([('per', 'Percentage'), ('fa', 'Fixed Amount')],
                                     required=True)
    name = fields.Char(required=True, default="")
    discount = fields.Integer(string="Discount")
    min_order_amount = fields.Integer(string="Amount", default='100')
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    currency_id = fields.Many2one("res.currency", string="Currency", readonly=True)

    @api.onchange('discount_type')
    def _compute_symbol(self):
        for rec in self:
            if rec.discount_type == 'fa':
                self.currency_id = self.env.company.currency_id.id
            elif rec.discount_type == 'per':
                self.currency_id = False

    @api.constrains('start_date', 'end_date')
    def check_date(self):
        if self.start_date >= self.end_date:
            raise ValidationError("Please Select Valid Date")
