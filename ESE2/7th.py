# 7. Create a DataFrame of students' scores, write a Python program to filter out the students
# who scored above a certain threshold in a specific subject.

import pandas as pd
# Step 1: Create a DataFrame with students' scores
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 78, 92, 88, 76],
    'English': [90, 82, 87, 91, 84],
    'Science': [88, 79, 85, 93, 80]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Step 2: Define the threshold for the specific subject
threshold = 85
subject = 'Math'

# Step 3: Filter students who scored above the threshold in the specific subject
filtered_df = df[df[subject] > threshold]
print("\nFiltered DataFrame (Students who scored above", threshold, "in", subject + "):")

print(filtered_df)











# Explanation:
# 1. Import pandas:
# import pandas as pd
# o We import the pandas library, which provides data manipulation tools and data
# structures.
# 2. Create the DataFrame:
# data = {
# 'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
# 'Math': [85, 78, 92, 88, 76],
# 'English': [90, 82, 87, 91, 84],
# 'Science': [88, 79, 85, 93, 80]
# }
# df = pd.DataFrame(data)
# o We create a dictionary named data where keys are column names ('Student',
# 'Math', 'English', 'Science') and values are lists of scores.
# o We convert this dictionary into a DataFrame using pd.DataFrame(data).
# 3. Print the Original DataFrame:
# print("Original DataFrame:")
# print(df)
# o This prints the original DataFrame showing all students' scores in different
# subjects.

# 4. Define the Threshold and Subject:
# threshold = 85
# subject = 'Math'
# o We set the threshold score (85) and specify the subject ('Math') for filtering.
# 5. Filter the DataFrame:
# filtered_df = df[df[subject] &gt; threshold]
# o We filter the DataFrame to include only the rows where the score in the specified
# subject ('Math') is greater than the threshold (85).
# o This is done using boolean indexing, df[subject] &gt; threshold, which creates a
# boolean series used to filter the DataFrame.

# 6. Print the Filtered DataFrame:

# print("\nFiltered DataFrame (Students who scored above", threshold, "in", subject + "):")
# print(filtered_df)
# o This prints the filtered DataFrame showing only the students who scored above
# the specified threshold in the chosen subject.

# Example Output:
# Original DataFrame:
# Student Math English Science
# 0 Alice 85 90 88
# 1 Bob 78 82 79
# 2 Charlie 92 87 85
# 3 David 88 91 93
# 4 Eva 76 84 80
# Filtered DataFrame (Students who scored above 85 in Math):
# Student Math English Science
# 2 Charlie 92 87 85
# 3 David 88 91 93
# In this example, Charlie and David are the students who scored above 85 in the Math subject.