from odoo import fields, models, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    """
    Add Boolean Field in Website in Res Config Setting
    """

    covid_message_boolean = fields.Boolean(config_parameter="covid_message")
