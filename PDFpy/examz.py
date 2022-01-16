bölünen = int(input("Bir sayı giriniz: "))

bölen = int(input("Bir sayı daha giriniz: "))

sablon = "{} sayısı {} sayısına".format(bölünen, bölen)

if bölünen % bölen == 0:
    print(sablon, "bölüyünor!")

else:
    print(sablon, "bölünmüyor!")