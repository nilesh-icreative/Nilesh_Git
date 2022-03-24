

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import *

class rental_management(models.Model):
    """  Rental Management Project """

    _name = 'rental.management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'rental_management'

    name = fields.Char(string="Name", required=True)
    customer = fields.Many2one('res.partner', string="Customer")
    rental_type = fields.Many2one('rental.type', string="Rental Type")
    s_date = fields.Date(string="Start Date")
    e_date = fields.Date(string="End Date")
    rental_product = fields.Many2one('product.product', string="Rental Product", domain=[('is_rental','=',True)])
#    c_id = fields.Many2one('res.currency', default=20)
    currency_id = fields.Many2one("res.currency", string="Currency", default=20, readonly=True)

    price = fields.Float(string="Price_p", related='rental_product.list_price',)

    state = fields.Selection(selection=[('draft', 'Draft'), ('waiting', 'Waiting'), ('approve', 'Approve'), ('cancle', 'Cancle')])

    def btn_draft(self):
        self.write({'state': 'draft'})

    def btn_waiting(self):
        self.write({'state': 'waiting'})

    def btn_approved(self):
        self.write({'state': 'approve'})

    _sql_constraints = {
        ('name_unique', 'unique(name)', "Name Must Be Unique !")
    }

    @api.constrains('s_date','e_date')
    def check_date(self):
        if self.s_date and self.e_date:
            for rec in self:
                s = datetime.strptime(str(rec.s_date),'%Y-%m-%d').date()
                e = datetime.strptime(str(rec.e_date),'%Y-%m-%d').date()

                if(e.day < s.day) or (e.month < s.month) or (e.year < e.year):
                    raise ValidationError("End Date Not Less Than Star Date")
                else:
                    pass
        else:
            raise ValidationError("Please Enter Date")














