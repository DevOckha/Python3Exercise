from types import LambdaType
import matplotlib.pyplot as plt
import numpy as np


"""x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y,'o--r')
plt.axis([0,6,0,20])
plt.title('Grafik Başlığı')
plt.xlabel('x label')
plt.ylabel('y label')"""



"""
x = np.linspace(0,2,100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')
"""





import pandas as pd 
df = pd.read_csv('nba.csv')
df = df.drop(['Number'], axis=1).groupby('Team').mean()
df.head().plot(subplots=True)
plt.legend()
plt.show()