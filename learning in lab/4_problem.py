#method2
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('learning in lab/Iris 2.csv')
print(df)
df['Species'] = df['Species'].astype('category').cat.codes
#Scatter plot of sepal_length vs. sepal_width, colored by species.
plt.scatter(df['SepalLengthCm'], df['SepalWidthCm'],c=df['Species'], cmap='viridis')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Scatter plot of Sepal Length vs Sepal Width')
plt.colorbar(label='Species')
plt.show()
print(df.columns)