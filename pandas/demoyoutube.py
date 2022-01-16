import pandas as pd
from pandas.io.parsers import read_csv 

df = pd.read_csv('youtube-ing.csv')

result = df.head(10)
result = df[5:10].head(5)

result = df.columns
result = len(df.columns)
df = df.drop['']














print(result)