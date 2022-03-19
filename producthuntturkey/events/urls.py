from django.urls import path
from . import views

urlpatterns = [
    path('events', views.show_event, name='show-event'),
    path('event/<slug:event_slug>', views.show_event, name='event-detail'),
    path('events/city/<slug:event_city_slug>', views.show_event, name='events-city-list'),
]