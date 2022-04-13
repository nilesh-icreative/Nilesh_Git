from odoo import models, fields
from odoo.tools.misc import xlwt
from xlwt import easyxf
from io import BytesIO
import base64


class Employee_Wizards(models.TransientModel):
    """ Hr Employee Excel report"""

    _name = 'excel_report_wizards'
    _description = 'excel_report_wizards'

    hr_employees_ids = fields.Many2many('hr.employee')
    start_date = fields.Date()
    end_date = fields.Date()
    excel_file = fields.Binary()

    def print_excel_report(self):
        filename = 'Timesheet.xls'

        workbook = xlwt.Workbook()

        worksheet = workbook.add_sheet('Timesheet')

        header_style = easyxf('font:height 500; align:horiz center;'
                              ' font:bold True;')

        Row1 = 5
        Row2 = 6
        Col1 = 1
        Col2 = 5

        worksheet.col(1).width = 256 * 20
        worksheet.col(2).width = 256 * 25
        worksheet.col(3).width = 256 * 25
        worksheet.col(4).width = 256 * 25
        worksheet.col(5).width = 256 * 20

        worksheet.write_merge(Row1, Row2, Col1, Col2,
                              "Timesheet", header_style)
        font = easyxf('align: horiz center;font:bold True;')

        worksheet.col(0).width = 3000
        Row = 7
        Col = 1
        worksheet.write(Row, Col, 'Employee Name', font)
        Col += 1
        worksheet.write(Row, Col, 'Project', font)
        Col += 1
        worksheet.write(Row, Col, 'Task', font)
        Col += 1
        worksheet.write(Row, Col, 'Description', font)
        Col += 1
        worksheet.write(Row, Col, 'Hours', font)

        for rec in self.hr_employees_ids:
            emp_records_set = self.env['account.analytic.line'].search(
                [('employee_id', '=', rec.id),
                 ('date', '>=', self.start_date),
                 ('date', '<=', self.end_date)])
            Col = 1
            Row += 1
            employee_name = rec.name
            worksheet.write(Row, Col, employee_name)

            total_hours = 0
            for emp_rec in emp_records_set:
                worksheet.write(Row, 2, emp_rec.project_id.name)
                worksheet.write(Row, 3, emp_rec.task_id.name)
                worksheet.write(Row, 4, emp_rec.name)
                worksheet.write(Row, 5, emp_rec.unit_amount)
                total_hours += emp_rec.unit_amount
                Row += 1

            worksheet.write(Row, 5, "Total Hours: {}".format(total_hours))

        fp = BytesIO()

        workbook.save(fp)

        fp.seek(0)

        excel_file = base64.encodebytes(fp.getvalue())

        fp.close()

        self.write({'excel_file': excel_file})

        url = ('web/content/?model=excel_report_wizards&download=true&'
               'field=excel_file&id=%s&filename=%s'
               % (self.id, filename))

        if self.excel_file:
            return {'type': 'ir.actions.act_url',
                    'url': url,
                    'target': 'new'}
