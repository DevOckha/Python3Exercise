import matplotlib.pyplot as plt 

"""yil = [2011,2012,2013,2014,2015]

oyunucu1 = [8,10,12,7,9]
oyunucu2 = [7,12,5,15,21]
oyunucu3 = [18,21,22,25,19]

#STACK plot

plt.plot([],[], color='y', label='oyuncu1')
plt.plot([],[], color='r', label='oyuncu2')
plt.plot([],[], color='b', label='oyuncu3')


plt.stackplot(yil,oyunucu1,oyunucu2,oyunucu3, colors=['y','r','b'])
plt.title('Yıllara göre atılan goller')
plt.xlabel('Yil')
plt.ylabel('Gol Sayısı')
plt.legend()
plt.show()"""

#PİE grapf

"""goal_types = 'Penaltı', 'Kaleye Atılan Şut', 'Serbest Vuruş'

goals = [12,35,7]
colors = ['y','r','b']

plt.pie(goals, labels=goal_types, colors=colors, shadow=True, explode=(0.05,0.05,0.05), autopct='%1.1F%%')
plt.show()"""

#bar grapf
"""plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20], label='BMW', width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60], label='Audi', width=.5)

plt.legend()
plt.xlabel('GÜN')
plt.ylabel('Mesafe (Km)')

plt.title('Araç Bilgileri')

plt.show()"""



yaslar = [1,2,3,4,12,13,14,51,43,23,45,67,55,47,89,76,77,75,33,25,66,54,112,113,115,123]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yas_gruplari,histtype='bar',rwidth=0.8)
plt.xlabel('yaş grupları')
plt.ylabel('kişi sayısı')
plt.title('histogram')
plt.show()