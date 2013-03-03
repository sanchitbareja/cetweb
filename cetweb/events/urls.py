from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('events.views',
    url(r'^events/$', 'event_list', name="event_list"),
    url(r'^event/(?P<pk>[\w\d]+)/$', 'event', name="event"),
    url(r'^create/$', 'create_event', name="event_create"),
)
