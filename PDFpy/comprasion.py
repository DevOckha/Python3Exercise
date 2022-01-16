"""for i in range(1):
    firstnum = int(input("Enter first number: "))
    secondnum = int(input("Enter second number: "))
    if firstnum > secondnum:
        print(firstnum)
    else:
        print(secondnum)
"""

"""for i in range(1):
    v1 = int(input("Birinci vize notunuzu giriniz: "))
    v2 = int(input("ikinci vize notunuzu giriniz: "))
    f1 = int(input("Birinci finaz notunuzu giriniz: "))
    f2 = int(input("ikinci finaz notunuzu giriniz: "))
    n = ((v1+v2)*0.6 + (f1+f2)*0.4)/2
    if n > 50:
        print('geçti', n)
    else:   
        print("kaldı", n)
"""


sayı = int(input("Lütfen bir sayı giriniz: "))

print(sayı%2==0, "Çift")
print(sayı%2!=0, "Tek")
