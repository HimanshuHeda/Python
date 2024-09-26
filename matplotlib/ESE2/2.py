# Write a dataframe with some missing values.Use Pandas functions to fill the missing values with the mean, 
# and then drop any remaining rows with missing data.

import pandas as pd
import numpy as np

# Create a DataFrame with some missing values
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, np.nan],
    'D': [1, np.nan, np.nan, 4, 5]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Fill missing values with the mean of the respective columns
df_filled = df.fillna(df.mean())

# To Print the DataFrames after missing values
print("\nDataFrame after filling missing values with mean:")
print(df_filled)

# Drop any remaining rows with missing data
df_cleaned = df_filled.dropna()

print("\nDataFrame after dropping remaining rows with missing data:")
print(df_cleaned)
