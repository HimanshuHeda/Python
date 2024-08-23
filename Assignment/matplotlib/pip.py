import matplotlib.pyplot as plt

labels = ['A', 'B','C']
sizes = [50, 30 , 20]

plt.pie(sizes, labels=labels)
plt.title('Pie Chat')
plt.show()