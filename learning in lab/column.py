#Boxplot of petal_length for each species.

import pandas as pd
df = pd.read_csv('learning in lab/Iris 2.csv')
print(df)
print(df.columns)
import matplotlib.pyplot as plt
plt.boxplot([df[df['Species']=='Iris-setosa']['PetalLengthCm'],
             df[df['Species']=='Iris-versicolor']['PetalLengthCm'],
             df[df['Species']=='Iris-virginica']['PetalLengthCm']],
            labels=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
plt.ylabel('Petal Length (cm)')
plt.title('Boxplot of Petal Length by Species')
plt.show()

