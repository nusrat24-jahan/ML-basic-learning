import pandas as pd
from sklearn.datasets import load_iris

import matplotlib.pyplot as plt

# Load the Iris dataset
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Calculate the average petal length for each species
average_petal_length = data.groupby('species')['petal length (cm)'].mean()

# Plot the bar chart
average_petal_length.plot(kind='bar', color=['blue', 'orange', 'green'], figsize=(8, 5))
plt.title('Average Petal Length by Species')
plt.ylabel('Petal Length (cm)')
plt.xlabel('Species')
plt.xticks(rotation=0)
plt.show()

# Print the species with the longest petals
longest_species = average_petal_length.idxmax()
print(f"The species with the longest petals is: {longest_species}")