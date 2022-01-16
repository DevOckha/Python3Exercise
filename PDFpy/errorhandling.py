# error handling => hata yönetimi 

"""try:
    x = int(input('x: '))
    y = int(input('y: '))
except Exception as ex :
    print('Yanlış bir bilgi girdiniz!', ex)
finally:
    print('her zaman çalışacak olan kodları finally: kodunun altına yazabiliriz!')"""

#Exception hataları genelleyip oluşan hata türünü ekrana yazdırabiliriz. Exception base bir hata türüdür




"""class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception('name alanı fazla karakter içeriyor!')
        else:
            self.name = name

p = Person('aliiiiiiiiiiiiiii', 1999)"""


"""liste = ['1','2','5a', '10b','abc']


for i in liste:
    try:
        if i.isdecimal():
            print(i)
    except ValueError:
        continue"""




"""while True:
    cikis = input("(Programdan çıkmak için lütfen 'Q' tuşuna basınız) bir sayı giriniz: ")
    if cikis.upper() == 'Q':
        break
    try:
        result = float(cikis)
        print(f'Girdiğiniz  değer bir sayıdır:{cikis}')
    except ValueError:
        print('geçersiz sayı')
        continue"""



def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('negatif değer')
    result = 1
    for i in range(1,x+1):
        result *= i
    return result



for x in [5,10,20,-3,'10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)































        