from django.shortcuts import render
from products.models import Product

def openpage(request):
    products_number = Product.objects.filter(is_avaliable=True).count()

    context = {
        'products_number': products_number
    }
    return render(request, 'open-startup.html', context)