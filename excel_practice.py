import os
import copy
import openpyxl
from openpyxl import Workbook

def convert_excel(file_path, status_label):
    try:
        status_label.config(text="Processing...", fg="blue")

        input_wb = openpyxl.load_workbook(file_path)
        output_wb = Workbook()
        output_wb.remove(output_wb.active)  # Remove default sheet

        for sheet_name in input_wb.sheetnames:
            source_ws = input_wb[sheet_name]
            target_ws = output_wb.create_sheet(title=sheet_name)

            # Copy cell values and styles
            for row_idx, row in enumerate(source_ws.iter_rows(), 1):
                for col_idx, cell in enumerate(row, 1):
                    new_cell = target_ws.cell(row=row_idx, column=col_idx, value=cell.value)

                    if cell.has_style:
                        new_cell.font = copy.copy(cell.font)
                        new_cell.fill = copy.copy(cell.fill)
                        new_cell.border = copy.copy(cell.border)
                        new_cell.number_format = cell.number_format
                        new_cell.protection = copy.copy(cell.protection)
                        new_cell.alignment = copy.copy(cell.alignment)

            # Copy row and column dimensions
            for row_dim in source_ws.row_dimensions:
                target_ws.row_dimensions[row_dim] = copy.copy(source_ws.row_dimensions[row_dim])
            for col_dim in source_ws.column_dimensions:
                target_ws.column_dimensions[col_dim] = copy.copy(source_ws.column_dimensions[col_dim])

            # Copy conditional formatting (includes flags/icons)
            target_ws.conditional_formatting = copy.deepcopy(source_ws.conditional_formatting)

            # Now convert values where applicable
            for row in target_ws.iter_rows():
                for cell in row:
                    if cell.value is None or (isinstance(cell.value, str) and str(cell.value).startswith('=')):
                        continue
                    if '0%' in cell.number_format or '%' in cell.number_format:
                        continue
                    if isinstance(cell.value, (int, float)):
                        cell.value = round(cell.value / 1.95583, 2)
                        cell.number_format = '"€"#,##0.00'

        # Save output
        base = os.path.basename(file_path)
        name, ext = os.path.splitext(base)
        output_path = os.path.join(os.getcwd(), f"{name}_EUR{ext}")
        output_wb.save(output_path)

        status_label.config(text="Conversion completed!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")
