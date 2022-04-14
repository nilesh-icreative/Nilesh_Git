from odoo import fields, models


class Sale_order_mail(models.Model):
    """ Sale Order Inherit """

    _inherit = 'sale.order'

    def send_mail(self):
        """ Send Mail Sale Order """
        print("======Hello========")

        template_id = self.env.ref('email_template.email_template_sale_order').id
        print("=======template id=======\n\n", template_id)

        template = self.env['mail.template'].browse(template_id)
        print("======template===\n\n", template)

        template.send_mail(self.id, force_send=True)
