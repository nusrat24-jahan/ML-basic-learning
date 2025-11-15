# Dataset for the histogram
import matplotlib.pyplot as plt
data = [12, 15, 20, 21, 22, 22, 23, 24, 25, 25, 25, 26, 27, 28, 30, 30, 32, 35, 36, 40]

# You can use this dataset to plot a histogram using libraries like matplotlib.
plt.hist(data, bins=5, color='pink', edgecolor='black')
plt.xlabel('score range')
plt.ylabel('No. of students')
plt.title('data oakjans')
plt.show()