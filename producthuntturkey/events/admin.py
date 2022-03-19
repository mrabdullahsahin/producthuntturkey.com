from django.contrib import admin
from parler.admin import TranslatableAdmin
from . models import Event

class EventAdmin(TranslatableAdmin):
    list_display = ('event_name','event_city','is_avaliable')
    list_filter = ('is_avaliable','event_city')
    search_fields = ('event_name','event_city')
    prepopulated_fields = {'slug': ('event_name',)}

admin.site.register(Event, EventAdmin)