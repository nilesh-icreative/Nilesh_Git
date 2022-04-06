from odoo import models, fields


class contacts_action(models.TransientModel):
    """ Contacts Wizard Form"""

    _name = 'contacts_action'
    _description = "contacts_action"

    product_ids = fields.Many2many(comodel_name="product.product",
                                   string="Product")
    quantity = fields.Float()
    price = fields.Float()

    def order_create(self):
        """ Sale Order Line Create """

        active_id = self.env['res.partner'].browse([self._context['act_id']])
        print("==================", active_id)
        sale_record = self.env['sale.order']

        record = sale_record.create({
            'partner_id': active_id.id,
        })

        for product in self.product_ids:
            record.write({'order_line': [(0, 0,
                                          {
                                              'product_id': product.id,
                                              'product_uom_qty': self.quantity,
                                              'price_unit': self.price,
                                          })]})
