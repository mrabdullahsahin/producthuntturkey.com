from django.shortcuts import render, get_object_or_404
from . models import Product, City, TeamSize

def index(request, product_slug=None, city_slug=None, teamsize_slug=None):
    if product_slug != None:
        product = Product.objects.get(slug = product_slug)

        context = {
            'product': product
        }

        return render(request, 'product-detail.html', context)

    elif city_slug != None:
        city_page = get_object_or_404(City, slug=city_slug)
        city =  City.objects.get(slug=city_slug)
        products = Product.objects.all().filter(is_avaliable=True, product_city = city_page).order_by('-product_launch_date')

        context = {
            'products': products,
            'city': city
        }

        return render(request, 'city.html', context)

    elif teamsize_slug != None:
        team_page = get_object_or_404(TeamSize, slug=teamsize_slug)
        team_size =  TeamSize.objects.get(slug=teamsize_slug)
        products = Product.objects.all().filter(is_avaliable=True, product_team_size = team_page).order_by('-product_launch_date')

        context = {
            'products': products,
            'teamsize': team_size
        }

        return render(request, 'team-size.html', context)

    else:
        products = Product.objects.filter(is_avaliable=True).order_by('-product_launch_date')

        context = {
            'products': products
        }

        return render(request, 'index.html', context)