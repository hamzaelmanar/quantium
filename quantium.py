import pandas as pd

# Read all sheets from the Excel file
excel_file = pd.ExcelFile('QVI_results.xlsx')

# Get all sheet names
sheet_names = excel_file.sheet_names

# Create a dictionary to store DataFrames for each sheet
dfs = {}

# Read each sheet into a separate DataFrame
for sheet in sheet_names:
    dfs[sheet] = pd.read_excel(excel_file, sheet_name=sheet)


