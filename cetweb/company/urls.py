from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('company.views',
	url(r'^$', 'company_list' , name='company_list'),
	url(r'^mentors/$', 'mentor_list' , name='mentor_list'),
    url(r'^profile/(?P<pk>[\w\d]+)/$', 'profile', name="company_profile"),
    url(r'^profile/create/$', 'create_company', name="company_create"),
    url(r'^profile/edit/(?P<pk>[\w\d]+)/$', 'edit_company', name="company_edit"),
    url(r'^job/listings/(?P<pk>[\w\d]+)/$', 'job_listing', name="job_listing"),
    url(r'^job/all/$', 'job_listing_list', name="job_listing_list"),
    url(r'^job/create/$', 'create_job', name="job_create"),
    url(r'^job/create/(?P<company_pk>[\w\d]+)/$', 'create_job', name="job_create"),
)
