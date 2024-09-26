# WAP USING FANCY INDEXING FOR SORTING NUMPY ARRAY array can be of your choice 

import numpy as np

# create a numpy array
array1 = np.array([1, 2, 53, 4, 33, 26, 17, 58])

# select elements at index 1, 2, 5, 7
select_elements = array1[[1, 2, 5, 7]]

print(select_elements)

# Output: [2 53 26 58]