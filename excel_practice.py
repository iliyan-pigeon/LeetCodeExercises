def convert_excel(file_path, status_label):
    try:
        status_label.config(text="Processing...", fg="blue")

        wb = openpyxl.load_workbook(file_path)

        for sheet in wb.sheetnames:
            ws = wb[sheet]
            for row in ws.iter_rows():
                for cell in row:
                    if sheet == "indicators":
                        print(cell.value)
                    if cell.value is None or (isinstance(cell.value, str) and cell.value.startswith('=')):
                        continue
                    if '0%' in cell.number_format or '%' in cell.number_format:
                        continue
                    if isinstance(cell.value, (int, float)):
                        cell.value /= 1.95583

                        # Reapply the formatting after conversion
                        cell.font = copy.copy(cell.font)
                        cell.fill = copy.copy(cell.fill)
                        cell.border = copy.copy(cell.border)
                        cell.alignment = copy.copy(cell.alignment)
                        cell.number_format = copy.copy(cell.number_format)
                        cell.protection = copy.copy(cell.protection)
                        cell.flags = copy.copy(cell.flags)

        base = os.path.basename(file_path)
        name, ext = os.path.splitext(base)
        output_path = os.path.join(os.getcwd(), f"{name}_EUR{ext}")
        wb.save(output_path)
