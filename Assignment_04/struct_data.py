# Explain Structured Data: NumPy’s Structured Array

import numpy as np

# Define the data type for each field
dtype = [('name', 'S10'), ('age', int), ('height', float)]

# Create data
data = [('John', 25, 1.75), ('Alice', 30, 1.65), ('Bob', 35, 1.85)]

# Create the structured array
arr = np.array(data, dtype=dtype)

# Find the average height of students older than 30
average_height = np.mean(arr[arr['age'] > 30]['height'])
print(average_height)
