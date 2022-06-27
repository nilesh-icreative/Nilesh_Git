from odoo import fields, models, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    discount_boolean = fields.Boolean(compute="_discount_bool_value")

    # @api.onchange('order_line')
    # def discount_button_visible(self):
    #     """
    #     Button Visible Apply Promotional Discount
    #     """
    #     discount_product = self.env['product.product'].search([('pro_discount_boolean', '=', True)])
    #     for sale_rec in self.order_line.product_id:
    #         if sale_rec.id == discount_product.id:
    #             self.discount_boolean = False
    #         elif sale_rec.id != discount_product.id:
    #             self.discount_boolean = True
    #     # print("======onchange========\n\n", self.discount_boolean)

    @api.depends('order_line')
    def _discount_bool_value(self):
        self.discount_boolean = self.env['ir.config_parameter'].get_param(
            'pro_discount')
        discount_product = self.env['product.product'].search([('pro_discount_boolean', '=', True)])
        for sale_rec in self.order_line.product_id:
            if sale_rec.id == discount_product.id:
                self.discount_boolean = False
            elif sale_rec.id != discount_product.id:
                self.discount_boolean = True

    def discount_search(self):
        """
        Discount Calculation
        """

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
                self.discount_boolean = False
