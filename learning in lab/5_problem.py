from sklearn.datasets import load_iris
df=load_iris(as_frame=True).frame
print(df)

import matplotlib.pyplot as plt
df.hist(figsize=(14,8))
plt.show()
#Scatter plot of sepal_length vs. sepal_width, colored by species.


