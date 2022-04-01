

from odoo import models, fields, api


class rental_type(models.Model):
    """  Rental Type Object """

    _name = 'rental.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'rental_type'

    name = fields.Char(string="Name", required=True, tracking=True)
    code = fields.Integer(string="Code", tracking=True)
    description = fields.Text(string="Description", tracking=True)
