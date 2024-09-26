import numpy as np

# Creating an array
arr = np.array([10, 20, 30, 40, 50])

# Using fancy indexing with an array of indices
indices = np.array([0, 2, 4])
selected_elements = arr[indices]
print(selected_elements)  # Output: [10 30 50]

# Using fancy indexing with a boolean mask
mask = np.array([True, False, True, False, True])
selected_elements_mask = arr[mask]
print(selected_elements_mask)  # Output: [10 30 50]

