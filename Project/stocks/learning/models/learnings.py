from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
class Product(models.Model):
    name = models.CharField(max_length=120, verbose_name='ürün ismi')
    content = models.TextField(verbose_name='ürün açıklaması', max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    stock_count = models.PositiveSmallIntegerField(verbose_name='stok_adedi')
    price = models.DecimalField(verbose_name='ürün fiyatı', decimal_places=2, max_digits=10)
    slug = models.SlugField(unique=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'urunler'

    def __str__(self) -> str:
        return self.name

    
    def get_absolute_url(self):
        return '/learning/product/detail/%i' % self.id

 
    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
            
        super(Product, self).save()
