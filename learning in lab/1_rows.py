import pandas as pd
df = pd.read_csv('learning in lab/Iris 2.csv')
print(df)
# to read the first 5 rows of the file
print(df.head())
# to read the last 5 rows of the file
print(df.tail())
# to read the first 10 rows of the file
print(df.head(10))
# to read the last 10 rows of the file
print(df.tail(10))