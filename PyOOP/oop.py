import datetime
class Person():
    def __init__(self, name, phone, bday):
        self.name = name
        self.phone = phone 
        self.bday = bday
    
    def CalculatedBday(self):
        result = 2021 - self.bday