
from odoo import models , fields

class scheduled(models.Model):
    """ Scheduled Actions in Sale Order """

    _inherit = "sale.order"

    def demo_action(self):
        rec = self.search([('state', 'in', ['draft', 'sent'])])
        #print("\n\n", rec,"\n\n")
        rec.action_confirm()




