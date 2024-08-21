import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# Select data using label-based indexing 
print(df.loc[0, 'A'])       # Output :  1
print(df.iloc[0, 1])        # Output :  4

#  df is a user defined