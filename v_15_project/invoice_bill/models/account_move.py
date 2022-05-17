from odoo import models


class Account_Move(models.Model):
    """ Inherit Object Account Move"""

    _inherit = 'account.move'

    def bill_generate(self):
        """ Generate Bills"""

        vendor_ids = self.invoice_line_ids.mapped("vendor_id.id")
        #print("====================\n\n", vendor_ids)

        for vendor_id in vendor_ids:
            record_list = []

            for line in self.invoice_line_ids.filtered(lambda x: x.vendor_id.id == vendor_id):
                record_list.append((0, 0, {
                    "product_id": line.product_id.id,
                    "name": line.name,
                    "quantity": line.quantity,
                    "price_unit": line.price_unit,
                    "price_subtotal": line.price_subtotal,
                    "delivery_address_id": line.delivery_address_id,
                    "description": line.description,
                }))

            self.create({
                'move_type': 'in_invoice',
                'partner_id': vendor_id,
                'invoice_line_ids': record_list,

            })
