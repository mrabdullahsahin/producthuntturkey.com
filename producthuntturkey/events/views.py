from django.shortcuts import render, get_object_or_404
from . models import Event
from products.models import City
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def show_event(request, event_slug=None, event_city_slug=None):
    if event_slug != None:
        event = Event.objects.get(slug = event_slug)

        context = {
            'event': event
        }

        return render(request, 'event-detail.html', context)

    elif event_city_slug != None:
        city_page = get_object_or_404(City, slug=event_city_slug)
        city = City.objects.get(slug=event_city_slug)
        events_list = Event.objects.all().filter(is_avaliable=True, event_city = city_page).order_by('-event_date').all()

        page = request.GET.get('page', 1)

        paginator = Paginator(events_list, 3)
        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            events = paginator.page(1)
        except EmptyPage:
            events = paginator.page(paginator.num_pages)         

        context = {
            'events': events,
            'city': city
        }

        return render(request, 'event-city.html', context)

    else:
        events_list = Event.objects.filter(is_avaliable=True).order_by('-event_date').all()
        page = request.GET.get('page', 1)

        paginator = Paginator(events_list, 3)
        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            events = paginator.page(1)
        except EmptyPage:
            events = paginator.page(paginator.num_pages)

        context = {
            'events': events
        }

        return render(request, 'events.html', context)