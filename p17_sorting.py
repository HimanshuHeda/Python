import numpy as np

# Creating an array
# arr = np.array([1, 2, 3, 4, 5, 6])
arr = np.array(['B', 'C', 'D' , 'F', 'G'])

# Sorting the array 
sorted_arr = np.sort(arr)
print(sorted_arr)           # Output [1 2 3 5 6]

# In-Place sorting
arr.sort()
print(arr)                  # Output [1 2 3 5 6]




# array1 = np.array(['B', 'C', 'D' , 'F', 'G'])
# sorted_arr0 = array1[np.argsort(-array1)]
# print(sorted_arr0)