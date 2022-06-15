from odoo.addons.portal.controllers import portal
from odoo.http import request


class PortalAccount(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super(PortalAccount, self)._prepare_home_portal_values(counters)
        values['sale_order_count'] = request.env['sale.order'].search_count([])
        return values

