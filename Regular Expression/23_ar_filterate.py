# 1. Filter elements greater than a given value:

import numpy as np # Import the NumPy library

array = np.array([10, 15, 20, 25, 30]) # Create a NumPy array
print("Original array:", array) # Print the original array

mask = array > 20 # Create a mask for elements greater than 20
print("Mask for elements > 20:", mask) # Print the mask

filtered = array[mask] # Use the mask to filter the array
print("Filtered array:", filtered) # Print the filtered array
