import pandas as pd
from pandas.io.parsers import read_csv 


df = pd.read_csv('nba.csv')

result = df.head(10)
result = df.count()
result = df['Salary'].mean()
result = df['Salary'].sum()
result = df['Salary'].max()
result = df.groupby('Name').max()['Salary']
result = df[df['Salary'] == df['Salary'].max()]['Name'].iloc[0]
result = df[(df['Age'] >=20) & (df['Age'] < 25)][['Name','Team','Age']].sort_values('Age')
result = df[df['Name'] == 'John Holland'][['Team','Name']]
result = df.groupby('Team').mean()['Salary']
result = len(df.groupby('Team'))
result = df.groupby('Team').nunique()
result = df['Team'].value_counts()
df = df.dropna()
result = df[df['Name'].str.contains('and')]
print(result)