from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('profiles.views',
    url(r'^signup/$', 'signup', name='signup'),
    url(r'^thanks/$', 'signup_helper'),

    url(r'^dashboard/$', 'dashboard',name='dashboard'),
)
