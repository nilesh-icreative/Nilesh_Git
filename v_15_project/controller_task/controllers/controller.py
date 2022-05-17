from odoo import http
from odoo.http import request


class Contacts(http.Controller):
    """ Controllers display  Contacts Details"""

    @http.route(['/contacts_details'], type='http', auth='public',
                website=True)
    def contacts_details(self, **kw):
        contacts_details = request.env['res.partner'].sudo().search([])

        return request.render('controller_task.contacts_details_page',
                              {
                                  'details': contacts_details
                              })

    @http.route(["/contacts_details/<model('res.partner'):con>/"], type="http",
                auth='public', website=True)
    def person_details(self, con, **data):
        return http.request.render('controller_task.person_details_page',
                                   {
                                       'con': con
                                   })
