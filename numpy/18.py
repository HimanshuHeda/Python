# 10. Element-wise Comparison of Two Arrays

import numpy as np

# Create two NumPy arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])

# Compare the two arrays element-wise
comparison = np.equal(array1, array2)

# Print the result
print("Element-wise comparison:")
print(comparison)

# OUTPUT 
# Element-wise comparison:
# [False False  True False False]