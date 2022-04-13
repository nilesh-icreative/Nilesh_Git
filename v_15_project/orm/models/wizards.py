
from odoo import models , fields , api

class orm_wizard(models.TransientModel):
    _name = "ormw"
    _description = "orm create"

    name = fields.Char(string="Name")
    salary = fields.Integer(string="Salary")

    def btn_orm(self):
        pass

    # @api.model_create_multi
    # def create(self, vals_list):
    #     print("CREATEEEEEEEEEEE", vals_list)
    #     res = super().create(vals_list)
    #     print("resresres", res)
    #     return res

    def create(self, vals_list):
        print("CREATEEEEEEEEEEE", vals_list)
        res = super().create(vals_list)
        print("resresres", res)
        return res


