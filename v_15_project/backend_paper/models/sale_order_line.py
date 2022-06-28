from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    max_qty = fields.Float(string="Max Qty", readonly=True, related='product_id.qty_on_order')
    p_commision = fields.Float(string="P Commission")

    # @api.constrains('product_uom_qty', 'max_qty')
    # def check_qty(self):
    #     for rec in self:
    #         if rec.product_uom_qty >= rec.max_qty:
    #             raise ValidationError("Quantity Not More Than Max Qty !")
