"""
python fonksiyonları, yukarıdaki örnekte de gördüğünüz gibi, nasıl başka fonksiyonları çağırabiliyorsa, 
aynı şekilde, istenirse, kendi kendilerini de çağırabilirler. İşte bu tür fonksiyonlara Python programlama dilinde ‘kendi kendilerini yineleyen’,
veya daha teknik bir dille ifade etmek gerekirse ‘özyinelemeli’ (recursive) fonksiyonlar adı verilir.
"""


# def azalt(s):
#     if len(s) < 1:
#         return s
#     else:
#         print(list(s))
#         return azalt(s[1:])


# print(azalt('istihza'))


n = 0

def azalt(s):
    global n
    mesaj = '{} harfinin {}. çalışmadaki konumu: {}'
    if len(s) < 1:
        return s
    else:
        n += 1
        print(mesaj.format('a', n, s.index('a')))
        return azalt(s[1:])

azalt('istihza')




#"Python’da, fonksiyonlar programda kullanılan diğer bütün değerler gibi değerlendirilir (görülür). Bu da demek oluyor ki,
# bir fonksiyonu bir başka fonksiyona argüman olarak besleyebilirsiniz ya da bir fonksiyonun dış kapsama döndürdüğü (return) şey bir başka fonksiyon olabilir."



"""






>>> def outer():
...     def inner():
...         print "Inside inner"
...     return inner # 1
...
>>> foo = outer() #2
>>> foo # doctest:+ELLIPSIS
<function inner at 0x...>
>>> foo()
Inside inner

















"""