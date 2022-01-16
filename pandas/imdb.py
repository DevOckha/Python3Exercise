import pandas as pd 

df = pd.read_csv('imdb.csv')

result = df.columns
result = df.info
result = df.head()
result = df.head(10)
result = df.tail(10)
result = df[5:15][['Title', 'Year']].tail(7)
result = df[5:15][['Title', 'Year']]
print(result)