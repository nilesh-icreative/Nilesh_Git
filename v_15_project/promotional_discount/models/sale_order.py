from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    discount_boolean = fields.Boolean(compute="_hello", store=True)

    @api.depends('partner_id')
    def _hello(self):
        boolean_values = self.env['ir.config_parameter'].get_param(
            'pro_discount')
        self.discount_boolean = boolean_values

    def discount_search(self):

        order_date = self.env.get('sale.order.line')
        print("======================\n\n", order_date)
