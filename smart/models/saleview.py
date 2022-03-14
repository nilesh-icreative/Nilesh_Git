# -*- coding: utf-8 -*-

from odoo import models, fields, api


class orm_wizard(models.TransientModel):

    _name = 'sale_wizard'
    _description = ' sale wizard view'

    c_name = fields.Char(string="Customer", required=True)
    c_email = fields.Char(string="Customer Email")
    s_p = fields.Char(string="Sale Person")
    s_p_c = fields.Char(string="Sale Person Contact")
    p_t = fields.Char(string="Payment Terms")

    @api.model
    def default_get(self, field):

        sale_r = self.env['sale.order']
        act_id = self.env.context.get('active_id')
        record = sale_r.browse(int(act_id))
        val = record.read(['partner_id', 'email', 'mobile', 'user_id', 'payment_term_id'])
        so = super(orm_wizard, self).default_get(field)

        for i in val:

            so['c_name'] = i["partner_id"][1]
            so['c_email'] = i["email"]
            so['s_p_c'] = i["mobile"]
            so['s_p'] = i["user_id"][1]
            so['p_t'] = i["payment_term_id"][1]

        return so


