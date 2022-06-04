from odoo import models, fields, api


class BatchSaleWorkflow(models.Model):
    _name = 'batch.sale.workflow'
    _description = 'batch.sale.workflow'

    name = fields.Char(readonly=True, required=True, copy=False, default='New')
    users_id = fields.Many2one(comodel_name="res.users", string="Responsible")
    operation_type = fields.Selection(
        [('con',     'Confirm'), ('can', 'Cancel'), ('mer', 'Merge')], required=True, default='con')

    partner_id = fields.Many2one(comodel_name="res.partner", string="Customer")
    status = fields.Selection(selection=[
        ('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel')],
        default="draft")

    sale_order_ids = fields.Many2many(comodel_name='sale.order')
    operation_date = fields.Date(string="Operation Date", required=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'self.service') or 'New'
        result = super(BatchSaleWorkflow, self).create(vals)
        return result

    @api.onchange('operation_type', 'partner_id', 'users_id')
    def _onchange_operation_type(self):
        if self.operation_type == 'con':
            return {'domain': {'sale_order_ids': ['|', ('state', '=', 'draft'), ('state', '=', 'sent'),
                                                  ('user_id', '=', self.users_id.id)]}}
        elif self.operation_type == 'can':
            print("===========hello\n\n")
            return {'domain': {'sale_order_ids': ['|', '|',  ('state', '=', 'draft'), ('state', '=', 'sent'),
                                                  ('state', '=', 'sale'), ('user_id', '=', self.users_id.id)]}}
        elif self.operation_type == 'mer':
            return {'domain': {'sale_order_ids': ['|', ('state', '=', 'draft'), ('state', '=', 'sent'),
                                                  ('partner_id', '=', self.partner_id.id),
                                                  ('user_id', '=', self.users_id.id)]}}

    def btn_proceed_operation(self):
        self.write({'status': 'done'})
        for order_rec in self.sale_order_ids:
            sale_order_record = self.env['sale.order'].search(
                [('id', '=', order_rec.id)]
            )
            sale_order_record.write({
                'date_order': self.operation_date,
            })

            if self.operation_type == 'con':
                sale_order_record.action_confirm()
            elif self.operation_type == 'can':
                sale_order_record.action_cancel()
            elif self.operation_type == 'mer':
                if self.sale_order_ids.order_line:
                    sale_order_record.create({
                        'partner_id': self.partner_id.id,
                        'order_line': self.sale_order_ids.order_line,
                    })
                sale_order_record.action_cancel()

    def btn_cancel(self):
        self.write({'status': 'cancel'})

    def btn_draft(self):
        self.write({'status': 'draft'})
