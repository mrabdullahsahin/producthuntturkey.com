from django.db import models
from products.models import City
from django.utils.text import slugify
from datetime import datetime
from parler.models import TranslatableModel, TranslatedFields

STATUS_CHOICES = [
    ('w', 'İnceleme Bekliyor'),
    ('d', 'Yayınlandı'),
]

class Event(TranslatableModel):
    translations = TranslatedFields(
        event_description = models.TextField(blank=True, null=True),
    )

    event_name = models.CharField(max_length=350, blank=True, null=True)
    event_link = models.CharField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=500, unique=True, null=True)
    def get_filepath(instance, filename):
        fname, dot, extension = filename.rpartition('.')
        slug = instance.slug
        _now = datetime.now()
        file_name = '%s.%s' % (slug, extension)
        return 'events/{0}/{1}/{2}/{3}'.format(_now.strftime('%Y'),_now.strftime('%m'),_now.strftime('%d'),file_name)
    event_picture = models.ImageField(upload_to=get_filepath, default="default/producthuntturkey-logo.png", null=True, blank=True)
    event_city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True)
    event_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_avaliable = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='w')

    def __str__(self):
        return self.event_name

    def _get_unique_slug(self):
        slug = slugify(self.event_name)
        unique_slug = slug
        num = 1
        while Event.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
