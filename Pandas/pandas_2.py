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

