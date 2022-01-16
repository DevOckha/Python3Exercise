"karakter_dizisi[öğe_sırası]"


"""isim = input("isiminiz: ")

for i in range(len(isim)):
    print("isminizin {}. harfi: {}".format(i+1, isim[i]))
"""

"karakter_dizisi[alınacak_ilk_öğenin_sırası:alınacak_son_öğenin_sırasının_bir_fazlası]"

"""site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"

for isim in site1, site2, site3, site4:
    print("site: ", isim[4:-4])
"""
"""
Yukarıdaki örnekte isim[4:-4] yapısını
kullanarak, site1, site2, site3, site4 adlı karakter dizilerini, ilk dört ve son dört karakterler
hariç olacak sekilde dilimledik. Böylece elimizde ilk dört ve son dört karakter arasındaki bütün
karakterler kalmıs oldu. Yani “google”, “istihza”, “yahoo” ve “gnu”.
"""



" Karakter Dizilerini Ters Çevirmek "

"""isim = "ali"
print(isim[::-1])
"""
"""
isim degiskeni içindeki bütün karakterleri, en son karakterden ilk karaktere
kadar sondan basa dogru tek tek ekrana yazdır!
"""

"kardiz[ilk_karakter:son_karakter:atlama_sayısı]"
"isim[3:1:-1]"

"""for i in reversed("Sana Gül Bahçesi Vaadetmedim"):
    print(i, end="")

print(*reversed("Sana Gül Bahçesi Vaadetmedim"), sep="")
"""
" string ifadeleri sıralamak için sorted('çiçek') fonksiyonu kullanılır."
"çıktı liste şeklinde olur"



"""sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"

sesliler = ""
sessizler = ""

kelime = "istanbul"

for i in kelime:
    if i in sesli_harfler:
        sesliler += i
    else:
        sessizler += i

print("sesli harfler: ", sesliler)
print("sessiz harfler: ", sessizler)

"""
"""
Eger yazdiginiz bir programda numaralandirmaya iliskin islemler yapmaniz gerekiyorsa
Python’in size sundugu çok özel bir fonksiyondan yararlanabilirsiniz. Bu fonksiyonun adi
enumerate().

print(*enumerate("istihza"))
"""
"""for i in enumerate("istihza"):
    print(i)"""

"""for sıra, harf in enumerate("istihza", 1):
    print(sıra, harf)"""

"karakter_dizisi.metot(parametre)"
"karakter_dizisi.replace(eski_karakter_dizisi, yeni_karakter_dizisi)"

"""kardiz = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"
kardiz = kardiz.split(',')
for i in kardiz:
    print(i)"""


"""metin = Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin
Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını
düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından
gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz
komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek
adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama
dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek
halini almıştır diyebiliriz."""

"""clprint(metin.splitlines())"""