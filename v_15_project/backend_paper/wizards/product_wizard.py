from odoo import models, fields, api

class Product(models.TransientModel):
    """ Product Wizard"""

    _name = 'product'
    _description = 'product'

    sale_order_line = fields.One2many(comodel_name='order_line',
                                      inverse_name='sale_order_id')

    @api.model
    def default_get(self, field):
        sale_r = self.env['batch.sale.workflow']
        act_id = self.env.context.get('active_id')
        record = sale_r.browse(act_id)

        order_line = []
        for product_rec in record.sale_order_ids.order_line:
            order_line.append((0, 0, {
                'product_id': product_rec.product_id.id,
                'quantity': product_rec.product_uom_qty,
                'price': product_rec.price_subtotal,
            }))

        so = super(Product, self).default_get(field)
        so.update({
            'sale_order_line': order_line,
        })
        return so
