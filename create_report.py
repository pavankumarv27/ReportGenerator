from openpyxl import load_workbook


def write_excel(r, c, v):
    v = str(v)
    wb = load_workbook('FEB_2022.xlsx')
    sh = wb.active
    cell = sh.cell(row=r, column=c)
    cell.value = v
    print('value added to excel:', cell.value)
    wb.save('FEB_2022.xlsx')
