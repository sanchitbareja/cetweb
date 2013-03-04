from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
# from profiles.views import signup_helper

urlpatterns = patterns('profiles.views',
    url(r'^signup/$', 'signup', name='signup'),
    url(r'^thanks/$', 'signup_helper'),
)