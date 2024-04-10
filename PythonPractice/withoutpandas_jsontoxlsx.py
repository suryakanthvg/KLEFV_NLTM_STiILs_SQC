# Without Using Pandas Library
import xlwt
import json

# Load the JSON file
with open('samplejsonfile_2.json') as f:
    data = json.load(f)

# Create an Excel workbook
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("univerinfo")

# Write the JSON data to the Excel sheet
for row, item in enumerate(data):
    for col, value in enumerate(item.values()):
        sheet.write(row, col, value)

# Save the Excel workbook
workbook.save("universityinfo.xlsx")        



