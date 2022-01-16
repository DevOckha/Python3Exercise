ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except (ValueError, ZeroDivisionError):
    print("Bir Hata oluştu!")


"""
try:
    hata verebileceğini bildiğimiz kodlar
except HataAdı:
    hata durumunda yapılacak işlem
"""

"""
while True:
    ilk_sayı = input("ilk sayı (Programdan çıkmak için q tuşuna basın): ")
    if ilk_sayı == "q": 
        break
    ikinci_sayı = input("ikinci sayı: ")
    try:
        sayı1 = int(ilk_sayı)
        sayı2 = int(ikinci_sayı)
        print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
    except (ValueError, ZeroDivisionError):
        print("Bir hata oluştu!")
        print("Lütfen tekrar deneyin!")
"""


"""

Diyelim ki kullanıcıya olası bir hata durumunda hem kendi yazdıgınız hata mesajını, hem
de özgün hata mesajını göstermek istiyorsunuz



ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")
try:
sayı1 = int(ilk_sayı)
sayı2 = int(ikinci_sayı)
print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except (ValueError, ZeroDivisionError) as hata:
print("Bir hata oluştu!")
print("orijinal hata mesajı: ", hata)
"""



"""
try:
...bir takım işler...
except birHata:
...hata alınınca yapılacak işlemler...
finally:
...hata olsa da olmasa da yapılması gerekenler...

finally.. blogunun en önemli özelligi, programın çalısması sırasında herhangi bir hata
gerçeklesse de gerçeklesmese de isletilecek olmasıdır

Eger yazdıgınız programda mutlaka
ama mutlaka isletilmesi gereken bir kısım varsa, o kısmı finally... blogu içine yazabilirsiniz

"""



"""
try:
dosya = open("dosyaadı", "r")
...burada dosyayla bazı işlemler yapıyoruz...
...ve ansızın bir hata oluşuyor...
except IOError:
    print("bir hata oluştu!")
finally:
    dosya.close()


"""



"""
tr_karakter = "şçğüöıİ"
    parola = input("Parolanız: ")
for i in parola:
    if i in tr_karakter:
        raise TypeError("Parolada Türkçe karakter kullanılamaz!")
    else:
        pass
print("Parola kabul edildi!")
Bazen, yazdigimiz bir programda, kullanicinin yaptigi bir islem normal sartlar altinda hata
vermeyecek olsa bile biz ona ‘Python tarzi’ bir hata mesaji göstermek isteyebiliriz. Böyle
bir durumda ihtiyacimiz olan sey Python’in bize sundugu
adli deyimdir. Bu deyim
raise
yardimiyla duruma özgü hata mesajlari üretebiliriz. Bir örnek verelim:

"""

