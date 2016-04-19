__author__ = 'Jake'
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<event_id>\d+)/$', views.event, name='event'),
    url(r'^assign/$', views.assign, name='assign'),
]