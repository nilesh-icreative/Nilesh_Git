from odoo import http
from odoo.http import request
import base64

class ContactForm(http.Controller):

    @http.route("/create/contact", type="http", auth="public", website=True)
    def create_contacts(self, **kw):
        if kw:
            new_files = request.httprequest.files.getlist('image_1920')
            for file in new_files:
                partner = request.env['res.partner'].create({
                    'name': kw.get('name'),
                    'email': kw.get('email'),
                    'phone': kw.get('phone'),
                    'image_1920': base64.b64encode(file.read())
                })
            return request.render(
                    'frontend_paper.contacts_create_successfully', {}
            )
        else:
            return request.render(
                'frontend_paper.create_contacts_form_view_id', {}
            )

    @http.route(['/contacts_details'], type='http',
                auth='public', website=True)
    def contacts_details(self, **kw):
        contacts_details = request.env['res.partner'].sudo().search([])

        return request.render('frontend_paper.contacts_details_page',
                              {
                                  'details': contacts_details
                              })
