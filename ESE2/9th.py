# 9. Write a program using Matplotlib to create a basic bubble chart. Use random values for
# the x-axis, y-axis, and bubble sizes.

import matplotlib.pyplot as plt
import numpy as np

# Step 1: Generate random data for x, y, and bubble sizes
np.random.seed(0) # For reproducibility
num_points = 10
x = np.random.rand(num_points) * 100 # Random x-axis values scaled up to 100
y = np.random.rand(num_points) * 100 # Random y-axis values scaled up to 100
sizes = np.random.rand(num_points) * 1000 # Random bubble sizes scaled up to 1000

# Step 2: Create the bubble chart
plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=sizes, alpha=0.5, c='blue', edgecolors='w', linewidth=0.5)

# Step 3: Add labels and titles
plt.title('Basic Bubble Chart with Random Data')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Step 4: Display the bubble chart
plt.grid(True)
plt.show()









# Explanation:
# 1. Import Libraries:
# import matplotlib.pyplot as plt
# import numpy as np
# o We import matplotlib.pyplot for plotting and numpy for generating random
# numbers.
# 2. Generate Random Data:
# np.random.seed(0) # For reproducibility
# num_points = 10
# x = np.random.rand(num_points) * 100 # Random x-axis values scaled up to 100
# y = np.random.rand(num_points) * 100 # Random y-axis values scaled up to 100
# sizes = np.random.rand(num_points) * 1000 # Random bubble sizes scaled up to 1000
# o We use np.random.seed(0) to ensure the random values are the same each time the
# program is run (for reproducibility).
# o num_points defines the number of points in the bubble chart.
# o np.random.rand(num_points) generates random values between 0 and 1. We scale
# these values for the x, y, and sizes arrays.

# 3. Create the Bubble Chart:
# plt.figure(figsize=(10, 6))
# plt.scatter(x, y, s=sizes, alpha=0.5, c='blue', edgecolors='w', linewidth=0.5)
# o plt.figure(figsize=(10, 6)) creates a figure with a specific size.
# o plt.scatter() creates the scatter plot where:
#  x and y define the positions of the bubbles.
#  s=sizes defines the sizes of the bubbles.
#  alpha=0.5 sets the transparency of the bubbles.
#  c='blue' sets the color of the bubbles.

#  edgecolors='w' and linewidth=0.5 add a white border around the bubbles
# to enhance visibility.

# 4. Add Labels and Titles:
# plt.title('Basic Bubble Chart with Random Data')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')
# o We add a title and labels to the x and y axes to make the chart more informative.
# 5. Display the Bubble Chart:
# plt.grid(True)
# plt.show()
# o plt.grid(True) adds a grid to the chart for better readability.
# o plt.show() displays the chart.

# Sample Output:
# The output will be a bubble chart where:
#  The x and y values determine the position of each bubble.
#  The size of each bubble is proportional to the sizes values.
#  Bubbles are colored blue with a white border.
# To run this program, make sure you have matplotlib and numpy installed:
# pip install matplotlib numpy