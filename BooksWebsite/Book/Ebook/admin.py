from django.contrib import admin
from .models import Category, Book


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('name','brodcasting', 'price', 'category')

admin.site.register(Book, BookAdmin)