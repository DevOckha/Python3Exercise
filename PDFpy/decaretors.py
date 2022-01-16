def my_decorator(func):
    def wrapper():
        print('fonksiyondan önceki işlemler')
        func()
        print('fonksiyondan önceki işlemler ')
    return wrapper


@my_decorator
def sayHello():
    print('hello')