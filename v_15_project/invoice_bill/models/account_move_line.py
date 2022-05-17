from odoo import models, fields, api


class Account_Move_Line(models.Model):
    """ Inherit Object"""

    _inherit = 'account.move.line'

    vendor_id = fields.Many2one(comodel_name='res.partner', string="Vendor",
                                domain=[('customer_rank', '>', 0)])

    delivery_address_id = fields.Many2one(comodel_name='res.partner',
                                          string="Delivery",
                                          domain=[('type', '=', 'delivery')])

    vendor_price = fields.Float(string="Vendor Price")

    planned_gp = fields.Float(string="Planned Gp")

    description = fields.Html(string="Description",
                              compute="concatenation_description", store=True)

    @api.onchange('price_unit', 'vendor_price')
    def calculate_gp(self):
        """ Calculate Planned Gp"""
        if self.price_unit and self.vendor_price:
            self.planned_gp = ((self.price_unit - self.vendor_price)
                               / self.price_unit) * 100

    @api.depends('product_id', 'delivery_address_id')
    def concatenation_description(self):
        """ Delivery addd and Product Description"""
        for rec in self:
            if rec.product_id.description and rec.delivery_address_id:
                rec.description = ('{} {}' .format(
                    rec.product_id.description, rec.delivery_address_id.name))
            elif rec.product_id.description:
                rec.description = ('{}' .format(rec.product_id.description))
            elif rec.delivery_address_id:
                rec.description = ('{}' .format(rec.delivery_address_id.name))
            else:
                rec.description = False
