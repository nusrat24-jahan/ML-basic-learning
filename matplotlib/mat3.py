import matplotlib.pyplot as plt

# Data for the bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 12, 9]

# Create the bar chart
plt.barh(categories, values, color='green', label='horizontal example')


# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.legend()
# Show the plot
plt.show()