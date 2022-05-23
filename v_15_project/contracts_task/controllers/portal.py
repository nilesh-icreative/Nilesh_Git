from odoo import http
from odoo.addons.portal.controllers import portal
from odoo.http import request
import base64


class Contracts_Count(portal.CustomerPortal):
    """ Contracts Count """

    def _prepare_home_portal_values(self, counters):
        user_id = request.env.user.employee_id.id
        values = super()._prepare_home_portal_values(counters)
        values['contracts_count'] = request.env['hr.contract'].sudo().search_count(
            [('employee_id', '=', user_id)]
        )

        return values


class Contracts_Portal(http.Controller):
    """ Controllers display  Contracts List"""
    @http.route(['/my/contracts'], type='http', auth='public',
                website=True)
    def contacts_details(self, **kw):

        user_id = request.env.user.employee_id.id
        contracts_details = request.env['hr.contract'].sudo().search(
            [('employee_id', '=', user_id)]
        )

        return request.render('contracts_task.contracts_list_page',
                              {
                                  'details': contracts_details
                              })

    @http.route(["/my/contracts/<model('hr.contract'):con>/"], type="http",
                auth='public', website=True)
    def person_details(self, con, **kw):
        return http.request.render('contracts_task.contracts_details_page',
                                   {
                                       'con': con
                                   })

    @http.route('/file/upload', type='http', auth="public", website=True)
    def upload_files(self, **kw):
        """Attachment Store"""

        if kw.get('image_upload'):
            project_id = kw.get('project_id')
            attached_files = request.httprequest.files.getlist('image_upload')
            for attachment in attached_files:
                attached_file = attachment.read()
                request.env['ir.attachment'].sudo().create(
                    {
                        'name': attachment.name,
                        'type': 'binary',
                        'res_model': 'hr.contract',
                        'res_id': project_id,
                        'datas': base64.b64encode(attached_file),
                    }
                )

        return request.render(
            'contracts_task.attachment_create_successfully', {})
