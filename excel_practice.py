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

def convert_excel(file_path, status_label):
    try:
        status_label.config(text="Processing...", fg="blue")

        # Load workbook with openpyxl
        wb = openpyxl.load_workbook(file_path)

        # Process all sheets except "indicators" using openpyxl
        for sheet_name in wb.sheetnames:
            if sheet_name == "indicators":
                continue
            ws = wb[sheet_name]
            for row in ws.iter_rows():
                for cell in row:
                    if cell.value is None or (isinstance(cell.value, str) and cell.value.startswith('=')):
                        continue
                    if '0%' in cell.number_format or '%' in cell.number_format:
                        continue
                    if isinstance(cell.value, (int, float)):
                        cell.value /= 1.95583
                        # Reapply formatting
                        cell.font = copy.copy(cell.font)
                        cell.fill = copy.copy(cell.fill)
                        cell.border = copy.copy(cell.border)
                        cell.alignment = copy.copy(cell.alignment)
                        cell.number_format = copy.copy(cell.number_format)
                        cell.protection = copy.copy(cell.protection)

        # Save the openpyxl-processed part to a temporary file
        base = os.path.basename(file_path)
        name, ext = os.path.splitext(base)
        temp_path = os.path.join(os.getcwd(), f"{name}_temp{ext}")
        wb.save(temp_path)

        # Reopen the saved file with xlwings to process "indicators" sheet
        app = xw.App(visible=False)
        wb_xlw = app.books.open(temp_path)

        try:
            sheet = wb_xlw.sheets['indicators']
        except Exception:
            sheet = None

        if sheet:
            for row in sheet.used_range.rows:
                for cell in row:
                    value = cell.value
                    if value is None or (isinstance(value, str) and value.startswith('=')):
                        continue
                    if cell.number_format and ('%' in cell.number_format or '0%' in cell.number_format):
                        continue
                    if isinstance(value, (int, float)):
                        cell.value = value / 1.95583

        # Save the final version
        final_path = os.path.join(os.getcwd(), f"{name}_EUR{ext}")
        wb_xlw.save(final_path)
        wb_xlw.close()
        app.quit()

        # Delete temp file if needed
        if os.path.exists(temp_path):
            os.remove(temp_path)

        status_label.config(text="Conversion complete", fg="green")

    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")
