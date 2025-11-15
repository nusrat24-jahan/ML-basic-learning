#step 1 - sample data frame

import pandas as pd
data={
    'Name':['Tom','nick','krish','jack','nusrat'],
    'Age':[20,21,19,18,19],
    'salary':[2000,3000,4000,5000,6000]
}
df=pd.DataFrame(data)
print(df)
#step 2 - describe() function
print("Describe the data frame")
print(df.describe())
#step 3 - include parameter
print("Describe the data frame with include parameter")
print(df.describe(include=['object']))
#step 4 - exclude parameter
print("Describe the data frame with exclude parameter")
print(df.describe(exclude=['number']))
#step 5 - percentiles parameter
print("Describe the data frame with percentiles parameter")
print(df.describe(percentiles=[.10,.20,.30,.40,.50,.60,.70,.80,.90]))
#step 6 - transpose parameter
print("Describe the data frame with transpose parameter")
print(df.describe().transpose())
#step 7 - include all data types
print("Describe the data frame with include all data types")
print(df.describe(include='all'))
#step 8 - custom percentiles
print("Describe the data frame with custom percentiles")
print(df.describe(percentiles=[.25,.5,.75]))
#step 9 - describe specific columns
print("Describe specific columns")
print(df[['Age','salary']].describe())
#step 10 - describe with datetime data
print("Describe with datetime data")
data2={
    'Name':['Tom','nick','krish','jack','nusrat'],
    'DOB':['2000-01-01','2001-02-02','2002-03-03','2003-04-04','2004-05-05']
}