from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        """
        Confirm button click check Block limit amount
        """
        so = super(SaleOrder, self).action_confirm()

        sale_order_obj_block = self.env['sale.order'].search([('partner_id', '=', self.partner_id.id),
                                                              ('state', '=', 'sale')])
        block_limit = 0
        block_limit += self.amount_total
        for sale_rec in sale_order_obj_block:
            block_limit += sale_rec['amount_total']

        if block_limit > self.partner_id.blocking_limit_score:
            raise ValidationError("You cannot create SO as the Block Limit has been Exceeded")

        return so

    def action_draft(self):
        """
        set Quotation button click check credit limit amount
        """
        so = super(SaleOrder, self).action_draft()

        sale_order_obj_credit = self.env['sale.order'].search([('partner_id', '=', self.partner_id.id),
                                                               ('state', '=', 'draft')])
        credit_amount = 0
        credit_amount += self.amount_total
        for sale_rec_credit in sale_order_obj_credit:
            credit_amount += sale_rec_credit['amount_total']

        if credit_amount > self.partner_id.credit_limit_score:
            raise ValidationError("Your Sale Order Credit Limit has been Exceeded.")

        return so

    def mail_trigger(self):
        """
        Notify Person send mail Customer limit is exceeds
        """
        template_id = self.env.ref(
            'exam_paper.email_template_limit_customer').id

        template = self.env['mail.template'].browse(template_id)

        template.send_mail(self.id, force_send=True)

    def create(self, val):
        """
        Check Credit SCore For Particular User
        Limit is Over Than Display Error Message
        """

        so = super(SaleOrder, self).create(val)
        so.action_draft()
        return so

    # def write(self, vals):
    #     """
    #
    #     """
    #     so = super(SaleOrder, self).write(vals)
    #
    #     # sale_obj = self.env['sale.order'].search([('id', '=', self.id)]).read([])
    #     # sale_obj.action_draft()
    #     return so
