import pandas as pd
df = pd.read_csv('pandas/netflix_titles.csv')
# to get the columns of the data frame 
print(df.info())
# To analyze the small data set
df_small =pd.read_csv('pandas/people.csv')
print(df_small.info())