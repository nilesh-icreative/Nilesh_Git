from odoo import models, fields, api

class Product(models.TransientModel):
    """ Product Wizard"""

    _name = 'product'
    _description = 'product'

    sale_order_line = fields.One2many(comodel_name='order_line',
                                      inverse_name='sale_order_id')

    @api.model
    def default_get(self, field):
        """
        Wizard Fill Data Sale Order Line In Sale Order Record
        """
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

    def merge_sale_order(self):
        """
        Merge The sale Order Line And Create New Sale Order
        Orders is Done
        """
        sale_r = self.env['batch.sale.workflow']
        act_id = self.env.context.get('active_id')
        record = sale_r.browse(act_id)
        batch_sale_obj = record.read(['partner_id', 'operation_date', 'sale_order_ids', 'status'])
        record.write({'status': 'done'})

        sale_order_id = []
        for sale_rec in batch_sale_obj:
            sale_order_id.extend(sale_rec['sale_order_ids'])

        order_line = []
        for product_rec in self.sale_order_line:
            order_line.append((0, 0, {
                'product_id': product_rec.product_id.id,
                'product_uom_qty': product_rec.quantity,
            }))

        sale_obj = self.env['sale.order'].search([('id', 'in', sale_order_id)])
        for sale_rec in batch_sale_obj:
            new_rec = sale_obj.create({
                'partner_id': sale_rec['partner_id'][0],
                'date_order': sale_rec['operation_date'],
            })

            new_rec.order_line = order_line

        sale_obj.action_cancel()
