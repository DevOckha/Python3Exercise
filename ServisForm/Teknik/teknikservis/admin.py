from django.contrib import admin

# Register your models here.
### models.py dosyamızdaki Teknisyen ( class - sınıf ) tablomuzu ve alanları ekliyoruz.
from teknikservis.models import Teknisyen

class TeknisyenAdmin(admin.ModelAdmin):
    ### Admin sayfasında gösterilecek detaylar
    list_display = ['Aktif', 'AdSoyad', 'Yazdir']

    ### Admin sayfasında gösterilecek detaylar
    list_display = ('Aktif', 'AdSoyad')
    ### sırayla gösterilecek alanlar
    list_per_page = 20
    ### sayfadaki kayıt adeti, otomatik sayfalama yapacak
    exclude = ( 'KayitTarihi', )
    ### KayitTarihi alanını gizliyoruz
admin.site.register(Teknisyen, TeknisyenAdmin)
### Teknisyen ve TeknisyenAdmin sınıflarını kayıt ettiriyoruz


    