# Write a Python program to plot a bubble chart with labels for each bubble. 
# Display the x and y values as the labels inside the bubbles.


# Importing the necessary library for plotting
import matplotlib.pyplot as plt

# Data for the x and y axes
x = [1, 2, 3, 4, 5]  # X-coordinates representing days of the week
y = [10, 20, 15, 30, 25]  # Y-coordinates representing total bill amounts

# Create a scatter plot using the x and y data points
plt.scatter(x, y)

# Adding a label to the x-axis
plt.xlabel("Day of the Week")

# Adding a label to the y-axis
plt.ylabel("Total Bill")

# Adding a title to the plot
plt.title('Bubble Chart')

# Display the plot on the screen
plt.show()
