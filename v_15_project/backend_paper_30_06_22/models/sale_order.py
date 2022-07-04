from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    product_id = fields.Many2one(comodel_name="product.product")
    product_qty = fields.Float(default=1)

    @api.onchange('product_id', 'product_qty')
    def _create_sale_order_line(self):
        """
        Create Sale Order Line
        Calculate Subtotal and Total Length
        """
        product_unique_id = []
        for sale_rec in self.order_line:
            product_unique_id.append(sale_rec.product_id.id)

        if self.product_id.id:
            order_line = []
            for sale_rec in self:
                if self.product_id.id not in product_unique_id:
                    order_line.append((0, 0, {
                        'product_id': sale_rec.product_id.id,
                        'name': sale_rec.product_id.name,
                        'product_uom_qty': sale_rec.product_qty,
                        'price_unit': sale_rec.product_id.list_price,
                        'product_uom': sale_rec.product_id.uom_id.id,
                    }))

                self.update({
                        'order_line': order_line
                    })

            for sale_rec in self.order_line:
                if sale_rec.product_id.id == self.product_id.id:
                    sale_rec.product_uom_qty = self.product_qty
                    sale_rec.total_length = sale_rec.product_uom_qty * sale_rec.length
                    sale_rec.price_subtotal = sale_rec.product_uom_qty * sale_rec.length * sale_rec.price_unit

    def _create_invoices(self, grouped=False, final=False, date=None):
        """
        Add Total Length Value in Invoice
        """
        so = super(SaleOrder, self)._create_invoices()

        for sale_rec in self.order_line:
            for invo_rec in so.invoice_line_ids:
                if invo_rec.product_id.id == sale_rec.product_id.id:
                    invo_rec.total_length = sale_rec.total_length
        return so
