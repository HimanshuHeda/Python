# 2. Logical operations on boolean arrays:

import numpy as np # Import the NumPy library
bool_array1 = np.array([True, False, True]) # Create the first boolean array
bool_array2 = np.array([False, True, True]) # Create the second boolean array

print("Boolean array 1:", bool_array1) # Print the first boolean array
print("Boolean array 2:", bool_array2) # Print the second boolean array

# Logical AND operation
and_result = np.logical_and(bool_array1, bool_array2) # Perform  the logical AND operation
print("Logical AND result:", and_result) # Print the result of logical  AND operation

# Logical OR operation
or_result = np.logical_or(bool_array1, bool_array2) # Perform logical OR operation
print("Logical OR result:", or_result) # Print the result of logical OR