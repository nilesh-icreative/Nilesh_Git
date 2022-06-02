from odoo import http
from odoo.http import request


class ContactForm(http.Controller):

    @http.route("/create/contact", type="http", auth="public", website=True)
    def create_contacts(self, **kw):

        if kw:
            contact_record = {
                'name': kw.get('name'),
                'email': kw.get('email'),
                'phone': kw.get('phone'),
            }

            request.env['res.partner'].sudo().create(contact_record)
            return request.render(
                'frontend_paper.contacts_create_successfully', {}
            )
        else:
            return request.render(
                'frontend_paper.create_contacts_form_view', {}
            )

    @http.route(['/contacts_details'], type='http',
                auth='public', website=True)
    def contacts_details(self, **kw):
        contacts_details = request.env['res.partner'].sudo().search([])

        return request.render('frontend_paper.contacts_details_page',
                              {
                                  'details': contacts_details
                              })
