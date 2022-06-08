from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    qty_on_order = fields.Float(string="Qty on Order", default="1.0")
