"""users = {
    'yakup':{
        'age': 21,
        'email': 'yakup@gmail.com',
        'phone': '5389445656'
        }
}

print(users['yakup']['age'])"""



# ogrenciler = {}
# for i in range(3):
#     number = input("Öğrenci No: ")
#     name = input("Öğrenci Adı: ")
#     surname  = input("Öğrenci Soyad: ")
#     phone = input("Öğrenci Telefon: ")


#     ogrenciler.update({
#         number: {
#             'ad': name,
#             'soyad': surname,
#             'telefon': phone
#         }
#     })

# #print( ogrenciler)


liste = [['ali',32], ['veli',24], ['ahmet',34]]
sözlük = {}
for i in liste:
    sözlük[i[0]] = i[1]
print(sözlük)

#Yani sözlüklere anahtar olarak her veri tipini atayamayiz.
# Bir degerin ‘anahtar’ olabilmesi için, o ögenin degistirilemeyen (immutable) bir veri tipi
# olmasi gerekir.





ing_sözlük = {"dil": "language", "bilgisayar": "computer", "masa": "table"}
sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:")
print(ing_sözlük.get(sorgu, "Bu kelime veritabanımızda yoktur!"))

"""
Gördügünüz gibi, burada çok basit bir metot yardımıyla bütün dertlerimizi hallettik.
Sözlüklerin get() adlı metodu, parantez içinde iki adet argüman alır. Birinci argüman
sorgulamak istedigimiz sözlük ögesidir. Ikinci argüman ise bu ögenin sözlükte bulunmadıgı
durumda kullanıcıya hangi mesajın gösterilecegini belirtir

"""


elemanlar = "Ahmet", "Mehmet", "Can"
adresler = dict.fromkeys(elemanlar, "Kadıköy")
adresler


"""
metodu öteki metotlardan biraz farklidir. Bu metot mevcut sözlük üzerinde
fromkeys()
islem yapmaz.
fromkeys()
‘in görevi yeni bir sözlük olusturmaktir. Bu metot yeni bir sözlük
olustururken listeler veya demetlerden yararlanir. Söyle ki:

"""
