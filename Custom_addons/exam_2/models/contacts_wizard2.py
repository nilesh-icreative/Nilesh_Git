from odoo import models, fields


class contacts_action(models.TransientModel):
    """ Contacts Wizard Form"""

    _name = 'sale_order_wizard'
    _description = "sale_order_wizard"

    sale_order_line = fields.One2many(comodel_name='contacts_action',
                                      inverse_name='sale_order_id')

    def order_create(self):
        """ Sale Order Line"""

        active_id = self.env['res.partner'].browse(self._context['act_id'])
        print("==================", active_id)
        sale_record = self.env['sale.order']

        for rec in active_id:
            print("========id===========", rec.id)
            print("===================", type(rec))

            record = sale_record.create({
                'partner_id': rec.id,
            })

            for product in self.sale_order_line:
                record.write(
                    {'order_line': [(0, 0,
                                     {
                                         'product_id': product.product_id.id,
                                         'product_uom_qty': product.quantity,
                                         'price_unit': product.price,
                                     })]})
