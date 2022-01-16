

class Çalışan():
    kabiliyetleri = ['sınıf niteliği']
    def __init__(self):
        self.kabiliyetleri = ['örnek niteliği']

ahmet = Çalışan()
print(Çalışan.kabiliyetleri)
print(ahmet.kabiliyetleri)