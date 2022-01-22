from django.contrib import admin
from . models import AddYourStartupArea

@admin.register(AddYourStartupArea)
class AddYourStartupAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}