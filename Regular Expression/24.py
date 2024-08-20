# 2. Replace elements based on a condition:

import numpy as np # Import the NumPy library

array = np.array([1, 2, 3, 4, 5]) # Create a NumPy array
print("Original array:", array) # Print the original array

bool_array = array % 2 == 0 # Create a boolean array for even elements
print("Boolean array for even elements:", bool_array) # Print the boolean array

result = np.where(bool_array, array, -1) # Replace even elements with themselves and odd elements with -1
print("Resulting array:", result) # Print the resulting array