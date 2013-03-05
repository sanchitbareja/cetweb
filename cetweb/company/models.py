#standard model stuff
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Company(models.Model):
    name = models.CharField(max_length=100)
    founders = models.ManyToManyField(User,blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to="company_images",null=True,blank=True)
    pitch = models.TextField(default="",blank=True)
    video = models.URLField(null=True,blank=True,verbose_name="Video to pitch your idea")
    milestones = models.CharField(max_length=500, blank=True)
    investors = models.CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.name
    @models.permalink
    def get_absolute_url(self):
        return ('company_profile', [self.pk])
    
admin.site.register(Company)

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company)
    requests = models.ManyToManyField(User,blank=True,verbose_name="People who are interested in the job.")

    available = models.BooleanField(default=True,verbose_name="Is this job still available?")
    description = models.TextField()

    def __unicode__(self):
        return str(self.company) + ": " + self.title
    @models.permalink
    def get_absolute_url(self):
        return ('job_listing', [self.pk])

admin.site.register(Job)
