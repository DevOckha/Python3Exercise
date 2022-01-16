from datetime import date, datetime

an = datetime.now()
#ize içindeki bulunduğumuz andaki tarih, saat ve zaman bilgilerini verir.


tarih = datetime.ctime(an)

#ctime() fonksiyonu, içinde bulunduğumuz ana ilişkin tarih ve zaman bilgilerini içeren okunaklı bir karakter dizisi verir


tarih = datetime.strftime(an, '%x')
#strftime() fonksiyonu, size tarih ve zaman bilgilerini ihtiyaçlarınız doğrultusunda biçimlendirme imkanı sunar.
"""
Bu fonksiyon toplam iki parametre alır. İlk parametre, tıpkı ctime() fonksiyonunda olduğu gibi, bir datetime.datetime sınıfıdır.
İkinci parametre ise, tarih/zaman bilgisini içeren karakter dizisini nasıl biçimlendirmek istediğimizi gösteren bir biçimlendiricidir.
"""

"""
%a
hafta gününün kısaltılmış adı

%A
hafta gününün tam adı

%b
ayın kısaltılmış adı

%B
ayın tam adı

%c
tam tarih, saat ve zaman bilgisi

%d
sayı değerli bir karakter dizisi olarak gün

%j
belli bir tarihin, yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı

%m
sayı değerli bir karakter dizisi olarak ay

%U
belli bir tarihin yılın kaçıncı haftasına geldiğini gösteren 0-53 arası bir sayı

%y
yılın son iki rakamı

%Y
yılın dört haneli tam hali

%x
tam tarih bilgisi

%X
tam saat bilgisi
"""

t = '27 Mayıs 2014'
"""

İşte böyle bir durumda strptime() adlı fonksiyon devreye 
girerek, tarih/zaman bilgisi içeren herhangi bir karakter dizisini datetime.datetime türünde bir nesneye dönüştürebilmemiz için bize bir yol sunar.

"""

z = datetime.strptime(t, '%d %B %Y %H:%M:%S ') 

