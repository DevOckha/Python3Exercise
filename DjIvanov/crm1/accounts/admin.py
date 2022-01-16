from django.contrib import admin
from django.db.utils import DJANGO_VERSION_PICKLE_KEY
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)

