# 6. WAP to Demonstrate Pandas with its Operations?
#   1. Create a DataFrame from a dictionary with student names, ages, and grades.
#   2. Calculate the average age of students.
#   3. Sort the DataFrame based on grades in descending order.

# Solution:

import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
'Age': [20, 22, 21, 23],
'Grade': [85, 90, 78, 92]}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Calculate the average age of students
average_age = df['Age'].mean()
print("\nAverage Age:", average_age) # Output: Average Age: 21.5

# Sort the DataFrame based on grades in descending order
sorted_df = df.sort_values(by='Grade', ascending=False)
print("\nDataFrame sorted by Grade:")
print(sorted_df)