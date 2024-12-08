# -*- coding: utf-8 -*-

import base64
import os
import openpyxl
import io

from odoo import models, api, _


class ReportXlsx(models.TransientModel):
    _name = 'report.xlsx'
    _description = 'Report XLSX Wizard'

    @api.model
    def generate_xlsx_report(self, employee_id):
        # Load the template
        template_path = os.path.join(os.path.dirname(__file__), '..', 'views', 'xlsx', 'template1.xlsx')

        # Open and modify the Excel template
        workbook = openpyxl.load_workbook(template_path)
        sheet = workbook.active

        # Assume you want to put the employee name in cell B3
        employee = self.env['hr.employee'].browse(employee_id)
        sheet['B3'] = employee.name
        sheet['B8'] = 25
        sheet['B9'] = 30
        sheet['B10'] = 40

        # Save the file in memory
        output = io.BytesIO()
        workbook.save(output)
        output.seek(0)

        # Create an attachment
        file_data = base64.b64encode(output.read())
        output.close()

        return file_data
