import pandas as pd 
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)

df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])

result = df
result = df.columns
result = df.head(5) # satır 
result = df.tail()
result = df['Column1'].head()
result = df[['Column1','Column2']].head()
result = df[df % 2 == 0]
result = df[df['Column1'] > 50]
result = df.query('<Age<25')['Column1']
print(result)