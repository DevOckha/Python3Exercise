import pandas as pd 
from numpy.random import randn
OuterIndex = ['Group1','Group1','Group1','Group2','Group2','Group2','Group3','Group3','Group3']
InnerIndex = ['Index1','Index2','Index3','Index1','Index2','Index3','Index1','Index2','Index3']

hierarchy = list(zip(OuterIndex,InnerIndex))
hierarchy = pd.MultiIndex.from_tuples(hierarchy)

df = pd.DataFrame(randn(9,3), hierarchy, columns=['Column1','Column2','Column3'])
result = df.loc['Group1']
result = df.loc[['Group1','Group2']]
result = df.loc['Group1'].loc['Index1'] #‘Group’, ‘Column’ ve ‘Index’ gibi değerleri bu şekilde çağrılabilir ve birden fazla ve farklı türden de çağırma yapabilirsiniz.
result = df.loc['Group1'].loc['Index1']['Column1']
result = df.xs('Group1').xs('Index1').xs('Column1')
print(result)

"""
2 adet index oluşturup ‘zip’ fonksiyonu ile birleştirdik. Bunu yaparken liste kullandık ama siz ‘Tuple’ ve ‘Dict’ de kullanabilirsiniz.
2. görselde bunu ‘hierarchy’e eşitledik. Sonra ise ‘pd.MultiIndex.from_tuples()’ özelliği ile Multi index’i oluşturduk
En son görselde ise ‘rand()’ fonksiyonu ile rastgele değerler atayıp sütun bilgilerini verdik. 
Ve görüldüğü üzere ‘Group’ ‘Index’ ‘Column’ değerlerine sahip Multi index DataFrame elde ettik.

"""