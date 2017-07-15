#!usr/bin/python
import xlrd
from collections import OrderedDict
import simplejson as json
 
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('Test_Properity.xlsx')
sh = wb.sheet_by_index(0)
 
# List to hold dictionaries
fields_list = []
 
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    fields = OrderedDict()
    row_values = sh.row_values(rownum)# row vlaues 
    column_amount = len(row_values)
    print column_amount
    for row_amount in range(1,column_amount):
        fields[row_values[row_amount]] = row_values[row_amount]
    fields_list.append(fields)
 
# Serialize the list of dicts to JSON
j = json.dumps(fields_list)
 
# Write to file
with open('data.json', 'w') as f:
    f.write(j)
	