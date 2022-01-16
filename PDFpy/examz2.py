#print(round(2.68)) sayıyı yuvarlamak için kullanılır   
#print(pow(23,2)) verilen ilk  sayının karesini hesaplamak için
#aynı anlama geliyorlar
#pow(25, 2, 5) == (25 ** 2) % 5

giriş = """
(1) topla
(2) çıkar
(3) çarp
(4) böl
(5) karesini hesapla
(6) kare kök hesapla
"""
print(giriş)

seçenek1 = "(1) topla"
seçenek2 = "(2) çıkar"
seçenek3 = "(3) çarp"
seçenek4 = "(4) böl"
seçenek5 = "(5) karesini hesapla"
seçenek6 = "(6) karekök hesapla"
print(seçenek1, seçenek2, seçenek3, seçenek4, seçenek5, sep='\n')

soru = input("Yapmak istediğiniz işlemin numarasını giriniz: ")

if soru == "1":
    sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
    sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
    print(sayı1, "+", sayı2, "=", sayı1+sayı2 )
elif soru == "2":
    sayı3 = int(input("Çıkarma işlemi için ilk sayıyı giriniz: "))
    sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı giriniz: "))
    print(sayı3, "-", sayı4, "=", sayı3-sayı4)
elif soru == "3":
    sayı5 = int(input("Çarpma işlemi için ilk sayıyı giriniz: "))
    sayı6 = int(input("Çarpma işlemi için ikinci sayıyı giriniz: "))
    print(sayı5, "x", sayı6, "=", sayı5*sayı6)
elif soru == "4":
    sayı7 = int(input("Bölme işlemi için ilk sayıyı giriniz: "))
    sayı8 = int(input("Bölme işlemi için ikinci sayıyı giriniz: "))
    print(sayı7, "/", sayı8, "=", sayı7/sayı8)
elif soru == "5":
    sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı giriniz: "))
    print(sayı9,"Sayının karesi =", sayı9**2)
elif soru == "6":
    sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı giriniz: "))
    print(sayı10, "Sayının karekökü =", sayı10**(0.5))
else:
    print("Yanlış giriş.")
    print("Aşağıdaki seçeneklerden birini giriniz:", giriş)