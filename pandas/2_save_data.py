# we will learn about the imp things to create the data frame and save it to different file formats
import pandas as pd
# create a data frame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)
print(df)
# save the data frame to a csv file
# df.to_csv('pandas/people.csv', index=False)
# save the data frame to an excel file
df.to_excel('pandas/people2.xlsx', index=False)
# save the data frame to a json file
df.to_json('pandas/people3.json', orient='records', lines=True)