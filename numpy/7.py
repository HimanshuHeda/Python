# 4. Count of Elements Greater Than a Threshold
# This program counts the number of elements in a list that are greater than a specified threshold.

# Program to count the number of elements greater than a threshold

# Define the list of numbers
numbers = [10, 20, 30, 40, 50]

# Define the threshold
threshold = 25

# Use list comprehension to filter elements greater than the threshold
greater_than_threshold = [num for num in numbers if num > threshold]

# Count the elements
count = len(greater_than_threshold)

# Print the result
print(f"The number of elements greater than {threshold} is: {count}")


# Output: The number of elements greater than 25 is: 3