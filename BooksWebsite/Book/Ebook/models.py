from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=120)
    brodcasting = models.CharField(max_length=120)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self) -> str:
        return self.name