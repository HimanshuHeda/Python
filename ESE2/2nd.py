# 2. Write a Python program to create a DataFrame with some missing values. Use Pandas
# functions to fill the missing values with the mean, and then drop any remaining rows with missing data.

import pandas as pd
import numpy as np

# Step 1: Create a DataFrame with missing values
data = {
'A': [1, 2, np.nan, 4],
'B': [5, np.nan, np.nan, 8],
'C': [10, 11, 12, np.nan]
}

df = pd.DataFrame(data)
print("Original DataFrame with Missing Values:")
print(df)

# Step 2: Fill missing values with the mean of each column
df_filled = df.fillna(df.mean())
print("\nDataFrame after Filling Missing Values with Column Mean:")
print(df_filled)

# Step 3: Drop any remaining rows with missing values
df_cleaned = df_filled.dropna()
print("\nDataFrame after Dropping Remaining Missing Values:")
print(df_cleaned)









# Explanation:
# 1. import pandas as pd and import numpy as np
# o We import the pandas library as pd to create and manipulate the DataFrame, and
# numpy as np to work with missing values (np.nan).

# 2. Creating the DataFrame:
# data = {
# 'A': [1, 2, np.nan, 4],
# 'B': [5, np.nan, np.nan, 8],
# 'C': [10, 11, 12, np.nan]
# }
# df = pd.DataFrame(data)
# o We create a dictionary called data where the keys are the column names ('A', 'B',
# 'C') and the values are lists. Some of the values are np.nan, representing missing
# data.
# o We use pd.DataFrame(data) to create a DataFrame called df.
# 3. Printing the Original DataFrame:
# print("Original DataFrame with Missing Values:")
# print(df)
# o We print the original DataFrame to show the missing values.
# 4. Filling Missing Values with Column Means:
# df_filled = df.fillna(df.mean())
# o The df.mean() function computes the mean of each column, ignoring np.nan
# values.
# o df.fillna(df.mean()) replaces the np.nan values in the DataFrame with the mean of
# their respective columns.
# o We store the result in a new DataFrame called df_filled.
# 5. Printing the DataFrame After Filling Missing Values:
# print("\nDataFrame after Filling Missing Values with Column Mean:")
# print(df_filled)
# o We print the updated DataFrame to show the filled values.
# 6. Dropping Any Remaining Missing Values:
# df_cleaned = df_filled.dropna()

# o The dropna() function removes any rows that still contain missing values. After
# filling the NaN values with the mean, this will remove any remaining rows with
# missing data (if any still exist).
# o We store the cleaned DataFrame in df_cleaned.
# 7. Printing the Final Cleaned DataFrame:
# print("\nDataFrame after Dropping Remaining Missing Values:")
# print(df_cleaned)
# o We print the cleaned DataFrame to show the final result with no missing data.




# Output:
# Original DataFrame with Missing Values:
# A B C
# 0 1.0 5.0 10.0
# 1 2.0 NaN 11.0
# 2 NaN NaN 12.0
# 3 4.0 8.0 NaN
# DataFrame after Filling Missing Values with Column Mean:
# A B C
# 0 1.0 5.0 10.0
# 1 2.0 6.5 11.0
# 2 2.333333 6.5 12.0
# 3 4.0 8.0 11.0
# DataFrame after Dropping Remaining Missing Values:
# A B C
# 0 1.0 5.0 10.0
# 1 2.0 6.5 11.0
# 2 2.333333 6.5 12.0
# 3 4.0 8.0 11.0
# The missing values in columns A, B, and C are filled with the column means. Any rows that still
# had missing values would have been dropped, but in this case, no rows remain with missing data
# after the fill operation.