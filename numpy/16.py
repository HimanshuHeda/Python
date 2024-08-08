# 8. Inverse of a Matrix

import numpy as np

# Create a 2x2 NumPy matrix (2D array)
matrix = np.array([[1, 2], [3, 4]])

# Calculate the inverse of the matrix
inverse_matrix = np.linalg.inv(matrix)

# Print the result
print("Original matrix:")
print(matrix)
print("Inverse matrix:")
print(inverse_matrix)

# OUTPUT
# Original matrix:
# [[1 2]
#  [3 4]]
# Inverse matrix:
# [[-2.   1. ]
#  [ 1.5 -0.5]]