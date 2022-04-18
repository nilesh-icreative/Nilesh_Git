from odoo import models


class Account_Move(models.Model):
    """ Inherit Object Account Move"""

    _inherit = 'account.move'

    def bill_generate(self):
        """ Generate Bills"""

        vendor_list = []
        for rec in self.invoice_line_ids:
            if rec.vendor_id.id not in vendor_list:
                vendor_list.append(rec.vendor_id.id)

            # for product in rec:
            #     print("==================\n\n", rec.id, product.name, product.quantity,
            #           product.price_unit, product.price_subtotal, product.delivery_address_id.name,
            #           product.description)

        for rec in vendor_list:
            self.create([{
                'move_type': 'in_invoice',
                'partner_id': rec,
            }])

