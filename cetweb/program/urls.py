from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('program.views',
    url(r'^program/(?P<pk>[\w\d]+)/$', 'program_detail', name="program_detail"),
    url(r'^programs/$', 'program_list', name="program_list"),
    url(r'^course/(?P<pk>[\w\d]+)/$', 'course_detail', name="course_detail"),
)
