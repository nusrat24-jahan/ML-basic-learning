from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
data=load_breast_cancer(as_frame=True).frame
print(data)
X,y=load_breast_cancer(return_X_y=True)