# to find the numerical columns mean median and mode we have the syntax to find it!!
import pandas as pd
df = pd.read_csv('learning in lab/Iris 2.csv')
print("mean-",df.mean(numeric_only=True))
print("median-",df.median(numeric_only=True))
print("mode-",df.mode(numeric_only=True))
#to find the standard deviation and variance
print("standard deviation-",df.std(numeric_only=True))
print("variance-",df.var(numeric_only=True))

# we can use the describe function to find the mean median mode standard deviation and variance
print('description',df.describe())
#to fill the missing values with mean
df.fillna(df.mean(numeric_only=True),inplace=True)
print(df)
df["Species"] = df["Species"].fillna(df["Species"].mode()[0])
print(df)
#to find the mode of the categorical columns
print("mode of categorical column-",df["Species"].mode()[0])
