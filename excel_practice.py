import xlwings as xw
import os

def convert_excel(file_path, status_label):
    try:
        status_label.config(text="Processing...", fg="blue")

        app = xw.App(visible=False)
        wb = app.books.open(file_path)

        for sheet in wb.sheets:
            if sheet.name != "indicators":
                continue

            used_range = sheet.used_range
            values = used_range.value
            formats = used_range.number_format

            # Make sure it's a 2D list even for single row/col
            if not isinstance(values[0], list):
                values = [values]
                formats = [formats]

            for i, row in enumerate(values):
                for j, val in enumerate(row):
                    fmt = formats[i][j] if isinstance(formats[i], list) else formats[i]
                    if val is None or isinstance(val, str) and str(val).startswith('='):
                        continue
                    if fmt and ('%' in fmt or '0%' in fmt):
                        continue
                    if isinstance(val, (int, float)):
                        used_range[i+1, j+1].value = val / 1.95583  # +1 because xlwings uses 1-based indexing

        base = os.path.basename(file_path)
        name, ext = os.path.splitext(base)
        output_path = os.path.join(os.getcwd(), f"{name}_EUR{ext}")
        wb.save(output_path)
        wb.close()
        app.quit()
        status_label.config(text="Conversion complete", fg="green")

    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")


# New option
import openpyxl
import xlwings as xw
import os
import copy

import openpyxl
import xlwings as xw
import os

def convert_excel(file_path, status_label):
    try:
        status_label.config(text="Processing...", fg="blue")

        # Step 1: Load workbook via openpyxl
        wb_openpyxl = openpyxl.load_workbook(file_path, data_only=False)

        converted_data = {}

        # Step 2: Process all sheets except "indicators"
        for sheet_name in wb_openpyxl.sheetnames:
            if sheet_name == "indicators":
                continue

            ws = wb_openpyxl[sheet_name]
            sheet_data = []

            for row in ws.iter_rows():
                row_data = []
                for cell in row:
                    val = cell.value
                    if val is None or (isinstance(val, str) and val.startswith('=')):
                        row_data.append(val)
                        continue
                    if '0%' in cell.number_format or '%' in cell.number_format:
                        row_data.append(val)
                        continue
                    if isinstance(val, (int, float)):
                        row_data.append(val / 1.95583)
                    else:
                        row_data.append(val)
                sheet_data.append(row_data)

            converted_data[sheet_name] = sheet_data

        # Step 3: Open original file in Excel with xlwings
        app = xw.App(visible=False)
        wb_xlw = app.books.open(file_path)

        for sheet in wb_xlw.sheets:
            if sheet.name == "indicators":
                # Process indicators in-place
                for row in sheet.used_range.rows:
                    for cell in row:
                        val = cell.value
                        if val is None or (isinstance(val, str) and val.startswith('=')):
                            continue
                        if cell.number_format and ('%' in cell.number_format or '0%' in cell.number_format):
                            continue
                        if isinstance(val, (int, float)):
                            cell.value = val / 1.95583
            else:
                # Bulk update non-indicators sheets
                if sheet.name in converted_data:
                    sheet.range("A1").value = converted_data[sheet.name]

        # Step 4: Save final version
        base = os.path.basename(file_path)
        name, ext = os.path.splitext(base)
        final_path = os.path.join(os.getcwd(), f"{name}_EUR{ext}")
        wb_xlw.save(final_path)
        wb_xlw.close()
        app.quit()

        status_label.config(text="Conversion complete", fg="green")

    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")


