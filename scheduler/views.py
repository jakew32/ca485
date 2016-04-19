from django.shortcuts import render, redirect
from django.http import HttpResponse
from scheduler.models import Event, SubEvent

# Create your views here.

def index(request):
    latest_event_list = Event.objects.order_by('event_date')
    context = {'latest_event_list': latest_event_list}
    return render(request, 'scheduler/index.html', context)

def event(request, event_id):
    event = Event.objects.get(pk=event_id)
    subevent_list = SubEvent.objects.filter(event_id=event_id).order_by('time_start')
    context = {'subevent_list': subevent_list, 'event': event}
    return render(request, 'scheduler/event.html', context)

def assign(request):
    event = Event.objects.get(pk=request.POST['event'])
    subevent = SubEvent.objects.get(pk=request.POST['subevent'])
    new_assignee = request.POST['assignee']
    subevent.assignee = new_assignee
    subevent.save()
    return redirect('event', event_id = event.pk)
