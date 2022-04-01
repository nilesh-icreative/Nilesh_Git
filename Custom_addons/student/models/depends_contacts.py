
from odoo import models, fields, api
from datetime import *
from odoo.exceptions import UserError

class contacts_depends(models.Model):

    _inherit = 'res.partner'

    con_age = fields.Integer(string="Age", compute="cal_age", store=True)

    @api.depends("dob")
    def cal_age(self):
        """ Calculate Age Function """
        if self.dob is not False:
            for rec in self:
                today = date.today()
                rec.con_age = today.year - rec.dob.year - ((today.month - today.day) < (rec.dob.month - rec.dob.day))


class sale_confirm(models.Model):

    _inherit = 'sale.order'

    def action_confirm(self):
        """ Sale Order Confirm Button """
        val = super(sale_confirm, self).action_confirm()

        for rec in self:
            count = len(rec.order_line)
            if count > 3:
                raise UserError("You can only add max 3 lines per order")

        return val
