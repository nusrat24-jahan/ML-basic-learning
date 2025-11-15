import pandas as pd 
df = pd.read_csv('learning in lab/Iris 2.csv')
print(df.shape)
#column name and data type
print(df.columns)
print(df.dtypes)
#to find the missing the values in each column
print(df.isnull().sum())
#for categorical column print how many unique values
print("categorical-",df['Species'].unique())
#to find the number of unique values in each column
print("gdk",df.nunique())