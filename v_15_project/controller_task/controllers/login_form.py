from odoo import http
from odoo.http import request


class Login(http.Controller):
    """ Login Form"""

    @http.route('/login_forms', type="http", auth="public", website=True)
    def login_forms(self, **kw):
        return http.request.render('controller_task.login_forms_page', {})

    @http.route(["/login_forms/<model('res.partner'):con>/"], type="http",
                auth='public', website=True)
    def person_details(self, con, **kw):
        return http.request.render('controller_task.login_forms_page', {
            'data': con,
        })

    @http.route("/create/contacts", type="http",
                auth="public", website=True)
    def create_contacts(self, **kw):

        if kw.get('contact_id'):
            data = request.env['res.partner'].sudo().search([('id', '=', kw.get('contact_id'))])
            data.write({
                'name': kw.get('name'),
                'phone': kw.get('phone'),
                'email': kw.get('email'),
            })
            return request.redirect('/contacts_details')
        else:
            request.env['res.partner'].sudo().create(kw)
            return request.render(
                'controller_task.contacts_create_successfully', {}
            )
