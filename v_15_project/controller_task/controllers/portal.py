from odoo.addons.portal.controllers import portal
from odoo.http import request


class CustomerPortal(portal.CustomerPortal):
    """ Website My Account Add Field """

    def _prepare_home_portal_values(self, counters):
        """ Record count """

        values = super()._prepare_home_portal_values(counters)
        values['contacts_count'] = request.env['res.partner'].search_count([])

        return values
