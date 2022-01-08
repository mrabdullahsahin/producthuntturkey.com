from django.db import models

class City(models.Model):
    city = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

class TeamSize(models.Model):
    size = models.CharField(max_length=15, null=True)
    slug = models.SlugField(max_length=15, unique=True, null=True)