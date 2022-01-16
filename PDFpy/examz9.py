sayı_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]
print(("{:^9} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
for i in range(17):
    print("{0:^9} {0:^9o} {0:^9x} {0:^9b}".format(i))