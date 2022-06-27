from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    credit_limit = fields.Boolean(string="Credit Limit")
    blocking_limit = fields.Boolean(string="Blocking Limit")

    credit_limit_score = fields.Float(string="Credit Limit Score")
    blocking_limit_score = fields.Float(string="Blocking Limit Score")
    notify_person_email = fields.Char()
