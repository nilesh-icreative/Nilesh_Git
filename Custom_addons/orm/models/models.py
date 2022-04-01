# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class orm(models.Model):
    _name = 'orm'
    _description = 'orm.orm'

    emp_id = fields.Integer(string="Employee Id")
    name = fields.Char(string='Employee Name')
    emp_salary = fields.Integer(string="Employee Salary")
    stat = fields.Selection(selection=[('orm', 'orm'), ('orm_1', 'orm_1')])


    def orm_create(self):
        self.create({'emp_id': '1', 'name': 'Nilesh', 'emp_salary': '5000'})

    def orm_copy(self):
        self.copy()
        # for i in range(5):
        #     self.copy()

    def orm_write(self):
        self.write({'name': 'Max','emp_id':'1000','emp_salary': '20000'})

    def orm_browse(self):
        print("ORm Browse is===============:",self.browse([11]))
        # rec = self.browse([1])
        # print(rec.name)

    def orm_search(self):
        pass

    def orm_search_count(self):
        pass

    def orm_unlink(self):
        self.unlink()

    def orm_exists(self):
        rec = self.browse([1])
        if rec.exists():
            raise ValidationError("Record Exists")
        else:
            raise ValidationError("Record Dosen't exists")

    def orm_ensure_one(self):
        pass

    def orm_filtered(self):
        pass

    def orm_mapped(self):
        rec = self
        print("Mapping:",rec.mapped(lambda x:x.emp_id + x.emp_salary))

    def orm_sorted(self):
        print("Sorted=======",self.sorted(lambda x:x.name, reverse=False))

    def write(self, vals):
        print("write Method==========", vals)

        vals.update({
            'name': 'Nilesh'
        })
        print("Values===================", vals)
        res = super().write(vals)
        print("write---res", res)
        return res

    @api.model_create_multi
    def create(self, vals_list):
        print("Create Method=======", vals_list)
        res = super().create(vals_list)
        print("Create----res user====", res)
        return res

    def unlink(self):
        print("Unlink Method========", self)
        res = super().unlink()
        print("unlin ===========res", res)
        return res