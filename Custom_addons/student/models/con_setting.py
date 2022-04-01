
from odoo import models, fields, api

class conf_setting(models.TransientModel):

    _inherit = 'res.config.settings'

    is_bool = fields.Boolean()

    name = fields.Html()

    @api.onchange('is_bool')
    def onchange_name(self):
        if self.is_bool == False:
            self.name = False

    @api.model
    def get_values(self):
        rec = super(conf_setting, self).get_values()

        rec['is_bool'] = self.env['ir.config_parameter'].get_param('is_bool')
        rec['name'] = self.env['ir.config_parameter'].get_param('name')

        return rec

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param('is_bool', self.is_bool)
        self.env['ir.config_parameter'].set_param('name', self.name)
        super(conf_setting, self).set_values()

