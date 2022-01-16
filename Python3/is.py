namePolindrom = str(input("Lütfen polindrom bir isim giriniz: "))

if namePolindrom == namePolindrom[::-1]:
	print(f"Evet bu bir polindrom isim -->{namePolindrom}")
else:
	print("polindrom bi isim giriniz!")