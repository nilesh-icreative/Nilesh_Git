# -*- coding: utf-8 -*-
# from odoo import http


# class /home/odoo/workspace/projects/v15Project/(http.Controller):
#     @http.route('//home/odoo/workspace/projects/v_15_project///home/odoo/workspace/projects/v_15_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/odoo/workspace/projects/v_15_project///home/odoo/workspace/projects/v_15_project//objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/odoo/workspace/projects/v_15_project/.listing', {
#             'root': '//home/odoo/workspace/projects/v_15_project///home/odoo/workspace/projects/v_15_project/',
#             'objects': http.request.env['/home/odoo/workspace/projects/v_15_project/./home/odoo/workspace/projects/v_15_project/'].search([]),
#         })

#     @http.route('//home/odoo/workspace/projects/v_15_project///home/odoo/workspace/projects/v_15_project//objects/<model("/home/odoo/workspace/projects/v_15_project/./home/odoo/workspace/projects/v_15_project/"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/odoo/workspace/projects/v_15_project/.object', {
#             'object': obj
#         })
