from django.contrib import admin
from . models import AddYourStartupArea
from products.models import Product

@admin.action(description='Product Tablosuna Ekle')
def add_to_product_table(self, request, queryset):
    for startup in queryset:
        product = Product()
        product.product_name = startup.product_name
        product.slug = startup.slug
        product.product_twitter = startup.product_twitter
        product.product_owner_twitter = startup.product_owner_twitter
        product.product_ph_link = startup.product_ph_link
        product.product_website = startup.product_website
        product.product_launch_date = startup.product_launch_date
        product.product_team_size = startup.product_team_size
        product.product_picture = startup.product_picture
        product.product_city = startup.product_city
        product.set_current_language('en')
        product.product_description = startup.product_about_en
        product.set_current_language('tr')
        product.product_description = startup.product_about_tr
        product.save()
        startup.status = 'p'
        startup.save()
        self.message_user(
            request,"Product tablosuna kayıt başarıyla gerçekleştirildi.",
        )

@admin.register(AddYourStartupArea)
class AddYourStartupAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ['product_name', 'status']
    actions = [add_to_product_table]