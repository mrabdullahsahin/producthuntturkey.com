from django.urls import path
from . import views

urlpatterns = [
    path('add-your-startup', views.addyourstartup, name='add-your-startup'),
    path('add-your-future-startup', views.addyourfuturestartup, name="add-your-future-startup")
]