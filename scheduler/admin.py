from django.contrib import admin
from scheduler.models import Event, SubEvent

# Register your models here.
class SubEventInline(admin.TabularInline):
    model = SubEvent
    extra = 1


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description']}),
        ('Date information', {'fields': ['event_date', 'time_start', 'time_end']}),
    ]
    inlines = [SubEventInline]

admin.site.register(Event, EventAdmin)