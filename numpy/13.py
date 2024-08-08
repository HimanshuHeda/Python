# 5. Multiplying Two Arrays Element-wise

import numpy as np

# Create two NumPy arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])

# Multiply the two arrays element-wise
product_array = np.multiply(array1, array2)

# Print the result
print(f"Product of arrays: {product_array}")

# OUTPUT
# Product of arrays: [ 10  40  90 160 250]