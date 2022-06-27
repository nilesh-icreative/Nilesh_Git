from odoo import fields, models, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    notify_person_email = fields.Char(string="Notify Person Email", config_parameter="notify_email")
