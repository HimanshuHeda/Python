#  WAP to perform six commonly used commands in pandas dataframe 
import pandas as pd

std_data = [
    (1, 'Himanshu', 20, 'Male', 'Rajasthan'),
    (2, 'Anugrah', 21, 'Male', 'Rajasthan'),
    (3, 'Aaron', 22, 'Male', 'Delhi'),
    (4, 'Vatan', 32, 'Male', 'Delhi'),
    (5, 'Saksham', 25, 'Male', 'Delhi')
]
df = pd.DataFrame(std_data, columns=['stud_id', 'name', 'age', 'gender','address'])
print(df)


# df = pd.read_csv("D:/Christ_Python/Pandas/data.csv")
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.size)
print(df.columns)
print(df.dtypes)
print(df.values)
print(df.index)
