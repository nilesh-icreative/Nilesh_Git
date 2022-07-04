from odoo import fields, models, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    """
    Add Boolean Field in Website in Res Config Setting
    """
    group_covid_message_boolean = fields.Boolean(implied_group="29_06_22_frontend_paper.group_covid_message_boolean")
