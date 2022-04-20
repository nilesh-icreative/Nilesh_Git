
from odoo.exceptions import ValidationError
from odoo import models, fields, api

class smart(models.Model):

     _name = 'smart_button'
     _inherit = ['mail.thread','mail.activity.mixin']
     _description = 'smart_button'

     name = fields.Char(string="Name", tracking=True)
     dep = fields.Char(string="Department")
     r_no = fields.Integer(string="Roll No", tracking=True)


# Sql Constraints For Unique Record Store
     _sql_constraints={
          ('r_no_unique','unique(r_no)',"Roll No Mast Be Unique !")
     }

     _sql_constraints={
          ('name_unique','unique(name)',"Name Mast Be Unique !")
     }

# Api Constraints Not Store Condition Value

     @api.constrains('name')
     def check_name(self):
          if self.name == 'HHH':
               raise  ValidationError("HHH Name Not Allowed !")

     def icon(self):
          pass

     def chatter_button(self):

          for rec in self:
               display = "Name:" + rec.name + "<br/>" "Roll_No" + str(rec.r_no) + "<br/>" "Department:" + rec.dep
          self.message_post(body=display)

     def fetch_record(self):

          record = self.env['res.partner'].read([])
          print("===========================", record)