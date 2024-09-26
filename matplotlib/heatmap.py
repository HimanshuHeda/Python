import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 

data = np.random.rand(10, 10)
sns.heatmap(data)
plt.title('Heatmap')
plt.show()