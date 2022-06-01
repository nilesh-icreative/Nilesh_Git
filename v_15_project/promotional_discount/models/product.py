from odoo import fields, models, api


class Product(models.Model):
    _inherit = 'product.product'

    pro_discount_boolean = fields.Boolean()
