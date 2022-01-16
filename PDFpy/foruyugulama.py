"""import random

i = 1
hak = int(input("Lütfen tahim etme hakkınızı giriniz: "))

while i <= hak:
    rastSayı = random.randint(1,10)
    tahmin = int(input("Sayı tahmininiz: "))
    if rastSayı == tahmin:
        print('Doğru tahmin ettiniz: ')
        break
    elif tahmin < rastSayı:
        print('Tahmin ettiğiniz sayı küçük')
        continue
    else:
        print('tahmin ettiğiniz sayı büyük')
    i += 1"""
    

"""sayi = int(input(' Asal mı? : '))"""



"""a = []
n = int(input())
for i in range(n):
    new_element = int(input())
    a.append(new_element)
print(a)"""

string = 'ABCDCDC'
sub = 'CDC'
a = 0
for i in range(1,len(string)):
    if sub in string[i:5]:
        
        #a += string.count(sub)
print(a)
#print(string[i:5])