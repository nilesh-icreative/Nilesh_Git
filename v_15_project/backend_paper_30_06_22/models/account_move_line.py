from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    length = fields.Float(string="Length", related='product_id.product_length')
    total_length = fields.Float(string="Total Length")
