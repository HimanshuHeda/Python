# 5. Product of a List
# This program calculates the product of all elements in a list.

# Program to calculate the product of all elements in a list

# Import the reduce function from the functools module
from functools import reduce

# Define the list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the product using the reduce() function and a lambda function
product = reduce(lambda x, y: x * y, numbers)

# Print the result
print(f"The product of the list is: {product}")


# Output: The product of the list is: 120