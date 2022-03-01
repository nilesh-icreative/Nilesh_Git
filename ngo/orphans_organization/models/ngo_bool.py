
from odoo import models, fields, api

class ngo(models.Model):

    _inherit = 'res.partner'

    ngo_check = fields.Boolean(string="NGO",default="True")
