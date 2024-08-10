# Creating 3x3 matrices using multiple operations 

# Import the numpy library
import numpy as np

# Creating 3x3 matrices
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Matrix sum
sum_array = np.add(matrix1, matrix2)
print("Sum of Matrix:")
print(sum_array)

# Matrix subtraction
sub_array = np.subtract(matrix1, matrix2)
print("Matrix Subtract:")
print(sub_array)

# Matrix multiplication
matrix_product = np.matmul(matrix1, matrix2)
print("Matrix Multiplication:")
print(matrix_product)

# Transpose of a matrix
transpose_matrix1 = np.transpose(matrix1)
print("Transpose of Matrix1:")
print(transpose_matrix1)
