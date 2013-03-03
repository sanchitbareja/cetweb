from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('chatroom.views',
    url(r'^wall/$','chatroom_wall',name='chatroom_wall'),
)
