from odoo import models, fields, api
from odoo.exceptions import UserError
import base64


class WizardReportXlsx(models.TransientModel):
    _name = 'wizard.report.xlsx'
    _description = 'Wizard for generating XLSX report'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)

    def action_generate_report(self):
        # Check if an employee has been selected
        if not self.employee_id:
            raise UserError("Please select an employee.")

        report_data = self.env['report.xlsx'].generate_xlsx_report(self.employee_id.id)
        file_name = f"Report_{self.employee_id.name}.xlsx"

        # Create an attachment
        attachment = self.env['ir.attachment'].create({
            'name': file_name,
            'type': 'binary',
            'datas': report_data.decode('utf-8'),
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'res_model': 'wizard.report.xlsx',
            'res_id': self.id,
        })

        # Return an action to download the attachment
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'self',
            'nodestroy': True,
            'name': file_name,
        }
