"""
1 how big is the data
2 what are the names of columns
shape and columns
"""
import pandas as pd
data={
    'Name':['Alice','Bob','Charlie','David','Eva'],
    'Age':[24,27,22,32,29],
    'City':['New York','Los Angeles','Chicago','Houston','Phoenix']
}
df=pd.DataFrame(data)
print(f'shape: {df.shape}')
print(f'columns: {df.columns}')
print(df)
print(type(df.columns))
# to convert the columns to list
print(f'columns as list: {df.columns.tolist()}')
print(type(df.columns.tolist()))
# to convert the columns to array
print(f'columns as array: {df.columns.values}')
print(type(df.columns.values))
# to convert the columns to set
print(f'columns as set: {set(df.columns)}')             
print(type(set(df.columns)))
# to convert the columns to string

print(f'columns as string: {", ".join(df.columns)}')
print(type(", ".join(df.columns)))
# to get the number of columns
print(f'number of columns: {len(df.columns)}')
print(type(len(df.columns)))
# to get the number of rows
print(f'number of rows: {len(df)}')
print(type(len(df)))
# to get the index of the data frame
print(f'index: {df.index}')
print(type(df.index))
# to convert the index to list
print(f'index as list: {df.index.tolist()}')
print(type(df.index.tolist()))

