from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date',)
    list_display_links = ('created_date','name',)

admin.site.register(Movie, MovieAdmin)

