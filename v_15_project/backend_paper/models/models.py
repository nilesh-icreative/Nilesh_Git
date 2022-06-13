from odoo import models, fields, api
import json

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

    user_domain = fields.Char(compute="_responsible_user", readonly=True, store=False)

    @api.depends('users_id', 'operation_type', 'partner_id')
    def _responsible_user(self):
        for rec in self:
            if rec.operation_type == 'con':
                rec.user_domain = json.dumps([
                    ('user_id', '=', rec.users_id.id),
                    ('state', 'in', ['draft', 'sent'])
                ])
            elif rec.operation_type == 'can':
                rec.user_domain = json.dumps([
                    ('user_id', '=', rec.users_id.id),
                    ('state', 'in', ['draft', 'sent', 'sale'])
                ])
            elif rec.operation_type == 'mer':
                rec.user_domain = json.dumps([
                    ('user_id', '=', rec.users_id.id),
                    ('state', 'in', ['draft', 'sent']),
                    ('partner_id', '=', rec.partner_id.id)
                ])

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'self.service') or 'New'
        result = super(BatchSaleWorkflow, self).create(vals)
        return result

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
                order_line = []
                for product_rec in self.sale_order_ids.order_line:
                    order_line.append((0, 0, {
                        'product_id': product_rec.product_id.id,
                        'product_uom_qty': product_rec.product_uom_qty,
                    }))
                new_sale_order = sale_order_record.create({
                    'partner_id': self.partner_id.id,
                    'date_order': self.operation_date,
                })
                new_sale_order.order_line = order_line
                sale_order_record.action_cancel()

    def btn_cancel(self):
        self.write({'status': 'cancel'})

    def btn_draft(self):
        self.write({'status': 'draft'})
