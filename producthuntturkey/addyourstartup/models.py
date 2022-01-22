from django.db import models
from products.models import City, TeamSize

class AddYourStartupArea(models.Model):
    def get_filepath(self, instance, filename):
        fname, dot, extension = filename.rpartition('.')
        filename = '%s.%s' % (self.slug, extension)
        return 'products/%Y/%m/%d/{}'.format(filename)

    product_name = models.CharField(max_length=250, null=True, blank=True)
    product_about_tr = models.TextField(null=True, blank=True)
    product_about_en = models.TextField(null=True, blank=True)
    product_twitter = models.CharField(max_length=250, null=True, blank=True)
    product_owner_twitter = models.CharField(max_length=250, null=True, blank=True)
    product_ph_link = models.CharField(max_length=250, null=True, blank=True)
    product_website = models.CharField(max_length=250, null=True, blank=True)
    product_launch_date = models.DateField(auto_now=True, null=True, blank=True)
    product_team_size = models.ForeignKey(TeamSize, on_delete=models.DO_NOTHING, null=True, blank=True)
    product_picture = models.ImageField(upload_to=get_filepath, default="default/producthuntturkey-logo.png", null=True, blank=True)
    product_city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name