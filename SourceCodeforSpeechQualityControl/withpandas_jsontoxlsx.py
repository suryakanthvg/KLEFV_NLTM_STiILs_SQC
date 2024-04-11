# With Using Pandas Library

import pandas as pd
import json

# Load the JSON file
with open('samplejsonfile_2.json') as f:
    data = json.load(f)

# Convert the JSON data to a Pandas DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('uinverinfo.xlsx', index=False)

