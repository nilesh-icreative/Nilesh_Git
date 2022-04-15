from odoo import models, fields


class Account_Move_Line(models.Model):
    """ Inherit Object"""

    _inherit = 'account.move.line'

    vendor_id = fields.Many2one(comodel_name='res.partner', string="Vendor",
                                domain=[('customer_rank', '>', 0)])

    delivery_address_id = fields.Many2one(comodel_name='res.partner', string="Delivery",
                                          domain=[('type', '=', 'delivery')])
