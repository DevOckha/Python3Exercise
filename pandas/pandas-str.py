import pandas as pd 

data = pd.read_csv('imdb.csv')

data.dropna(inplace=True, thresh= 2)

#data['Title'] = data['Title'].str.upper()
#data['index'] = data['Title'].str.find('a')
data = data.Title.str.contains('Hands')
print(data.head(10))