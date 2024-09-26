import numpy as np              # Import the NumPy library

array = np.array([1,2,3,4,5])   # Create a NumPy array 
array1 = np.array([1,2,3,4,5])   # Create a NumPy array 
array3 = np.array([11, 33, 45, 5, 56, 34, 84, 92, 100])

print(array)                    # Print the array 

result = array + 10             # Add 10 to each element of the array
print(result)                   # Print the resulting array

result = array + 5.5            # Add 5.5 to each element of the array
print(result)                   # Print the resulting array

result = array1 - 5             # Add 5 to each element of the array
print(result)                   # Print the resulting array

total = np.sum(array)           # Compute the sum of the array elements
print(total)                    # Print the total array

mean_value = np.mean(array3)    # Compute the mean of the array elements 
print(mean_value)               # Print the mean 

max_value = np.max(array3)       # Compute the maximum value in the array
print(max_value)                # Print the maximum value


# WAp Compute the mean of the array elements
# WAP to compute the maximum value in the array.. change the value of elements from double digit to triple digit

# explain in detail numpy .... definition in 5 mark que
# Create an array using numpy and perform addition of any integers value higher then 6.6 
# Create an array and perform sub of any integer value higher then 17.9
# array = [22,34,26,25,24, or any no. higher than 17.9