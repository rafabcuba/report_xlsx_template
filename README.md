# Report XLSX Template for Odoo

This Odoo module allows generating XLSX reports for employees through a wizard. Users can select an employee and generate a report that is automatically downloaded with a meaningful name.

## Requirements

- Odoo 14 (or the compatible version you are using)
- Required modules: `hr` (Human Resource Management)
- Python library: `openpyxl` for XLSX file generation

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/report_xlsx_template.git
   ```

2. **Copy the module to Odoo's addons directory**:
   Place the `report_xlsx_template` folder in your Odoo installation's addons directory.

3. **Update the module list**:
   - Go to **Apps** within Odoo.
   - Click the update button (often represented by a reload icon) to let Odoo recognize your new module.

4. **Install the module**:
   - Once the module appears in the list, click `Install`.

## Usage

1. **Access the Module**:
   - Navigate to **Employees > Reports > XLSX Report**.

2. **Generate a Report**:
   - Select an employee from the dropdown list.
   - Click the `Generate Report` button.

3. **Download the Report**:
   - The XLSX report will automatically be downloaded with the name `Report_{Employee Name}.xlsx`.

## Module Structure

The module is organized as follows:

```
report_xlsx_template/
¦
+-- __init__.py                         # Initializes the module
+-- __manifest__.py                     # Module metadata
+-- models/
¦   +-- __init__.py                     # Initializes the models package
+-- reports/
¦   +-- __init__.py                     # Initializes the reports package
¦   +-- report_xlsx.py                  # XLSX report generation logic
+-- wizards/
¦   +-- __init__.py                     # Initializes the wizards package
¦   +-- wizard_report_xlsx.py           # Wizard logic for generating reports
+-- views/
    +-- __init__.py                     # Initializes the views package
    +-- report_xlsx_template.xml         # View and action definitions
    +-- xlsx/
        +-- template1.xlsx               # XLSX report template
```

## Customization

You can customize the Excel template (`template1.xlsx`) to suit your specific needs. Ensure you use a valid file structure to avoid issues with report generation.

## Dependencies

This module depends on the `openpyxl` library. Make sure it is installed in your Python environment. You can install it using pip:

```bash
pip install openpyxl
```

## Contributions

If you wish to contribute to this module, feel free to open an issue or submit a pull request on GitHub.

## License

This module is licensed under the [MIT License](LICENSE).

## Support

For issues or questions, please contact the module author or leave your concerns in the issues section of the repository.
