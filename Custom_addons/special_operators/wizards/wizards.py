from odoo import models, api, fields

class sale_wizard(models.TransientModel):
    """ Sale Order Wizard """

    _name = 'sale_order_wizard'
    _description = ' sale wizard view'

    product_ids = fields.Many2many('product.product', string="Product Name")

    def create_order_lines(self):

        sale_dataset = self.env['sale.order']
        active_id = self.env.context.get('active_id')
        record = sale_dataset.browse(active_id)

        for product in self.product_ids:
            print("==============", product, product.id)
            record.write({'order_line': [(4, product.id)]})
