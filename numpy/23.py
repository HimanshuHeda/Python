# 5. Compare Two Arrays and Find Unique Elements

import numpy as np

# Creating two arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([4, 5, 6, 7, 8])

# Finding unique elements in both arrays
unique_elements = np.setxor1d(array1, array2)
print("Array 1:", array1)
print("Array 2:", array2)
print("Unique elements:", unique_elements)

# OUTPUT : 
# Array 1: [1 2 3 4 5]
# Array 2: [4 5 6 7 8]
# Unique elements: [1 2 3 6 7 8]