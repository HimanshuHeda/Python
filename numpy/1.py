# Program 1: Creating and Manipulating Arrays

import numpy as np

# Creating a NumPy array from a list
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:")
print(arr)

# Accessing elements of the array
print("Accessing Elements:")
print("First element:", arr[0])
print("Last element:", arr[-1])

# Slicing the array
print("Slicing the Array:")
print("Elements from index 1 to 3:", arr[1:4])