import matplotlib.pyplot as plt

# Example data
x = [5, 7, 8, 7, 6, 9, 5, 6, 7, 8]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

plt.scatter(x, y, color='green', marker='p', label='student_data')   # scatter plot
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Simple Scatter Plot")
plt.legend()
plt.grid(True)
plt.show()
