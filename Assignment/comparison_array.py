import numpy as np

def element_wise_comparison(arr1, arr2):
    equal = np.equal(arr1, arr2)
    greater = np.greater(arr1, arr2)
    less = np.less(arr1, arr2)
    
    return equal, greater, less

def main():
    # Example arrays
    arr1 = np.array([10, 20, 50, 80, 190])
    arr2 = np.array([10, 29, 30, 25, 60])
    
    # Perform element-wise comparison
    equal, greater, less = element_wise_comparison(arr1, arr2)
    
    print("Element-wise equality:", equal)
    print("Element-wise greater than:", greater)
    print("Element-wise less than:", less)

if __name__ == "__main__":
    main()
