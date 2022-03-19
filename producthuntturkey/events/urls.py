from django.urls import path
from . import views

urlpatterns = [
    path('events', views.show_event, name='show-event'),
]