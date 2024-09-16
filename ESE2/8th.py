# 8. Write a Python program to create a pivot table from a given DataFrame that summarizes
# data based on two categorical columns, calculating the sum of another numerical column.

import pandas as pd

# Step 1: Create a DataFrame with sample data
data = {
    'Department': ['HR', 'IT', 'IT', 'HR', 'Sales', 'Sales', 'IT'],
    'Region': ['North', 'South', 'North', 'West', 'North', 'South', 'West'],
    'Sales': [1500, 2200, 1800, 1600, 2100, 2400, 2000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Step 2: Create a pivot table
pivot_table = pd.pivot_table(df, values='Sales', index='Department', columns='Region',
aggfunc='sum', fill_value=0)

print("\nPivot Table Summarizing Sales:")
print(pivot_table)
















# Explanation:
# 1. Import pandas:
# import pandas as pd
# o We import the pandas library for data manipulation and analysis.
# 2. Create the DataFrame:
# data = {
# 'Department': ['HR', 'IT', 'IT', 'HR', 'Sales', 'Sales', 'IT'],
# 'Region': ['North', 'South', 'North', 'West', 'North', 'South', 'West'],
# 'Sales': [1500, 2200, 1800, 1600, 2100, 2400, 2000]
# }
# df = pd.DataFrame(data)
# o We create a dictionary named data containing three columns: 'Department',
# 'Region', and 'Sales'.
# o We convert this dictionary into a DataFrame using pd.DataFrame(data).
# 3. Print the Original DataFrame:
# print("Original DataFrame:")
# print(df)
# o This prints the original DataFrame to show the raw data.
# 4. Create the Pivot Table:
# pivot_table = pd.pivot_table(df, values='Sales', index='Department', columns='Region',
# aggfunc='sum', fill_value=0)
# o pd.pivot_table() creates a pivot table from the DataFrame.
#  values='Sales' specifies that the Sales column will be used for aggregation.
#  index='Department' indicates that the rows of the pivot table will be
# categorized by Department.
#  columns='Region' indicates that the columns of the pivot table will be
# categorized by Region.
#  aggfunc='sum' specifies that the aggregation function used will be the sum
# of the Sales values.
#  fill_value=0 replaces any missing values with 0 in the resulting pivot
# table.
# 5. Print the Pivot Table:
# print("\nPivot Table Summarizing Sales:")
# print(pivot_table)

# o This prints the resulting pivot table, which summarizes the total sales for each
# department and region combination.

# Example Output:
# Original DataFrame:
# Department Region Sales
# 0 HR North 1500
# 1 IT South 2200
# 2 IT North 1800
# 3 HR West 1600
# 4 Sales North 2100
# 5 Sales South 2400
# 6 IT West 2000
# Pivot Table Summarizing Sales:
# Region North South West
# Department
# HR 1500 0 1600
# IT 1800 2200 2000
# Sales 2100 2400 0
# In this output:
#  The pivot table shows the total sales for each combination of Department and Region.
#  For example, the total sales for HR in the North region is 1500, and for Sales in the South
# region is 2400.

# This program helps to summarize and analyze data effectively by aggregating values based on
# different categorical dimensions.