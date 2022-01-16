# x, y, z = 1, 2, 3

from typing import Union


x, y, z = 2, 5, 107

numbers = 1, 5, 7, 10, 6


"""for i in range(1):
    num1 = int(input("Enter once number: "))
    num2 = int(input("Enter second number: "))
    islem = num1 * num2 + (x+y+z)

print(islem)"""


div = y//x
print(div)

mod = (x+y+z)%3
print(mod)


c = y**x
print(c)

x, *y, z = numbers

print(sum(y))