# WAP to count the number of True values in a boolean array:

import numpy as np

# Create a boolean array
bool_array = np.array([True, False, True, False, True, False, True, False])

# Count the number of True values in the boolean array
true_count = np.sum(bool_array)

# Print the result
print("Number of True values in the array:", true_count)



# WAP to count the number of False values in a boolean array:

import numpy as np

# Create a boolean array
bool_array = np.array([True, False, True, False, True, False, True, False])

# Count the number of True values in the boolean array
false_count = np.sum(bool_array)

# Print the result
print("Number of True values in the array:", false_count)
