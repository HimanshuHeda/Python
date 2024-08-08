# 9. Determinant of a Matrix

import numpy as np

# Create a 2x2 NumPy matrix (2D array)
matrix = np.array([[1, 2], [3, 4]])

# Calculate the determinant of the matrix
determinant = np.linalg.det(matrix)

# Print the result
print("Original matrix:")
print(matrix)
print(f"Determinant of the matrix: {determinant}")

# OUTPUT :
# Original matrix:
# [[1 2]
#  [3 4]]
# Determinant of the matrix: -2.0000000000000004