from django.conf.urls import url
from django.urls.conf import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

]
