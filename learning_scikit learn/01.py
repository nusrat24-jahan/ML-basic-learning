from sklearn.datasets import load_iris
boston= load_iris()
print(boston)
print(boston.DESCR)
X,y=load_iris(return_X_y=True)
print(X)
