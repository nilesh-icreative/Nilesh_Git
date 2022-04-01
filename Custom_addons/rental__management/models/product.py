
from odoo import models, fields, api

class product(models.Model):
    """ Product View """

    _inherit = 'product.template'

    is_rental = fields.Boolean()

    rental_type = fields.Many2one('rental.type', required=True)



