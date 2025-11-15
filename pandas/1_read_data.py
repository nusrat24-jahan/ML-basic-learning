import pandas as pd
#read data from csv file

data = pd.read_csv('pandas/netflix_titles.csv')
print(data)
# to read the excel file we use the syntax pd.read_excel('file_name.xlsx')
# to read the json file we use the syntax pd.read_json('file_name.json')
# to read the html file we use the syntax pd.read_html('file_name.html')
# to read the sql file we use the syntax pd.read_sql('file_name.sql')
# to read the clipboard data we use the syntax pd.read_clipboard()
# to read the data from a dictionary we use the syntax pd.DataFrame(dictionary_name)
# to read the data from a list we use the syntax pd.DataFrame(list_name)
# to read the data from a numpy array we use the syntax pd.DataFrame(numpy_array_name)
# to read the data from a series we use the syntax pd.DataFrame(series_name)    
