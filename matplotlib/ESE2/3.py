# Create  a DataFrame of students scores write a python Program to filter out the students who scored above 
# a certain threshold in a specfic object

import pandas as pd
# Create a DataFrame of students' scores
data = {
    'Name': ['Himanshu', 'Alok', 'Sangram', 'Saksham', 'Anugrah'],
    'Math': [85, 90, 88, 92, 88],
    'Science': [90, 84, 72, 88, 86],
    'English': [78, 93, 75, 90, 89]
}
df = pd.DataFrame(data)
# Threshold and subject
threshold = 90
subject = 'English'
# Filter out the students who scored above the threshold in the specific subject
filtered_df = df[df[subject] > threshold]
# Print the original and filtered DataFrames
print("Original DataFrame:")
print(df)
print("\nFiltered DataFrame ({} > {}):".format(subject, threshold))
print(filtered_df)