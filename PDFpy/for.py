


numbers = [1,3,5,7,9,12,19,21]
oddnum = []
"""for num in numbers:
    if num % 3 == 0:
        oddnum.append(num)

print(oddnum)"""
"""toplam = 0
for t in numbers:
    toplam += t
print(toplam)"""



"""for i in numbers:
    if i % 2 != 0:
        print(i**2)"""





"""sehirler = ['kocaeli','istanbul','ankara','izmir','rize']


for i in sehirler:
    if len(i) <=5:
        print(i)"""


urunler = [
    {'name':'samsung S6', 'price':'3000'},
    {'name':'samsung S7', 'price':'4000'},
    {'name':'samsung S8', 'price':'5000'},
    {'name':'samsung S9', 'price':'6000'},
    {'name':'samsung S10', 'price':'7000'},
]

"""toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print(f'ürünlerin toplam fiyatı: {toplam}')

"""

"""
for i in urunler:
    for key,val in i.items():
        for j in val.splitlines():
            if j.isalnum() and int(j) <= 5000:
                toplam += int(j)      
print(toplam)"""

"""for i in urunler:
    for key,val in i.items():
        for j in val.split():
            if j.isalpha() or  j.:
                print(j)
                """




for urun in urunler:
    if int(urun['price']) <= 5000:
        print(urun['name'])        





















