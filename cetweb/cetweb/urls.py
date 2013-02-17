from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', direct_to_template, {"template":"home.html"}, name='home'),
    url(r'^users/', include('profiles.urls')),
    url(r'^accounts/profile/', 'profiles.views.profile'),
    url(r'^company/', include('company.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^about/$', direct_to_template, {"template":"about.html"}, name='about'),
    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
