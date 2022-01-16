import time 
import random
import sys
class Oyuncu():
    def __init__(self,isim,can=5,enerji=100):
        self.isim = isim
        self.can = can
        self.darbe = 0
        self.enerji = enerji

    
    def mevcut_durumu_görüntüle(self):
        print('darbe: ', self.darbe)
        print('can: ', self.can)
        print('enerji: ', self.enerji)
    
    def saldır(self, rakip):
        print('Bir saldırı gerçekleştirdiniz.')
        print('Saldırı sürüyor bekleyiniz.')

        for i in range(10):
            time.sleep(3)
            print('.', end=' ', flush=True)
        sonuç = self.saldırı_sonucunu_hesapla()

        if sonuç == 0:
            print('\nSONUÇ: kazanan taraf yok')
        if sonuç == 1:
            print('\nSONUÇ: rakibinizi darbeledeniz')
            self.darbele(rakip)

        if sonuç == 2:
            print('\nSONUÇ: rakibinizden darbe aldınız')
            self.darbele(self)
    def saldırı_sonucunu_hesapla(self):
        return random.randint(0, 2)  
    

    def kaç(self):
        print('Kaçılıyor')
        for i in range(10):
            time.sleep(3)
            print('\n', flush=True)
        print('Rakibiniz sizi yakaladı')

    def darbele(self, darbelenen):
        darbelenen.darbe += 1
        darbelenen.enerji -= 1
        if (darbelenen.darbe % 5) == 0:
            darbelenen.can -= 1
        if darbelenen.can < 1:
            darbelenen.enerji = 0
        print('Oyunu {} kazandı!'.format(self.isim))
        self.oyundan_çık()
    
    
    def oyundan_çık(self):
        print('Çıkılıyor...')
        sys.exit()


siz = Oyuncu('Ahmet')
rakip = Oyuncu('Mehmet')


while True:
    print('Şu anda rakibinizle karşı karşıyasınız.',
    'Yapmak istediğiniz hamle: ',
    'Saldır: s',
    'Kaç: k',
    'Çık: q', sep='\n')
    hamle = input('\n> ')
    if hamle == 's':
        siz.saldır(rakip)
        print('Rakibinizin durumu')
        rakip.mevcut_durumu_görüntüle()
        print('Sizin durumunuz')
        siz.mevcut_durumu_görüntüle()
    if hamle == 'k':
        siz.kaç()
    if hamle == 'q':
        break