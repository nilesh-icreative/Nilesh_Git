from odoo import models, fields
from odoo.tools.misc import xlwt
from xlwt import easyxf
from io import BytesIO
import base64
from datetime import date


class Organization_Reports(models.TransientModel):

    _name = "reports"
    _description = "reports"

    excel_file_donation = fields.Binary()
    excel_file_expense = fields.Binary()
    excel_file_profit = fields.Binary()

    date = fields.Date(default=date.today())

    def organization_report_donation(self):

        organization_record_set = self.env['res.partner'].search([('ngo_check', '=', True)])

        filename = 'Donation_report.xls'

        workbook = xlwt.Workbook()

        worksheet = workbook.add_sheet('Donation Report')

        header_style = easyxf('font:height 500;'
                              'font:bold True;'
                              'font:bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                                           left thin, right thin, top thin, bottom thin;'
                              )

        header_date = easyxf('font:height 230,bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                             left thin, right thin, top thin, bottom thin;')

        Row1 = 2
        Row2 = 3
        Col1 = 1
        Col2 = 5

        worksheet.col(1).width = 256 * 25
        worksheet.col(2).width = 256 * 15
        worksheet.col(3).width = 256 * 25
        worksheet.col(4).width = 256 * 15
        worksheet.col(5).width = 256 * 20

        worksheet.write_merge(Row1, Row2, Col1, Col2,
                              "Donation Report", header_style)

        worksheet.write_merge(4, 4, 1, 5,
                              "Date:" + str(self.date), header_date)

        col_name = easyxf('font:bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                                       left thin, right thin, top thin, bottom thin;'
                          )

        col_data = easyxf('align: horiz left; borders: top_color black, bottom_color black, right_color black, left_color black,\
                             left thin, right thin, top thin, bottom thin;')

        worksheet.col(0).width = 3000
        Row = 6
        Col = 1
        worksheet.write(Row, Col, 'Organization Name', col_name)
        Col += 1
        worksheet.write(Row, Col, 'Donor Name', col_name)
        Col += 1
        worksheet.write(Row, Col, 'Email', col_name)
        Col += 1
        worksheet.write(Row, Col, 'Phone No', col_name)
        Col += 1
        worksheet.write(Row, Col, 'Amount', col_name)

        for rec in organization_record_set:

            donation_record_set = self.env['orphans.organization.donation'].search([('o_organization', '=', rec.id)])

            Col = 1
            Row += 1
            organization_name = rec.name
            worksheet.write(Row, Col, organization_name, col_data)

            total_amount = 0
            for rec in donation_record_set:

                worksheet.write(Row, 2, rec.name, col_data)
                worksheet.write(Row, 3, rec.email, col_data)
                worksheet.write(Row, 4, rec.phone, col_data)
                worksheet.write(Row, 5, rec.amount, col_data)

                total_amount += rec.amount
                Row += 1

            worksheet.write_merge(Row, Row, 1, 5, "Total Amount: {}".format(total_amount), col_name)
            Row += 1

        fp = BytesIO()

        workbook.save(fp)

        fp.seek(0)

        excel_file = base64.encodebytes(fp.getvalue())

        fp.close()

        self.write({'excel_file_donation': excel_file})

        url = ('web/content/?model=reports&download=true&'
               'field=excel_file_donation&id=%s&filename=%s'
               % (self.id, filename))

        if self.excel_file_donation:
            return {'type': 'ir.actions.act_url',
                    'url': url,
                    'target': 'new'}

    def organization_report_expense(self):

        organization_record_set = self.env['res.partner'].search([('ngo_check', '=', True)])

        filename = 'Expense_report.xls'

        workbook = xlwt.Workbook()

        worksheet = workbook.add_sheet('Expense Report')

        header_style = easyxf('font:height 500;'
                              'font:bold True;'
                              'font:bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                                           left thin, right thin, top thin, bottom thin;'
                              )

        header_date = easyxf('font:height 230,bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                     left thin, right thin, top thin, bottom thin;')

        Row1 = 2
        Row2 = 3
        Col1 = 1
        Col2 = 4

        worksheet.col(1).width = 256 * 25
        worksheet.col(2).width = 256 * 15
        worksheet.col(3).width = 256 * 25
        worksheet.col(4).width = 256 * 15

        worksheet.write_merge(Row1, Row2, Col1, Col2,
                              "Expense Report", header_style)

        worksheet.write_merge(4, 4, 1, 4,
                              "Date:" + str(self.date), header_date)

        col_name = easyxf('font:bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                                               left thin, right thin, top thin, bottom thin;'
                          )

        col_data = easyxf('align: horiz left; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                     left thin, right thin, top thin, bottom thin;')

        worksheet.col(0).width = 3000
        Row = 6
        Col = 1
        worksheet.write(Row, Col, 'Organization Name', col_name)
        Col += 1
        worksheet.write(Row, Col, 'Expense User', col_name)
        Col += 1
        worksheet.write(Row, Col, 'Expense Type', col_name)
        Col += 1
        worksheet.write(Row, Col, 'Amount', col_name)

        for rec in organization_record_set:

            expense_record_set = self.env['orphans.organization.expense'].search([('od_organization', '=', rec.id)])

            Col = 1
            Row += 1
            organization_name = rec.name
            worksheet.write(Row, Col, organization_name, col_data)

            total_amount = 0
            for rec in expense_record_set:
                worksheet.write(Row, 2, rec.name_user, col_data)
                worksheet.write(Row, 3, rec.name.name, col_data)
                worksheet.write(Row, 4, rec.e_amount, col_data)

                total_amount += rec.e_amount
                Row += 1

            worksheet.write_merge(Row, Row, 1, 4, "Total Amount: {}".format(total_amount), col_name)
            Row += 1

        fp = BytesIO()

        workbook.save(fp)

        fp.seek(0)

        excel_file = base64.encodebytes(fp.getvalue())

        fp.close()

        self.write({'excel_file_expense': excel_file})

        url = ('web/content/?model=reports&download=true&'
               'field=excel_file_expense&id=%s&filename=%s'
               % (self.id, filename))

        if self.excel_file_expense:
            return {'type': 'ir.actions.act_url',
                    'url': url,
                    'target': 'new'}

    def organization_report_profit(self):

        organization_record_set = self.env['res.partner'].search([('ngo_check', '=', True)])

        filename = 'Profit_report.xls'

        workbook = xlwt.Workbook()

        worksheet = workbook.add_sheet('Profit Report')

        header_style = easyxf('font:height 500;'
                              'font:bold True;'
                              'font:bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                                           left thin, right thin, top thin, bottom thin;'
                              )

        header_date = easyxf('font:height 230,bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                     left thin, right thin, top thin, bottom thin;')

        Row1 = 2
        Row2 = 3
        Col1 = 1
        Col2 = 6

        worksheet.col(1).width = 256 * 25
        worksheet.col(2).width = 256 * 5
        worksheet.col(3).width = 256 * 15
        worksheet.col(4).width = 256 * 20
        worksheet.col(5).width = 256 * 15
        worksheet.col(7).width = 256 * 5

        worksheet.write_merge(Row1, Row2, Col1, Col2,
                              "Profit Report", header_style)

        worksheet.write_merge(4, 4, 1, 6,
                              "Date:" + str(self.date), header_date)

        col_name = easyxf('font:bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                                               left thin, right thin, top thin, bottom thin;'
                          )

        profit_loss = easyxf('font:bold True;pattern: pattern solid, fore_colour red;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                                                       left thin, right thin, top thin, bottom thin;'
                             )

        profit_win = easyxf('font:bold True;pattern: pattern solid, fore_colour green;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                                                               left thin, right thin, top thin, bottom thin;'
                            )

        col_data = easyxf('align: horiz left; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                     left thin, right thin, top thin, bottom thin;')

        expense_amount_data = easyxf('align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                             left thin, right thin, top thin, bottom thin;')



        worksheet.col(0).width = 3000

        Row = 7
        Col = 1

        for rec in organization_record_set:

            donation_record_set = self.env['orphans.organization.donation'].search([('o_organization', '=', rec.id)])
            expense_record_set = self.env['orphans.organization.expense'].search([('od_organization', '=', rec.id)])

            worksheet.write_merge(Row, Row, Col, Col, 'Organization Name', col_name)
            Col += 2
            worksheet.write_merge(Row, Row, Col, Col, 'Donor Name', col_name)
            Col += 1
            worksheet.write_merge(Row, Row, Col, Col, 'Email', col_name)
            Col += 1
            worksheet.write_merge(Row, Row, Col, Col, 'Phone No', col_name)
            Col += 1
            worksheet.write_merge(Row, Row, Col, Col, 'Amount', col_name)

            print(Row)
            print(Col)

            Col = 1
            Row += 1
            organization_name = rec.name
            worksheet.write(Row, Col, organization_name, col_data)

            total_amount_donation = 0
            total_amount_expense = 0

            for rec in donation_record_set:
                worksheet.write(Row, 3, rec.name, col_data)
                worksheet.write(Row, 4, rec.email, col_data)
                worksheet.write(Row, 5, rec.phone, col_data)
                worksheet.write(Row, 6, rec.amount, col_data)

                total_amount_donation += rec.amount
                Row += 1

            worksheet.write_merge(Row, Row, 3, 6, "Donation Amount: {}".format(total_amount_donation), col_name)
            Row += 2
            worksheet.write_merge(Row, Row, 3, 3, "Expense User", col_name)
            worksheet.write_merge(Row, Row, 4, 4, "Expense Type", col_name)
            worksheet.write_merge(Row, Row, 5, 6, "Amount", col_name)
            Row += 1

            for expense_record in expense_record_set:
                worksheet.write(Row, 3, expense_record.name_user, col_data)
                worksheet.write(Row, 4, expense_record.name.name, col_data)
                worksheet.write_merge(Row, Row, 5, 6, expense_record.e_amount, expense_amount_data)

                total_amount_expense += expense_record.e_amount
                Row += 1

            Row += 1
            worksheet.write_merge(Row, Row, 3, 6, "Expense Amount: {}".format(total_amount_expense), col_name)

            profit_amount = total_amount_donation - total_amount_expense
            if profit_amount > 0:
                worksheet.write_merge(Row, Row, 1, 1, "Profit Amount: {}".format(profit_amount), profit_win)
                Row += 1
            elif profit_amount == 0:
                worksheet.write_merge(Row, Row, 1, 1, "Profit Amount: {}".format(profit_amount), profit_win)
                Row += 1
            else:
                worksheet.write_merge(Row, Row, 1, 1, "Loss Amount: {}".format(profit_amount), profit_loss)
                Row += 1

            Row += 1

        fp = BytesIO()

        workbook.save(fp)

        fp.seek(0)

        excel_file = base64.encodebytes(fp.getvalue())

        fp.close()

        self.write({'excel_file_donation': excel_file})

        url = ('web/content/?model=reports&download=true&'
               'field=excel_file_donation&id=%s&filename=%s'
               % (self.id, filename))

        if self.excel_file_donation:
            return {'type': 'ir.actions.act_url',
                    'url': url,
                    'target': 'new'}
