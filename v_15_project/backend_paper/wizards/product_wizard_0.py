from odoo import models, fields, api


class Order_Line(models.TransientModel):
    """ Contacts Wizard Form"""

    _name = 'order_line'
    _description = "order_line"

    sale_order_id = fields.Many2one(comodel_name="product")

    product_id = fields.Many2one(comodel_name="product.product")
    quantity = fields.Float()
    price = fields.Float()
