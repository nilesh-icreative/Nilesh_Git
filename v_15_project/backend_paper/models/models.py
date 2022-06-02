from odoo import models, fields, api


class BatchSaleWorkflow(models.Model):
    _name = 'batch.sale.workflow'
    _description = 'batch.sale.workflow'

    name = fields.Char(required=True)
    users_id = fields.Many2one(comodel_name="res.users", string="Responsible")
    operation_type = fields.Selection(
        [('con', 'Confirm'), ('can', 'Cancel'), ('mer', 'Merge')],
        default="con", required=True)

    partner_id = fields.Many2one(comodel_name="res.partner", string="Customer")
    status = fields.Selection(selection=[
        ('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel')],
        default="draft")

    sale_order_ids = fields.Many2many(comodel_name='sale.order')
    operation_date = fields.Date(string="Operation Date")

    @api.onchange('operation_type')
    def _onchange_operation_type(self):
        if self.operation_type == 'con':
            return {'domain': {
                'sale_order_ids': ['|', ('state', '=', 'draft'),
                                   ('state', '=', 'sent')
                                   ]
            }}

        elif self.operation_type == 'cancel':
            return {'domain': {
                'sale_order_ids': ['|', ('state', '=', 'draft'),
                                   ('state', '=', 'sent'),
                                   ('state', '=', 'sale')
                                   ]
            }}

        elif self.operation_type == 'mer':
            return {'domain': {
                'sale_order_ids': ['|',
                                   ('state', '=', 'draft'),
                                   ('state', '=', 'sent')
                                   ]
            }}
        else:
            pass

    def btn_proceed_operation(self):
        self.write({'status': 'done'})

        for order_rec in self.sale_order_ids:
            print("================", order_rec)
            sale_order_record = self.env['sale.order'].search(
                [('id', '=', order_rec.id)]
            )

            sale_order_record.write({
                'date_order': self.operation_date,
            })

    def btn_cancel(self):
        self.write({'status': 'cancel'})

    def btn_draft(self):
        self.write({'status': 'draft'})
