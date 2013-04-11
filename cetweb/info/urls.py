from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('info.views',
    url(r'^testimonial/create/$', 'testimonial_create', name="testimonial_create"),
)
