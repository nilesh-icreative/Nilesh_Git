# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime



class contacts(models.Model):

    _inherit = 'res.partner'
    dob = fields.Date(string='Date_of_Birth',required=False)
    customer_r = fields.Char(string="Customer_reference")
    category_id = fields.Many2many("res.partner.category", string="category")

    def search_mail(self):

        res_obj = self.search([])
        record_list = res_obj.read(['email', 'phone'])

        for rec in record_list:
            print(rec)

        val = res_obj.read(['email'])

        def not_false_email(val):
            for i in val:
                if i['email'] != False:
                    print(i)
        not_false_email(val)

        find_record = res_obj.browse([18, 35])
        dis = find_record.read(['name'])
        print("========Record=====\n", dis)

        # res_obj = self.env['res.partner'].search([])
        # print("=====Res Partner List Record=================\n", res_obj)
