# WAP Demonstrate Pandas with its Operations

import pandas as pd

# Reading a CSV file into a DataFrame
df = pd.read_csv("D:/Christ_Python/Pandas/data.csv")

# 1. Print the entire DataFrame
print(df)

# 2. Print the first 5 rows of the DataFrame (default)
print(df.head())

# 3. Print the last 5 rows of the DataFrame (default)
print(df.tail())

# 4. Print the shape of the DataFrame (rows, columns)
print(df.shape)

# 5. Print the total number of elements in the DataFrame (rows * columns)
print(df.size)

# 6. Print the column names of the DataFrame
print(df.columns)

# 7. Print the data types of each column
print(df.dtypes)

# 8. Print the underlying data as a NumPy array
print(df.values)

# 9. Print the index of the DataFrame (row labels)
print(df.index)
