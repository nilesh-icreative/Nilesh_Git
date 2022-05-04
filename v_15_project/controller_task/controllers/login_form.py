from odoo import http
from odoo.http import request


class Login(http.Controller):
    """ Login Form"""

    @http.route('/login_forms', type="http", auth="public", website=True)
    def login_forms(self, **kw):
        return http.request.render('controller_task.login_forms_page', {})

    @http.route('/create/contacts', type="http", auth="public", website=True)
    def create_contacts(self, **kw):
        request.env['res.partner'].sudo().create(kw)
        return request.render(
            'controller_task.contacts_create_successfully', {})
