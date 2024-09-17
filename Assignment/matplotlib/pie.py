#  Program for PIE chart 


import matplotlib.pyplot as plt
# import numpy as np

labels= ['A','B','C']
sizes= [20,30,50]
plt.pie(sizes, labels=labels)
plt.title('pie chart')
plt.show()
