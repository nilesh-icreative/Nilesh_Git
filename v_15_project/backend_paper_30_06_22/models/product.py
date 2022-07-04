from odoo import fields, models, api


class Product(models.Model):
    _inherit = 'product.product'

    product_length = fields.Float(string="Length")
