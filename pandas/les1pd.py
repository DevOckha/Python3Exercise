from numpy.random.mtrand import rand
import pandas as pd
from numpy.random import randn


# Label_list = ['I','am','Learning','Data','Science']
# Data_List = [1,2,3,4,5]

# Pd_series1 = pd.Series(Data_List, Label_list)
# print(Pd_series1)

# DataDict = {'Michael_s exam result': 35, 'Olivia_s exam result': 85}
# A = pd.Series(DataDict)

# DataDict2 = {'Michael_s exam result': 44}
# B = pd.Series(DataDict2)

# DataDict3 = {'Darth_Vader_s exam result' :99}
# C = pd.Series(DataDict3)



"""
iki seri arasında dört işlem ve daha fazlası yapılabilir. Ancak dikkat etmeniz gereken bir husus var: ‘A’ değerinin içinde ‘Michael’ ve ‘Olivia’ kişilerinin sınav sonuçları varken,
‘B’ değerinde sadece ‘Michael’ kişisinin sınav sonucu var. İki değeri işleme soktuğumuzda sadece eşleşen değerler işleme tabii olur. 
Eşleşmeyen değer olursa (Bu örnekte ‘Olivia’ kişisi), o değer ‘NaN’ olarak görünecektir.
"""

# DataDict4 = C.append(A)
# print(DataDict4)


df = pd.DataFrame(data=randn(5,5), index = ['A','B','C','D','E'], columns = ['Columns1','Columns2','Columns3','Columns4','Columns5'])
reulst = df[['Columns1','Columns2']] #Çalıştığınız veride size gerekli olan sütunları şu yöntemle alabilirsiniz.
reulst = df['Columns6'] = pd.Series(randn(5),['A','B','C','D','E']) #Yeni bir sütun ekleme işlemini ise şöyle yapıyoruz.
print(reulst)






