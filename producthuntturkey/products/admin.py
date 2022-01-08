from django.contrib import admin
from . models import City, TeamSize, Product

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('city',)}

@admin.register(TeamSize)
class TeamSize(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('size',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('is_avaliable','product_city','product_team_size')
    search_fields = ('product_name','product_description')