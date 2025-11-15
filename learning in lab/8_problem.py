import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

import matplotlib.pyplot as plt

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target

# Map the target integers to species names
iris_df['species'] = iris_df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Create a pairplot
sns.pairplot(iris_df, hue='species', diag_kind='hist', markers=["o", "s", "D"])
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.show()