# -*- coding: utf-8 -*-
{
    'name': "report_xlsx_template",

    'summary': """
        A wizard for generating XLSX reports for employees,  
        allowing users to easily create and download reports.""",

    'description': """
        This module provides a user-friendly wizard that enables   
        the generation of Excel XLSX reports for individual employees.  
        Users can select an employee from the list, and upon   
        triggering the report generation action, an Excel file   
        is created and downloaded automatically. This module is   
        designed to enhance reporting capabilities within the   
        Human Resources management system in Odoo and as a demonstration of
        using xlsx templates for complex reporting.
    """,

    'author': "Rafael Enrique Báez Guevara <rafabcuba@gmail.com>",
    'website': "https://www.linkedin.com/in/rafabcuba",

    'category': 'HR',
    'version': '0.1',

    'depends': ['base', 'hr', 'report_xlsx'],

    'data': [
        'security/ir.model.access.csv',
        'views/report_xlsx_template.xml',
    ],
    'external_dependencies': {
        'python': ['openpyxl']
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
