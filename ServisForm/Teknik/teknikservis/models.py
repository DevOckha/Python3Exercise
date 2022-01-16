from django.db import models
from django.utils import timezone

# Create your models here.

class Teknisyen(models.Model):
    Aktif = models.BooleanField(default=1)
    AdSoyad = models.CharField(u'Adı Soyadı', max_length=255)
    KayitTarihi = models.DateField(u'Kayıt Tarihi', default=timezone.now)
    

    def __str__(self):
        return self.AdSoyad

    

    class Meta:
        verbose_name_plural = u'Teknisyenler'
        verbose_name = u'Teknisyen'


    def Yazdir (self) :
        return '<a href="/yazdir/%s" target="_blank">Yazdır</a>' % self.id
        ### Fonksiyon çağrıldığında döndürülecek metin.
        Yazdir.short_description = u'Yazdır'
        ### Fonksiyonun kısa açıklaması
        Yazdir.allow_tags = True
        ### Fonksiyonumuz html etiket içeriyor