from django.contrib import admin
from django.contrib.admin.sites import site
from django.db.models.fields.related import RECURSIVE_RELATIONSHIP_CONSTANT
from .models import *





class AdminTeacher(admin.ModelAdmin):
    list_display = ('name','principal',)
admin.site.register(Teacher, AdminTeacher)

class AdminPrincipal(admin.ModelAdmin):
    pass
admin.site.register(Principal, AdminPrincipal)


class AdminStudent(admin.ModelAdmin):
    list_display = ('name','teacher','principal')

admin.site.register(Student,AdminStudent)

class AdminStudentClass(admin.ModelAdmin):
    list_display = ('studentClass', 'number_of_students')

admin.site.register(StudentClass, AdminStudentClass)