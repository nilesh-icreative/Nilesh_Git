from odoo import models, fields, api

class sale(models.Model):

    _inherit = 'sale.order'

    c_rank = fields.Integer(related='partner_id.customer_rank')

    @api.model
    def create(self, vals):
        rec = super(sale, self).create(vals)
        if rec.partner_id.customer_rank > 2:
            best_cust_id = self.env.ref("special_operators.res_partner_add_tag_best_customer")
            #print("=====================ffff==", best_cust_id.id)
            rec.partner_id.write({'category_id': [(4, best_cust_id.id)]})

        return rec
