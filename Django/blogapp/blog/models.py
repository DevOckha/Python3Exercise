from django.db import models
from django.db.models.base import Model
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(null=False, unique=True, db_index=True, editable=False)
    
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)



    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(blank=True ,unique=True, db_index=True)
    categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.title


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

