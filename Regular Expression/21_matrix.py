# 1. Create a 3x3 matrix and perform basic operations:

import numpy as np # Import the NumPy library
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Create a 3x3
matrix
print("Original matrix:\n", matrix) # Print the original matrix
# Element-wise addition
result_add = matrix + 10 # Add 10 to each element
print("Matrix after adding 10:\n", result_add) # Print the resulting
matrix
# Element-wise multiplication
result_mul = matrix * 2 # Multiply each element by 2
print("Matrix after multiplying by 2:\n", result_mul) # Print the resulting matrix
