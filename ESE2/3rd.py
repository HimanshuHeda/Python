# 3. Write a Python program to plot a bubble chart with labels for each bubble. Display the x
# and y values as the labels inside the bubbles.

import matplotlib.pyplot as plt

# Step 1: Define data for the bubble chart
x = [10, 20, 30, 40, 50] # X values
y = [15, 25, 35, 45, 55] # Y values

sizes = [200, 400, 600, 800, 1000] # Sizes of the bubbles

# Step 2: Create a scatter plot with the sizes representing the bubbles
plt.scatter(x, y, s=sizes, alpha=0.5, c="red")

# Step 3: Add labels inside the bubbles showing the x and y values
for i in range(len(x)):
    plt.text(x[i], y[i], f"({x[i]}, {y[i]})", ha="center", va="center", color="black")

# Step 4: Add titles and labels
plt.title("Bubble Chart with Labels")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Step 5: Show the bubble chart
plt.show()








# Explanation:
# 1. import matplotlib.pyplot as plt
# o We import the matplotlib.pyplot library, which is used for plotting charts in
# Python.

# 2. Define the Data for the Chart:
# x = [10, 20, 30, 40, 50]
# y = [15, 25, 35, 45, 55]
# sizes = [200, 400, 600, 800, 1000]
# o We define three lists: x for the x-axis values, y for the y-axis values, and sizes for
# the sizes of the bubbles. The size of each bubble is proportional to the
# corresponding value in the sizes list.

# 3. Create a Scatter Plot:
# plt.scatter(x, y, s=sizes, alpha=0.5, c="blue")
# o We create a scatter plot using plt.scatter(). The x and y lists determine the
# positions of the points, s=sizes sets the sizes of the bubbles, and alpha=0.5 makes
# the bubbles semi-transparent. The color c="blue" specifies that the bubbles will be
# blue.

# 4. Add Labels Inside the Bubbles:
# for i in range(len(x)):
# plt.text(x[i], y[i], f"({x[i]}, {y[i]})", ha="center", va="center", color="white")

# o We use a loop to iterate over the x and y values. The plt.text() function adds text
# at the coordinates (x[i], y[i]). The label f"({x[i]}, {y[i]})" displays the x and y
# values inside each bubble.
# o ha="center" and va="center" align the text horizontally and vertically at the center
# of each bubble. The text color is set to white to make it stand out against the blue
# bubbles.
# 5. Add Titles and Labels:
# plt.title("Bubble Chart with Labels")
# plt.xlabel("X Values")
# plt.ylabel("Y Values")
# o We add a title and labels to the x and y axes to make the chart more informative.
# 6. Display the Chart:
# plt.show()
# o This command displays the chart.




# Output:
# When you run this code, a bubble chart will be displayed with bubbles sized according to the
# sizes list, positioned according to the x and y values. The bubbles will contain labels showing the
# corresponding (x, y) coordinates.
# Sample Output Visualization:
#  The bubbles appear at the (x, y) points, such as (10, 15), (20, 25), and so on.
#  Inside each bubble, the text will display the coordinates of that bubble (e.g., &quot;(10, 15)&quot;
# inside the bubble at x=10 and y=15).
# To run this code, ensure you have matplotlib installed:
# pip install matplotlib