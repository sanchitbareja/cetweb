from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('splash.views',
    url(r'^add_email/$', 'add_email', name="add_email"),
    url(r'^thanks/$', direct_to_template, {"template":"splash/thanks.html"}, name='thanks'),
)
