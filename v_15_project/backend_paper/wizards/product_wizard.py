from odoo import models, fields, api

class Product(models.TransientModel):
    """ Product Wizard"""

    _name = 'product'
    _description = 'product'

    sale_order_line = fields.One2many(comodel_name='order_line',
                                      inverse_name='sale_order_id')

    @api.model
    def default_get(self, field):

        sale_r = self.env['sale.order']
        act_id = self.env.context.get('active_id')
        record = sale_r.browse(act_id)
        print("=========\n\n", record)
        order_line = record.read(['sale_order_ids'])
        print("======\n\n", order_line)

        so = super(Product, self).default_get(field)

        return so
