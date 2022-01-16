"""class Araba:
    def __init__(self,marka,renk,plaka,hiz):
        self.marka = marka
        self.renk = renk
        self.plaka = plaka
        self.hiz = hiz

araba1 = Araba('BMW', 'Mavi', '34 LP 233', 30)
araba2 = Araba('MAZDA', 'Siyah', '34 LP 248', 100)



print("------Araba 1 ------")
print(araba1.marka)
print(araba1.renk)
print(araba1.plaka)
print(araba1.hiz)
print()
print()
print("-----Araba 2 -------")
print(araba2.marka)
print(araba2.renk)
print(araba2.plaka)
print(araba2.hiz)"""


class Robot:
    def action(self):
        print('Robot action')

class HelloRobot(Robot):
    def action(self):
        print('Hello World')

class DummyRobot(Robot):
    def start(self):
        print('Started.')


r = HelloRobot()
d = DummyRobot()

r.action()
d.action()

"""
Sınıf (Class): Sınıfın herhangi bir nesnesini karakterize eden bir özellik kümesi tanımlayan bir nesne için kullanıcı tanımlı bir prototiptir. Sınıf özellikleri üyelere, değişkenlere ve metotlara sahiptir. İyi bir sınıf tasarımı için yazılımcının soyutlama (abstraction) işlemini çok iyi yapması gerekir. Sınıf aslında yazılımcının kendi dünyasıdır.
Sınıf değişkeni (Class variable): Bir sınıfın tüm örnekleri tarafından paylaşılan bir değişkendir. Sınıf değişkenleri bir sınıf içerisinde ancak sınıfın herhangi bir metodunun dışında tanımlanır.
Veri üyesi (Data member): Bir sınıf ve nesnelerle ilişkili verileri tutan bir sınıf değişkeni veya örnek değişkenidir.
Fonksiyon aşırı yüklenmesi (Function overloading) – Belirli bir fonksiyona birden fazla davranışın atanmasıdır. Yapılan işlem, ilgili nesne veya argüman türlerine göre değişir.
Örnek değişkeni (Instance variable): Bir yöntem içinde tanımlanan ve yalnızca bir sınıfın geçerli örneğine ait olan bir değişkendir.
Kalıtım (Inheritance): Bir sınıfın özelliklerinin, ondan türetilen diğer sınıflara aktarılmasıdır.
Örnek (Instance): Belirli bir sınıfın bireysel bir nesnesidir. Örneğin, bir Circle sınıfına ait bir nesnedir. Başka bir deyişle Circle sınıfının bir örneğidir.
Örnekleme (Instantiation): Bir sınıfın örneğinin oluşturulmasıdır.
Metot (Method): Sınıf tanımlanırken tanımlanan özel bir fonksiyon türüdür.
Nesne (Object): Sınıfı tarafından tanımlanan bir veri yapısının benzersiz bir örneğidir. Bir nesne, hem veri üyelerini (sınıf değişkenleri ve örnek değişkenleri) ve yöntemleri içerir.
Operatörlerin aşırı yüklenmesi (Operator overloading): Belirli bir operatöre birden fazla işlevin atanmasıdır.
"""


