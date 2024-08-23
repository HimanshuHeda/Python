# WAP for Creating and Manipulating Arrays
import numpy as np

def elementwise_comparison_numpy(arr1, arr2):
    # Convert lists to NumPy arrays (if they aren't already)
    np_arr1 = np.array(arr1)
    np_arr2 = np.array(arr2)
    
    # Perform element-wise comparison using NumPy
    comparison_results = np_arr1 == np_arr2
    
    return comparison_results

# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 0, 4, 5]

result = elementwise_comparison_numpy(arr1, arr2)
print("Element-wise comparison results (NumPy):", result)