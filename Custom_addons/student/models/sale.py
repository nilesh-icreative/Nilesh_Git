# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import ValidationError , UserError

class sale(models.Model):
    """ Sale Order Object Inherit """

    _inherit = 'sale.order'

    mobile = fields.Char(string="Mobile No")
    email = fields.Char(string="Email")

    @api.onchange('partner_id')
    def change_values(self):
        for rec in self:
            if rec.partner_id:
                rec.email = rec.partner_id.email
                rec.mobile = rec.partner_id.phone

    @api.constrains('payment_term_id')
    def check_payment(self):
        for rec in self:
            if rec.payment_term_id:
                if rec.payment_term_id != rec.partner_id.property_supplier_payment_term_id:
                    raise UserError("Can't Match Payment Term")
