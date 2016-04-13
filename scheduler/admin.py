from django.contrib import admin
from scheduler.models import Event, SubEvent

# Register your models here.
admin.site.register(Event)
admin.site.register(SubEvent)