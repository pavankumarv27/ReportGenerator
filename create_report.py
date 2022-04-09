from openpyxl import load_workbook


def write_excel(r, c, v):
    v = str(v)
    wb = load_workbook('template.xlsx')
    sh = wb.active
    cell = sh.cell(row=r, column=c)
    cell.value = v
    print(f'chosen row = {r}, col = {c}')
    print('value added to excel:', cell.value)
    wb.save('FEB_2022.xlsx')
    #input("Save complete")
