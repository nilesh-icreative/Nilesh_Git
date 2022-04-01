
from odoo import http
from odoo.http import request

class sale(http.Controller):
    """ Controllers display sale orders """

    @http.route(['/sale_details'], type='http', auth='public', website=True)
    def sale_details(self, **kw):
        sale_details = request.env['res.partner'].sudo().search([])

        return request.render('controller_task.sale_details_page',
                              {
                                  'details': sale_details
                              })
