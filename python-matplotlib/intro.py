import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

df = pd.read_csv("data/phone_stats.csv")

print(df.to_string())


# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a simple line plot
plt.plot(x, y, marker="p")
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

array1 = np.array([2020, 2021, 2022, 2023, 2024])
array2 = np.array([50, 75, 10, 125, 150])

plot_config = dict(
    marker="D",
    markersize=5,
    markerfacecolor="red",
    linestyle="--",
    color="cyan",
    linewidth=2,
)

plt.plot(
    array1,
    array2,
    **plot_config,
)

plt.title("Array Line Plot")
plt.xlabel("Year")
plt.ylabel("Values")
plt.xticks(array1)
plt.show()

earray1 = np.array([1, 2, 3, 4, 5])
earray2 = np.array([2, 3, 5, 7, 11])

plt.grid(axis="y")
plt.plot(earray1, earray2, marker="o", markersize=8)
plt.show()


plt.errorbar(
    earray1,
    earray2,
    yerr=0.5,
    fmt="o",
    ecolor="red",
    capsize=5,
    linestyle="None",
    marker="s",
    markerfacecolor="blue",
)
plt.title("Error Bar Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

categories = np.array(["A", "B", "C", "D"])
values = np.array([23, 45, 56, 78])

# plt.bar(categories, values, color="darkblue")
plt.barh(categories, values, color="darkblue")
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()


# Sample data for pie chart
labels = ["Category A", "Category B", "Category C", "Category D"]
sizes = [25, 35, 20, 20]
colors = ["gold", "lightblue", "lightgreen", "lightcoral"]
plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=140,
    colors=colors,
    explode=(0.1, 0, 0, 0),
)
plt.title("Pie Chart")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# Sample data for scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
a = np.random.rand(50)  # Size of points
b = np.random.rand(50)  # Color of points

plt.scatter(x, y, color="purple", marker="o", alpha=0.7)
plt.scatter(x, y, color="red")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(["Data Points", "Size Variation"])
plt.show()


# Sample data for histogram
categories = np.array(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
values = np.random.randint(1, 100, size=100)
plt.hist(values, bins=10, color="brown", edgecolor="black")
plt.title("Histogram")
plt.xlabel("Value Ranges")
plt.ylabel("Frequency")
plt.show()

scores = np.random.normal(loc=75, scale=10, size=200)
scores = np.clip(scores, 10, 100)  # Ensure scores are between 0 and 100
plt.hist(scores, bins=25, color="teal", alpha=0.7)
plt.title("Normal Distribution Histogram")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.show()


# sub plots
print("Creating subplots...")

figure, axes = plt.subplots(2, 2, figsize=(10, 8))

# First subplot - Line plot

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])

axes[0, 0].plot(x, y, marker="o", color="blue")
axes[0, 0].set_title("Line Plot")
axes[0, 0].set_xlabel("X-axis")
axes[0, 0].set_ylabel("Y-axis")

# Second subplot - Bar chart
categories = np.array(["A", "B", "C", "D"])
values = np.array([23, 45, 56, 78])
axes[0, 1].bar(categories, values, color="green")
axes[0, 1].set_title("Bar Chart")
axes[0, 1].set_xlabel("Categories")
axes[0, 1].set_ylabel("Values")

# Third subplot - Scatter plot
x = np.random.rand(30)
y = np.random.rand(30)
axes[1, 0].scatter(x, y, color="red", marker="x")
axes[1, 0].set_title("Scatter Plot")
axes[1, 0].set_xlabel("X-axis")
axes[1, 0].set_ylabel("Y-axis")

# Fourth subplot - Histogram
data = np.random.randn(1000)
axes[1, 1].hist(data, bins=30, color="purple", edgecolor="black")
axes[1, 1].set_title("Histogram")
axes[1, 1].set_xlabel("Value Ranges")
axes[1, 1].set_ylabel("Frequency")
plt.tight_layout()


plt.show()
