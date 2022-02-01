from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class City(models.Model):
    city = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.city

class TeamSize(models.Model):
    size = models.CharField(max_length=15, null=True)
    slug = models.SlugField(max_length=15, unique=True, null=True)

    def __str__(self):
        return self.size

class Product(TranslatableModel):
    translations = TranslatedFields(
        product_description = models.TextField(blank=True, null=True),
        product_launch_date = models.DateField(),
    )

    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    product_picture = models.ImageField(upload_to="products/%Y/%m/%d/", default="default/producthuntturkey-logo.png")
    product_city = models.ForeignKey(City, blank=True, null=True, on_delete=models.DO_NOTHING)
    product_ph_link = models.CharField(max_length=250)
    product_website = models.CharField(max_length=250, blank=True, null=True)
    product_team_size = models.ForeignKey(TeamSize, blank=True, null=True, on_delete=models.DO_NOTHING)
    product_twitter = models.CharField(max_length=250, blank=True, null=True)
    product_owner_twitter = models.CharField(max_length=250, blank=True, null=True)
    product_hunt_votes = models.CharField(max_length=6, default=0, blank=True, null=True)
    is_published_telegram = models.BooleanField(default=False)
    is_published_twitter = models.BooleanField(default=False)
    is_published_mail = models.BooleanField(default=False)
    is_published_linkedin = models.BooleanField(default=False)
    is_avaliable = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name