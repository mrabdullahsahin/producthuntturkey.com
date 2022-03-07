from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:product_slug>', views.index, name='product_detail'),
    path('city/<slug:city_slug>', views.index, name='city-list'),
    path('team-size/<slug:teamsize_slug>', views.index, name='team-size-list'),
    path('privacy-policy', views.privacy_policy, name='privacy-policy'),
    path('terms-of-service', views.terms_of_service, name='terms-of-service'),
]