from django.contrib import admin
from django.db.models.base import Model
from .models import *


class StudentAdmin(admin.ModelAdmin):
    list_display = ( 'teachers','principal',)
admin.site.register(Student, StudentAdmin)


class AdminPrincipal(admin.ModelAdmin):
    #list_display = ('first_name','last_name')
    pass
admin.site.register(Principal, AdminPrincipal)


class AdminTeacher(admin.ModelAdmin):
    #list_display = ('first_name','last_name')
    pass
admin.site.register(Teacher,AdminTeacher)
