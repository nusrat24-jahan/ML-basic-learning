import seaborn as sns

import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset('iris')
print(iris)

# Create a scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species', palette='Set1')

# Add labels and title
plt.title('Petal Length vs Petal Width')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

# Show the plot
plt.show()