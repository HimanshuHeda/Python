import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Create a violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x="day", y="total_bill", data=tips)

# Add title and labels
plt.title("Violin Plot of Total Bill by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill")

# Show the plot
plt.show()