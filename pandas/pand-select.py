import pandas as pd 
from numpy.random import rand

df = pd.DataFrame(rand(3,3), index=['A','B','C'], columns=['Columns1', 'Columns2', 'Columns3'])
#Sütun işlemleri
result = df
result = df['Columns1']
result = df[['Columns1', 'Columns2']]

#Satır işlemleri
#loc['row','columns'] => loc["row"] => loc[":", "columns"]

result = df.loc['A']
result = df.loc[:,'Columns1']
print(result)