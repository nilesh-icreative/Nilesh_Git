
from odoo import  models , fields


class demo_w(models.TransientModel):

    _name = "demo_w.faculty"

    name = fields.Many2one('res.partner',string="Customer Name")
    from_date = fields.Date(string="From")
    to_date = fields.Date(string="To")

    def print_wizard(self):
        print("Hello First Demo Program of Wizard////////////")
