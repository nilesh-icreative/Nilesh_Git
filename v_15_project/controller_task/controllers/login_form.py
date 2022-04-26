from odoo import http
from odoo.http import request


class Login(http.Controller):
    """ Login Form"""

    @http.route('/login_forms', type="http", auth="public", website=True)
    def login_forms(self, **kw):
        return http.request.render('controller_task.login_forms_page', {})
