# Write a python program to plot a bubble chart with labels for each bubble. Display the x and y values as the 
# labels inside the bubbles.

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
sizes = [2500, 2500, 2500, 2500, 2500]  # size of each bubble
labels = [(f"({xi}, {yi})") for xi, yi in zip(x, y)]  # labels for each bubble

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the bubbles
for xi, yi, size, label in zip(x, y, sizes, labels):
    ax.scatter(xi, yi, s=size)
    ax.annotate(label, (xi, yi), textcoords="offset points", xytext=(0,10), ha='center')

# Set axis labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('Bubble Chart with Labels')

# Show the plot
plt.show()
