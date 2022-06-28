from django.db import models
from products.models import City, TeamSize
from django.utils.text import slugify
from datetime import datetime

STATUS_CHOICES = [
    ('w', 'İnceleme Bekliyor'),
    ('p', 'Product Tablosuna Eklendi'),
    ('d', 'Yayınlama'),
]
class AddYourStartupArea(models.Model):
    product_name = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True, null=True)
    product_about_tr = models.TextField(null=True, blank=True)
    product_about_en = models.TextField(null=True, blank=True)
    product_twitter = models.CharField(max_length=250, null=True, blank=True)
    product_owner_twitter = models.CharField(max_length=250, null=True, blank=True)
    product_ph_link = models.CharField(max_length=250, null=True, blank=True)
    product_website = models.CharField(max_length=250, null=True, blank=True)
    product_launch_date = models.DateField(null=True, blank=True)
    product_future_launch_date = models.DateField(null=True, blank=True)
    product_team_size = models.ForeignKey(TeamSize, on_delete=models.DO_NOTHING, null=True, blank=True)
    def get_filepath(instance, filename):
        fname, dot, extension = filename.rpartition('.')
        slug = instance.slug
        _now = datetime.now()
        file_name = '%s.%s' % (slug, extension)
        return 'products/{0}/{1}/{2}/{3}'.format(_now.strftime('%Y'),_now.strftime('%m'),_now.strftime('%d'),file_name)
    product_picture = models.ImageField(upload_to=get_filepath, default="default/producthuntturkey-logo.png", null=True, blank=True)
    product_city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='w')

    def __str__(self):
        return self.product_name

    def _get_unique_slug(self):
        slug = slugify(self.product_name)
        unique_slug = slug
        num = 1
        while AddYourStartupArea.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)