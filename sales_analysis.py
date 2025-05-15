import numpy as np
import matplotlib.pyplot as plt

# Define sales data
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])

print("=== Zomato Sales Data ===\n")
print("Shape of data:", sales_data.shape)
print("Sample data for first 3 restaurants:\n", sales_data[:3])  # Fixed slicing

# Compute sales statistics
yearly_total = np.sum(sales_data[:, 1:], axis=0)  # Excluding IDs from summation
print("Yearly total sales:", yearly_total)

min_sales = np.min(sales_data[:, 1:], axis=1)  # Corrected axis for per restaurant minimum sales
print("Minimum sales per restaurant:", min_sales)


max_sales = np.max(sales_data[:, 1:], axis=1)
print("Max sales per restaurant:\n", max_sales)

avg_sales = np.mean(sales_data[:, 1:], axis=1)
print("Average sales per restaurant:\n", avg_sales)

cumsum = np.cumsum(sales_data[:, 1:], axis=1)
print("Cumulative sales across each restaurant:\n", cumsum)

# **Plot Average Cumulative Sales Across All Restaurants**
plt.figure(figsize=(8, 6))
plt.plot(np.mean(cumsum, axis=0))
plt.title("Average Cumulative Sales Across All Restaurants")
plt.xlabel("Years")
plt.ylabel("Cumulative Sales Across All Years")
plt.grid(True)
plt.show()

# **Plot Max Sales Across Each Restaurant**
plt.figure(figsize=(6, 5))
plt.plot(sales_data[:, 0], max_sales, marker='o')  # Use restaurant IDs for x-axis
plt.xticks(sales_data[:, 0])  # Explicitly set x-axis ticks to restaurant IDs
plt.title("Max Sales Across Each Restaurant")
plt.xlabel("Restaurant ID")
plt.ylabel("Max Sales")
plt.grid(True)
plt.show()

# **Plot Min Sales Across Each Restaurant**
plt.figure(figsize=(6, 5))  # Fixed figure size consistency
plt.plot(sales_data[:, 0], min_sales, marker='o')  # Corrected x-axis values
plt.xticks(sales_data[:, 0])  # Explicitly set x-axis ticks to restaurant IDs
plt.title("Min Sales Across Each Restaurant")
plt.xlabel("Restaurant ID")
plt.ylabel("Min Sales")
plt.grid(True)
plt.show()
monthly_avg=sales_data[:,1:]/12
print(monthly_avg)
