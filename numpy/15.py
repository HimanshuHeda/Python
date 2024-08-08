# 7. Transpose of a Matrix

import numpy as np

# Create a 2x3 NumPy matrix (2D array)
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Transpose the matrix
transpose_matrix = np.transpose(matrix)

# Print the result
print("Original matrix:")
print(matrix)
print("Transposed matrix:")
print(transpose_matrix)

# OUTPUT : 
# Original matrix:
# [[1 2 3]
#  [4 5 6]]
# Transposed matrix:
# [[1 4]
#  [2 5]
#  [3 6]]