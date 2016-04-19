from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length = 200)
    event_date = models.DateField('date of the event')
    time_start = models.TimeField('start time of the event')
    time_end = models.TimeField('end time of the event')
    description = models.TextField()

    def __unicode__(self):
        return "%s is on %s from %s to %s" % (self.name, self.event_date, self.time_start, self.time_end)

class SubEvent(models.Model):
    name = models.CharField(max_length = 200)
    time_start = models.TimeField('start time of the subevent')
    duration = models.IntegerField('number of minutes for the subevent slot')
    description = models.TextField()
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    assignee = models.CharField(max_length=150, default='x')

    def __unicode__(self):
        return "%s, a subevent of %s is at %s for %s minutes" % (self.name, self.event_id, self.time_start, self.duration)
