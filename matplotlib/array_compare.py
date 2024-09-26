#  Compare 2 array 

import numpy as np

# Define two arrays
array1 = np.array([1, 2, 3, 4])
array2 = np.array([1, 2, 3, 4])

# Compare arrays for equality
are_equal = np.array_equal(array1, array2)

# Output result
if are_equal:
    print("The arrays are equal.")
else:
    print("The arrays are not equal.")
