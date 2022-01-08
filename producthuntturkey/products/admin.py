from django.contrib import admin
from . models import City, TeamSize

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('city',)}

@admin.register(TeamSize)
class TeamSize(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('size',)}