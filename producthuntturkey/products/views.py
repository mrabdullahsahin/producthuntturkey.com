from django.shortcuts import render
from . models import Product

def index(request, product_slug=None):
    if product_slug != None:
        product = Product.objects.get(slug = product_slug)

        context = {
            'product': product
        }

        return render(request, 'product-detail.html', context)

    else:
        products = Product.objects.filter(is_avaliable=True).order_by('-product_launch_date')

        context = {
            'products': products
        }

        return render(request, 'index.html', context)