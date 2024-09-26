import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y = [1, 4, 6, 8, 2]

plt.fill_between(x, y)
plt.title('Area Chart')
plt.show()

# plt.fill_between([1, 2, 3, 4, 5], [1, 4, 6, 8, 2])
# plt.title('Area Chart')
# plt.show()