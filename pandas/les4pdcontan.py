import pandas as pd 

data = {'A': ['A1','A2','A3','A4'],'B': ['B1','B2','B3','B4'],'C': ['C1','C2','C3','C4']}
data1 = {'A': ['A5','A6','A7','A8'],'B': ['B5','B6','B7','B8'],'C': ['C5','C6','C7','C8']}
df1 = pd.DataFrame(data, index = [1,2,3,4])
df2 = pd.DataFrame(data1, index = [5,6,7,8])
result = pd.concat([df1,df2])
print(result)