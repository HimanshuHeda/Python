# WAP Matrix Operations

import numpy as np

# Creating matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix are
print("First Matrix is :")
print(matrix1)
print("2nd Matrix is :")
print(matrix2)

# Matrix multiplication
matrix_product = np.matmul(matrix1, matrix2)
print("Matrix Multiplication:")
print(matrix_product)

# Transpose of a matrix
transpose_matrix1 = np.transpose(matrix1)
print("Transpose of Matrix1:")
print(transpose_matrix1)

transpose_matrix2 = np.transpose(matrix2)
print("Transpose of Matrix2:")
print(transpose_matrix2)