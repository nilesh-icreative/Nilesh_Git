from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    length = fields.Float(string="Length", related='product_id.product_length')
    total_length = fields.Float(string="Total Length")
