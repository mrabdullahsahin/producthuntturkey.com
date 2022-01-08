from django.db import models

class City(models.Model):
    city = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)