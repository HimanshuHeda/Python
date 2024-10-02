# WAP Maximum and Minimum of a List

import numpy as np  
# Importing the NumPy library for numerical operations

# List of numbers to find the maximum and minimum values from
numbers = [12, 45, 17, 23, 56, 80, 34]

# Using NumPy's max function to find the maximum value in the list
max_value = np.max(numbers)

# Using NumPy's min function to find the minimum value in the list
min_value = np.min(numbers)

# Printing the maximum and minimum values
print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")
