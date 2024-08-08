# Program 2: Basic Operations on Arrays

import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Addition of arrays
addition = arr1 + arr2
print("Array Addition:")
print(addition)

# Element-wise multiplication
multiplication = arr1 * arr2
print("Array Multiplication:")
print(multiplication)

# Dot product
dot_product = np.dot(arr1, arr2)
print("Dot Product:")
print(dot_product)