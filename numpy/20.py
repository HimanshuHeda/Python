# 2. Element-wise Comparison of Two Arrays

import numpy as np

# Creating two arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([1, 2, 0, 4, 5])

# Element-wise comparison
comparison = np.equal(array1, array2)
print("Array 1:", array1)
print("Array 2:", array2)
print("Element-wise comparison:", comparison)

# # OUTPUT :
# Array 1: [1 2 3 4 5]
# Array 2: [1 2 0 4 5]
# Element-wise comparison: [ True  True False  True  True]