# 4. Compare Two Arrays and Find Differences

import numpy as np

# Creating two arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([4, 5, 6, 7, 8])

# Finding elements in array1 that are not in array2
diff1 = np.setdiff1d(array1, array2)

# Finding elements in array2 that are not in array1
diff2 = np.setdiff1d(array2, array1)
print("Array 1:", array1)
print("Array 2:", array2)
print("Elements in array1 not in array2:", diff1)
print("Elements in array2 not in array1:", diff2)

# OUTPUT
# Array 1: [1 2 3 4 5]
# Array 2: [4 5 6 7 8]
# Elements in array1 not in array2: [1 2 3]   
# Elements in array2 not in array1: [6 7 8] 