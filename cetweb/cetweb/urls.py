from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', direct_to_template, {"template":"home.html"}, name='home'),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^company/', include('company.urls')),
    url(r'^program/', include('program.urls')),
    url(r'^chatroom/', include('chatroom.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^about/$', direct_to_template, {"template":"staticpages/about.html"}, name='about'),
    url(r'^globalprograms/$', direct_to_template, {"template":"staticpages/globalprograms.html"}, name='about'),
    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
