#Add proper titles, axis labels, and legends.
import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv('learning in lab/Iris 2.csv')
plt.plot(df['SepalLengthCm'], df['SepalWidthCm'], 'o', label='Sepal')
plt.plot(df['PetalLengthCm'], df['PetalWidthCm'], 'o', label='Petal')
plt.xlabel('Length (cm)')
plt.ylabel('Width (cm)')
plt.title('Sepal and Petal Dimensions')
plt.legend()
plt.show()


