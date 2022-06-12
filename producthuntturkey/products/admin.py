from django.contrib import admin
from parler.admin import TranslatableAdmin
from . models import City, TeamSize, Product

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('city',)}

@admin.register(TeamSize)
class TeamSize(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('size',)}

class ProductAdmin(TranslatableAdmin):
    list_display = ('product_name', 'slug', 'product_city','is_avaliable','is_published_telegram')
    list_filter = ('is_avaliable','product_city','product_team_size')
    search_fields = ('product_name','product_description')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)