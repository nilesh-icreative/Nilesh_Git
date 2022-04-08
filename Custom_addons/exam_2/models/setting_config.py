
from odoo import models, fields, api
from datetime import date


class conf_setting(models.TransientModel):
    """ Setting """

    _inherit = 'res.config.settings'

    today = date.today()
    module_employee = fields.Boolean()
    sale_order_details_ids = fields.Many2many(
        comodel_name='sale.order',
        domain=[('date_order', 'like', today.month),
                ('date_order', 'like', today.year)])

    @api.model
    def get_values(self):
        rec = super(conf_setting, self).get_values()
        rec['module_employee'] = self.env[
            'ir.config_parameter'].get_param('module_employee')

        sale_details = self.env[
            'ir.config_parameter'].get_param('sale_order_details_ids')

        if sale_details:
            rec.update(
                sale_order_details_ids=[(6, 0, eval(sale_details))],
            )

        return rec

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param('module_employee',
                                                  self.module_employee)

        self.env['ir.config_parameter'].set_param(
            'sale_order_details_ids', self.sale_order_details_ids.ids)
        super(conf_setting, self).set_values()
