from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import TextField

class Company(models.Model):
    name = models.CharField(verbose_name='isim', max_length=120)
    content = models.TextField(verbose_name='açıklama')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True




class BookCompany(Company):
    pass

class GameCompany(Company):
    pass