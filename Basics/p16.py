# WAP TO FIND MULTIPLE ELEMENTS USING NUMPY FANCY INDEXING ARRAY=[1,2,3,4,5,6,7,8] ELEMENTS TO BE SELECTED =[1,2,5,7]
import numpy as np

# Creating an array
arr = np.array([1,2,3,4,5,6,7,8])

# Using fancy indexing with an array of indices
indices = np.array([1,2,5,7])
selected_elements = arr[indices]
print(selected_elements)  # Output: [2, 3, 6, 8]
