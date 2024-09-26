import seaborn as sns
# import pandas as pd
import matplotlib.pyplot as plt 


df = sns.load_dataset('iris')
sns.pairplot(df)
plt.show()