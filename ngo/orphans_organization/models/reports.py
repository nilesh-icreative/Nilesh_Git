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

