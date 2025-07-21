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
            for row in sheet.used_range.rows:
                for cell in row:
                    value = cell.value
                    if value is None or (isinstance(value, str) and value.startswith('=')):
                        continue
                    if cell.number_format and ('%' in cell.number_format or '0%' in cell.number_format):
                        continue
                    if isinstance(value, (int, float)):
                        cell.value = value / 1.95583

        base = os.path.basename(file_path)
        name, ext = os.path.splitext(base)
        output_path = os.path.join(os.getcwd(), f"{name}_EUR{ext}")
        wb.save(output_path)
        wb.close()
        app.quit()
        status_label.config(text="Conversion complete", fg="green")

    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")