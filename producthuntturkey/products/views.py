from django.shortcuts import render, get_object_or_404
from . models import Product, City

def index(request, product_slug=None, city_slug=None):
    if product_slug != None:
        product = Product.objects.get(slug = product_slug)

        context = {
            'product': product
        }

        return render(request, 'product-detail.html', context)

    elif city_slug != None:
        city_page = get_object_or_404(City, slug=city_slug)
        products = Product.objects.all().filter(is_avaliable=True, product_city = city_page).order_by('-product_launch_date')

        context = {
            'products': products
        }

        return render(request, 'city.html', context)

    else:
        products = Product.objects.filter(is_avaliable=True).order_by('-product_launch_date')

        context = {
            'products': products
        }

        return render(request, 'index.html', context)