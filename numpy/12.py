# 4. Adding Two Arrays Element-wise

import numpy as np

# Create two NumPy arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])

# Add the two arrays element-wise
sum_array = np.add(array1, array2)

# Print the result
print(f"Sum of arrays: {sum_array}")

# OUTPUT :
# Sum of arrays: [11 22 33 44 55]