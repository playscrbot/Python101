import openpyxl

wb = openpyxl.load_workbook("employees.xlsx")
sheet = wb.active

print(sheet["A1"].value)