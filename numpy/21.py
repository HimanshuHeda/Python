# 3. Find Common Elements Between Two Arrays

import numpy as np

# Creating two arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([4, 5, 6, 7, 8])

# Finding common elements
common_elements = np.intersect1d(array1, array2)
print("Array 1:", array1)
print("Array 2:", array2)
print("Common elements:", common_elements)

# OUTPUT : 
# Array 1: [1 2 3 4 5]
# Array 2: [4 5 6 7 8]
# Common elements: [4 5]