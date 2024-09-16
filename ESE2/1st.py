# 1. Write a program to count the number of elements in a list that are greater than a given threshold.

# Define the function count_greater_than which accepts two parameters:
# 'lst' which is the list of numbers, and 'threshold' which is the value we compare elements with.

def count_greater_than(lst, threshold):
# Initialize a counter to keep track of how many numbers are greater than the threshold.
    count = 0
# Use a for loop to iterate over each element in the list.
    for num in lst:
# Check if the current number is greater than the threshold.
        if num > threshold:
# If the condition is true, increment the counter by 1.
            count += 1
# Return the final count after checking all elements in the list.
    return count

# Define a sample list and a threshold value
sample_list = [10, 45, 23, 78, 5, 19, 89]
threshold_value = 30

# Call the function and store the result
result = count_greater_than(sample_list, threshold_value)

# Print the result which shows how many numbers are greater than the threshold
print("Number of elements greater than", threshold_value, "is:", result)






# Explanation:
# 1. def count_greater_than(lst, threshold):
# o This defines a function named count_greater_than. The function takes two
# arguments: lst (a list of numbers) and threshold (the threshold value we will
# compare the list elements to).

# 2. count = 0
# o This initializes a variable count to 0. It will be used to keep track of how many
# elements in the list are greater than the threshold.

# 3. for num in lst:
# o This starts a loop that iterates over each element (num) in the list lst.
# 4. if num &gt; threshold:
# o Inside the loop, it checks whether the current element (num) is greater than the
# threshold.
# 5. count += 1
# o If the condition (num &gt; threshold) is true, this line increments the count by 1.
# 6. return count

# o After the loop finishes iterating over all elements in the list, the function returns
# the final value of count (the total number of elements greater than the threshold).

# 7. sample_list = [10, 45, 23, 78, 5, 19, 89]
# o This defines a list of numbers (sample_list), which we will use to test the
# function.
# 8. threshold_value = 30
# o This sets a threshold value (threshold_value) that we will use for comparison.
# 9. result = count_greater_than(sample_list, threshold_value)
# o Here, we call the count_greater_than function, passing the sample list and
# threshold as arguments. The result (number of elements greater than the
# threshold) is stored in the variable result.

# 10. print(&quot;Number of elements greater than&quot;, threshold_value, &quot;is:&quot;, result)
# o Finally, this prints the result, showing how many elements in the list are greater
# than the threshold.


# Example Output:
# Number of elements greater than 30 is: 3
# In this case, the numbers greater than 30 in the list [10, 45, 23, 78, 5, 19, 89] are 45, 78, and 89,
# so the count is 3.