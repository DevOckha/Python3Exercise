from django.db import models



class Principal(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    principal = models.ManyToManyField(Principal,)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    principal = models.ForeignKey(Principal, on_delete=models.CASCADE)
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.first_name, self.last_name}"


class HomeWork():
    pass