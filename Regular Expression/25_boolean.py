# 1. Count the number of True values in a boolean array:

import numpy as np # Import the NumPy library

bool_array = np.array([True, False, True, True, False]) # Create a boolean array

print("Boolean array:", bool_array) # Print the boolean array
true_count = np.sum(bool_array) # Count the number of True values

print("Number of True values:", true_count) # Print the count of True values
