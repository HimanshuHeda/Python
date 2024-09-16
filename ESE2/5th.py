# 5. WAP to Implement NumPy Features?
#   1. Create a 3x3 matrix using NumPy.
#   2. Extract the diagonal elements of the matrix.
#   3. Find the maximum value in each row of the matrix.

# Solution:

import numpy as np

# Create a 3x3 matrix
matrix = np.array([[5, 2, 8],
[3, 7, 4],
[6, 1, 9]])

# Extract the diagonal elements
diagonal_elements = np.diag(matrix)
print("Diagonal elements:", diagonal_elements) # Output: Diagonal elements: [5 7 9]

# Find the maximum value in each row
max_in_rows = np.max(matrix, axis=1)
print("Maximum value in each row:", max_in_rows) # Output: Maximum value in each row: [8 7 9]