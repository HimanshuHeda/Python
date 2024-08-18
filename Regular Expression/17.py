# 1. Boolean Array Creation:

import numpy as np # Import the NumPy library

array = np.array([1, 2, 5, 4]) # Create a NumPy array

bool_array = np.array([True, False, True, True]) # Create a boolean array with the same length
print(bool_array) # Print the boolean array

# 2. Using Boolean Arrays:
result = np.where(bool_array, array, -1) # Replace True values with array elements and False values with -1
print(result) # Print the resulting array
