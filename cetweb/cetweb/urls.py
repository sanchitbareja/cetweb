from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', direct_to_template, {"template":"home.html"}, name='home'),
    url(r'^users/', include('profiles.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^about/$', direct_to_template, {"template":"about.html"}, name='about'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
