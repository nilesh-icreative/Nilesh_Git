from odoo import fields, models, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    discount_boolean = fields.Boolean(compute="_hello", store=True)

    @api.depends('partner_id')
    def _hello(self):
        boolean_values = self.env['ir.config_parameter'].get_param(
            'pro_discount')

        self.discount_boolean = boolean_values

    def discount_search(self):

        discount_product = self.env['product.product'].search([('pro_discount_boolean', '=', True)])

        if len(discount_product) == 0:
            raise ValidationError("Add Discount Product")

        for sale_rec in self:
            pro_discount = self.env['promotional.discount'].search(
                [('start_date', '<=', sale_rec.date_order),
                 ('end_date', '>=', sale_rec.date_order),
                 ('min_order_amount', '<=', sale_rec.amount_total)]
            )

            if len(pro_discount) == 0:
                raise ValidationError("Not Available Any Discount ")

            discount_amount = []
            for pro_disc_rec in pro_discount:
                if pro_disc_rec.discount_type == 'per':
                    amount = (sale_rec.amount_total * pro_disc_rec.discount)/100
                    discount_amount.append(amount)
                elif pro_disc_rec.discount_type == 'fa':
                    discount_amount.append(pro_disc_rec.discount)

            sale_order_line_obj = self.env['sale.order.line']

            if discount_amount:
                sale_order_line_obj.create({
                    'product_id': discount_product.id,
                    'order_id': self.id,
                    'price_unit': -float(min(discount_amount)),
                    })
