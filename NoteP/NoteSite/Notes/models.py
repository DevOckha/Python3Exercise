from django.db import models
from django.db.models.deletion import PROTECT


class Principal(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self) -> str:
        return self.name


class Teacher(models.Model):
    principal = models.ForeignKey(Principal, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=120)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    principal = models.ForeignKey(Principal, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name


class StudentClass(models.Model):
    number_of_students = models.PositiveIntegerField()
    Classes = (
        ('M', 'Math'),
        ('C', 'Chemistry'),
        ('P', 'Picture'),
    )
    studentClass = models.CharField(max_length=1, choices=Classes)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    