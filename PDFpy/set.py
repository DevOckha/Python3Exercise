fruits = {'orange', 'apple', 'banana'}

#print(fruits[0]) indekslenemez

#for i in fruits:
    #print(i)

fruits.add('cherry') #eleman ekleme
fruits.update(['mango', 'grape', 'apple'])
print(fruits)
#listeler içerisinde bir elemenadan birden fazla yazılamaz

fruits.remove('mango')#elemana silme
fruits.discard('apple')

fruits.pop()# liste sıralanmadığı için herhangi bir eleman silinir.

fruits.clear()# bütün elemanları siler