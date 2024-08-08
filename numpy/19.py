# 1. Compare Two Arrays for Equality

import numpy as np

# Creating two arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([1, 2, 3, 4, 5])

# Check if both arrays are equal
are_equal = np.array_equal(array1, array2)
print("Array 1:", array1)
print("Array 2:", array2)
print("Are both arrays equal?", are_equal)

# OUTPUT :
# Array 1: [1 2 3 4 5]
# Array 2: [1 2 3 4 5]
# Are both arrays equal? True