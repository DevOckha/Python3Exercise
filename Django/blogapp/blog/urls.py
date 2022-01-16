from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, ),
    path('blogs', views.blogs, name='blogs'),
    path('blogs/<slug:slug>', views.blogs_details, name='blogs_details'),
]