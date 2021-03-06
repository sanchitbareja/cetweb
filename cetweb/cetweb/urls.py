from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template, redirect_to
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

#project
from cetweb.views import home

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', direct_to_template, {"template":"splash.html"}, name='splash'),
    url(r'^$', home, name='home'),
    url(r'^home/', home, name='home'),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^company/', include('company.urls')),
    url(r'^splash/', include('splash.urls')),
    url(r'^program/', include('program.urls')),
    url(r'^chatroom/', include('chatroom.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^info/', include('info.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/profile/$', redirect_to, {'url': '/profiles/dashboard/'}),
    url(r'^about/$', direct_to_template, {"template":"about.html"}, name='about'),
    url(r'^donate/$', direct_to_template, {"template":"donate.html"}, name='donate'),
    url(r'^faq/$', direct_to_template, {"template":"faq.html"}, name='faq'),
    url(r'^contact/$', direct_to_template, {"template":"contact.html"}, name='contact'),
    url(r'^globalprograms/$', direct_to_template, {"template":"globalprograms.html"}, name='about'),
    url(r'^apply/$', direct_to_template, {"template":"program/apply_reveal.html"}, name='apply'),
    url(r'^comments/', include('django.contrib.comments.urls')),

    # ERROR PAGES
    url(r'^construction/$', direct_to_template, {"template":"errors/construction.html"}, name='construction'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
