# -*- coding: utf-8 -*-

from odoo import models, fields, api



class sale(models.Model):

    _inherit = 'sale.order'

    customer_Email = fields.Char(string="Customer Email", compute="_name_search", store=True)

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=50, name_get_uid=None):
        args = args or []
        domain = []

        if name:
            domain = [('email', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
