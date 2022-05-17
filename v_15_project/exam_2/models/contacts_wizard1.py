from odoo import models, fields


class contacts_action(models.TransientModel):
    """ Contacts Wizard Form"""

    _name = 'contacts_action'
    _description = "contacts_action"

    sale_order_id = fields.Many2one(comodel_name="sale_order_wizard")

    product_id = fields.Many2one(comodel_name="product.product")
    quantity = fields.Float()
    price = fields.Float()
