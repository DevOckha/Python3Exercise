#tekrar eden itemleri barındırmaz
#kümeler değiştirilebilir
#kümelerde sıralama işlemi yoktur

string = "Python is awesome programing language. Python is better than."
stringSet = set(string.split())
print(f"Cümle {len(stringSet)} farklı kelimeden oluşuyor.")
