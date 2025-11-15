# to read the rows of the the file

import pandas as pd
df = pd.read_csv('pandas/netflix_titles.csv')
print(df)
# to read the first 5 rows of the file
print(df.head())
# to read the last 5 rows of the file
print(df.tail())
# to read the first 10 rows of the file
print(df.head(10))
