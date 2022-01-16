from django.urls import path
from . import views
from django.views import generic
app_name = 'polls'
urlpatterns = [
    #ex: /pools/
    path('', views.IndexView.as_view(), name='index'),
    #ex: /polls/5
    # {% url %} şablon etiketiyle çağrılan 'name' değeri
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #ex: /polls/5/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #ex: /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),

]


