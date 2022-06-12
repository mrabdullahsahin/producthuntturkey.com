import environ
import requests
from datetime import datetime, date
from django.contrib import admin
from parler.admin import TranslatableAdmin
from . models import City, TeamSize, Product

env = environ.Env()
environ.Env.read_env()

@admin.action(description='Telegram Kanalında Yayınla')
def send_to_telegram(self, request, queryset):
    for product in queryset:
        if product.is_avaliable:
            if product.is_published_telegram == False:
                if product.product_launch_date == datetime.today().date():
                    product.set_current_language('en')
                    product_about_en = product.product_description
                    product.set_current_language('tr')
                    product_about_tr = product.product_description
                    product_info_tr = "Bugünün Product Hunt Girişimi\n\n{}\n\n{}\n https://producthuntturkey.com/tr/product/{}".format(product_about_tr, product.product_ph_link, product.slug)
                    url = 'https://api.telegram.org/bot'+ env("TELEGRAM_GENERAL_BOT_API") +'/sendMessage'

                    data = {
                        'chat_id': env("TELEGRAM_GENERAL_CHAT_ID"), 
                        'text': product_info_tr
                    }
                
                    requests.post(url, data)
                    product.is_published_telegram = True
                    product.save()
                    self.message_user(
                        request,"Ürün telegram kanalında başarılı bir şekilde paylaşıldı.",
                    )
                elif product.product_launch_date < datetime.today().date():
                    self.message_user(
                        request,"Launch tarihi bugünün tarihinden önce olduğu için bu ürünü telegram kanalında yayınlayamazsınız.",
                    )
                elif product.product_launch_date > datetime.today().date():
                    self.message_user(
                        request,"Ürünün launch tarihi ileri bir tarih olduğu için şu an bu ürünü telegram kanalında yayınlayamazsınız.",
                    )
                else:
                    self.message_user(
                        request,"Ürün telegram kanalında yayınlanamaz.",
                    )
            else:
                self.message_user(
                    request,"Telegramda yayınlanmış bir ürünü tekrar yayınlayamazsınız."
                )
        else:
            self.message_user(
                request,"Bu ürünü telegramda yayınlayabilmek için önce onaylamanız gerekmektedir."
            )

@admin.action(description='Ürünü Onayla')
def accept_to_product(self, request, queryset):
    for product in queryset:
        if product.is_avaliable == False:
            product.is_avaliable = True
            product.save()
            self.message_user(
                request,"Ürün başarılı bir şekilde onaylandı.",
            )
        else:
            self.message_user(
                request,"Ürün onaylanamadı.",
            )

@admin.action(description='Ürünün Onayını Kaldır')
def unaccept_to_product(self, request, queryset):
    for product in queryset:
        if product.is_avaliable:
            product.is_avaliable = False
            product.save()
            self.message_user(
                request,"Ürünün onayı başarılı bir şekilde kaldırıldı.",
            )
        else:
            self.message_user(
                request,"Ürünün onayı kaldırılamadı.",
            )

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('city',)}

@admin.register(TeamSize)
class TeamSize(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('size',)}

class ProductAdmin(TranslatableAdmin):
    list_display = ('product_name', 'slug', 'product_city','is_avaliable','is_published_telegram','is_published_mail','product_launch_date')
    list_filter = ('is_avaliable','product_city','product_team_size')
    search_fields = ('product_name','product_description')
    prepopulated_fields = {'slug': ('product_name',)}
    actions = [send_to_telegram,accept_to_product,unaccept_to_product]

admin.site.register(Product, ProductAdmin)