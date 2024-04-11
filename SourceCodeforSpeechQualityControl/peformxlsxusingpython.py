import pandas as pd

# pip install openpyxl
# Read the Excel file
df = pd.read_excel('Kannada_Metadata_16012023_V2.xlsx')

#print(df.to_string())
print('I am here1')
print(df.head)
print(df.head(2))
print(df.tail())

enter_key = input('Press Enter Key\n')

df2=pd.read_excel(open('Kannada_Metadata_16012023_V2.xlsx', 'rb'),sheet_name='SVG_Students_Details')
#df2=pd.read_excel(open('Kannada_Metadata_16012023_V2.xlsx', 'rb'),sheet_name='SVG_Students_Details')




import os
linuxcmd = 'clear'
os.system(linuxcmd)

print('I am here2')
print(df2)
print('I am here3')
print(df2.sort_values(by='Name'))
print('I am here4')
print(df2.columns)

df2["Total"]=df2["M1"]+df2["M2"]+df2["M3"]
print(df2)

df2.to_excel('results.xlsx', index=False)
#df2.to_excel('results.xlsx', index=True)








