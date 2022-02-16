from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:product_slug>', views.product_detail, name='product_detail'),
]