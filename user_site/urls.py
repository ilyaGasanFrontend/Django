from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_articles/', views.show_articles, name='show_articles'),
]
