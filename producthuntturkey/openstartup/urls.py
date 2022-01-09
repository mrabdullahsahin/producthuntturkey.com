from django.urls import path
from . import views

urlpatterns = [
    path('open-startup', views.openpage, name='open-startup'),
]