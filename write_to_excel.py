from xlsxwriter import Workbook

def write_to_excel(workbook: Workbook, response: dict, ip_address: str) -> None:

    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold': True})

    col=0
        
    for key, values in response.items():

        worksheet.set_column(0, col, 25)
        worksheet.set_column(1, col, 25)
        worksheet.write(0, col, key, bold)
        worksheet.write(1, col, str(values))
        col+=1

    worksheet.set_column(0, col, 25)
    worksheet.set_column(1, col, 25)
    worksheet.write(0, col, "ip_address", bold)
    worksheet.write(1, col, ip_address)

