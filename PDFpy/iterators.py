# liste = [1,2,3,4,5]
# iterator = iter(liste)

# print(next(iterator))



class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    
    def __iter__(self):
        return self
    

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        
        else:
            raise StopIteration
liste = MyNumbers(12,33)
print(list(liste))
# for x in liste:
#     print(x)