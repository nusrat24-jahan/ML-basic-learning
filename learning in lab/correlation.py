import pandas as pd 
from sklearn.datasets import load_iris
import seaborn as sns
import matplotlib.pyplot as plt
iris=load_iris(as_frame=True)
X,y=load_iris(return_X_y=True)
df=pd.DataFrame(X,columns=iris.feature_names)
corr_matrix=df.corr()
print(corr_matrix)
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()