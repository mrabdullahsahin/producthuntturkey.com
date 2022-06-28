import environ
import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import AddYourStartupForm

env = environ.Env()
environ.Env.read_env()

def addyourstartup(request):
    form = AddYourStartupForm()

    if request.method == "POST":
        form = AddYourStartupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            product_info = "Ürünün Adı: {}\n Ürünün Product Hunt Linki: {}\n Ürünün Websitesinin Linki: {}\n Ürünün Product Hunt Yayınlanma Tarihi: {}\n Ürünün Twitter Kullanıcı Adı: {}\n Ürün Geliştiricisinin Twitter Kullanıcı Adı: {}\n Ürünün Takım Büyüklüğü: {}\n Ürünün Geliştirildiği Şehir: {}\n Ürünün Türkçe Açıklaması: {}\n Ürünün İngilizce Açıklaması: {}\n".format(form.instance.product_name, form.instance.product_ph_link, form.instance.product_website, form.instance.product_launch_date, form.instance.product_twitter, form.instance.product_owner_twitter, form.instance.product_team_size, form.instance.product_city, form.instance.product_about_tr, form.instance.product_about_en)

            url = 'https://api.telegram.org/bot'+ env("TELEGRAM_ADMIN_BOT_API") +'/sendMessage'

            data = {
                'chat_id': env("TELEGRAM_ADMIN_CHAT_ID"), 
                'text': product_info
            }
        
            requests.post(url, data)
            messages.success(request, "Your product was successfully submitted!")
            return redirect('add-your-startup')
        else:
            context = {
                'form': form
            }

            return render(request, 'add-your-startup.html', context)
    else:
        context = {
            'form': form
        }

        return render(request, 'add-your-startup.html', context)

    context = {
        'form': form
    }
    
    return render(request, 'add-your-startup.html', context)