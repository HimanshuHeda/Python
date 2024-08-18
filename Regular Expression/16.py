# 2. Using a Mask:

import numpy as np # Import the NumPy library
array = np.array([1,2,5,4]) # Create a NumPy array
mask = array > 2 # Create a mask for elements greater than 2
print(mask) # Print the mask
filtered = array[mask] # Use the mask to filter the array
print(filtered) # Print the filtered array
