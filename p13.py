import numpy as np

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Create various masks based on conditions
mask = array > 3         # Elements greater than 3
mask1 = array < 3        # Elements less than 3
mask2 = array == 3       # Elements equal to 3 (corrected comparison)
mask3 = array <= 3       # Elements less than or equal to 3
mask4 = array >= 3       # Elements greater than or equal to 3
mask5 = array == 3       # Elements equal to 3 (same as mask2, for clarity)
mask6 = array != 3       # Elements not equal to 3

# Print all masks
print("Mask (array > 3):", mask)
print("Mask (array < 3):", mask1)
print("Mask (array == 3):", mask2)
print("Mask (array <= 3):", mask3)
print("Mask (array >= 3):", mask4)
print("Mask (array == 3):", mask5)
print("Mask (array != 3):", mask6)

# Use the mask to filter the array
filtered = array[mask]
print("Filtered array (array > 3):", filtered)

# Create another array
Array = np.array([1, 0, 1, 0, 1, 0, 1, 0])

# Create a boolean array
bool_array = np.array([True, False, True, False, True, False, True, False])
# bool_array = np.array([5, None, 1.25, -10, 0,'A'])

print("Boolean array:", bool_array)

# Filter the array using the boolean array
filtered_array = Array[bool_array]
print("Filtered Array using boolean array:", filtered_array)
