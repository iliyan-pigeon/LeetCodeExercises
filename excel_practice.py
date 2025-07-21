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