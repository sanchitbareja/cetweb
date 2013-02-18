from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('profiles.views',
    url(r'^(?P<username>[\w\d]+)/$', 'profile', name="user_profile"),
)
