# WAP USING FANCY INDEXING FOR SORTING NUMPY ARRAY IN RANDOM ORDER ARRAY [1,2,3,4,5,6,7,8,9,10,11,12,13]

import numpy as np

# Initialize the array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# Generate a random permutation of indices
random_indices = np.random.permutation(len(array))

# Use fancy indexing to reorder the array
random_array = array[random_indices]

# Print the original array and the randomly ordered array
print("Original array:")
print(array)

print("Randomly ordered array:")
print(random_array)
