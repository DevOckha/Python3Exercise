sayilar = [1,3,5,7,9,12,19,21]
"""x = 0 
while x < len(sayilar):
    print(sayilar[x])
    x += 1
"""


"""ilksayi = int(input("İlk sayı: "))
ikinciksayi = int(input("ikinci sayı: "))

odd = []

while ilksayi <= ikinciksayi:
    if ilksayi % 2 != 0:
        odd.append(ilksayi)
    ilksayi += 1
print(odd)"""



"""x = 100
while x >= 1:
    print(x)
    x -= 1"""


"""numbers = []

while len(numbers) < 5:
    num = int(input('lütfen 5 adet sayı giriniz: '))
    numbers.append(num)
print(sorted(numbers))"""

urunler = []
count = 1
lcount = int(input("Kaç adet ürün sıralayacaksınız? :"))

while count < lcount:
    name = input('ürün adı: ')
    price = input('ürün fiyatı: ')
    urunler.append({
        'name': name,
        'price': price
    })
    count += 1
for urun in urunler:
    print(f"ürün adı: {urun['name']} ürün fiyatı {urun['price']}")