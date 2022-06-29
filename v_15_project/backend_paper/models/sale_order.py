from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_capacity = fields.Integer(string="Total Capacity", readonly=True)
    commision = fields.Float(string="commission", default=2.5)

    @api.onchange('order_line', 'commision', 'partner_id')
    def _calculate_commission(self):
        """
        Calculate Product Commission
        """
        # product_obj = self.env['product.product'].search([('categ_id', '=', 8),
        #                                                   ('standard_price', '>', 20)],
        #                                                  limit=10, order='create_date')
        #print("==================\n\n", product_obj)
        # product_obj = self.env['product.product'].search([('sale_ok', '=', True),
        #                                                   ('detailed_type', '=', 'consu')])
        # print("==================\n\n", product_obj)
        for sale_rec in self.order_line:
            cal_commission = (sale_rec.price_subtotal * self.commision)/100
            sale_rec.p_commision = cal_commission

    def calculate_qty(self):
        """
        Calculate quantity in sale Order
        """
        if self.amount_total == 0.0:
            raise ValidationError("Please Select Product And Add Quantity")

        total_qty = []
        for rec in self.order_line:
            total_qty.append(rec.product_uom_qty)

        self.total_capacity = sum(total_qty)
    #
    # @api.constrains('order_line')
    # def _unique_product_check(self):
    #     for sale_rec in self:
    #         exist_product = []
    #         for line in sale_rec.order_line:
    #             if line.product_id.id in exist_product:
    #                 raise ValidationError('Product Select Must Be Unique')
    #             exist_product.append(line.product_id.id)
