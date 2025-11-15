
#from this we load the datasets already presents in the sklearn library
from sklearn.datasets import load_breast_cancer, fetch_california_housing
import matplotlib.pyplot as plt
# load_breast_cancer() function loads the breast cancer dataset from the sklearn library
# fetch_california_housing() function fetch it from the internet
# we basically get the dictionares of the data which contains the keys like "data",''target','target_names','feature_names','DESCR','frame' ,etc
df=load_breast_cancer(as_frame=True).frame
# this function frame the data as a pandas data frame
# print(df) 
#when we write the X,y = load_breast_cancer(return_X_y=True) it returns the features and target variable separately
X,y=load_breast_cancer(return_X_y=True)
#we can also write the X=data.data and y=data.target
# print(X)
# print(y)
df2=fetch_california_housing(as_frame=True).frame
# print(df2)
#now we can plot the data using matplotlib for the load_breast_cancer dataset
df.hist(figsize=(14,8))
plt.tight_layout()
plt.show()
from sklearn.datasets import make_blobs
# Generate synthetic dataset using make_blobs
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
plt.scatter(X[:, 0], X[:, 1], s=30)
plt.show()
# X is a 2D array of shape (300, 2) representing the coordinates of the points
# y is a 1D array of shape (300,) representing the cluster labels for each point
# We can use this synthetic dataset for clustering tasks
# In summary, this code demonstrates how to load datasets from sklearn, visualize them using matplotlib, and generate synthetic datasets for clustering tasks.
# print(X)

