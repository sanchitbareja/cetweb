#standard model stuff
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="program_images",null=True,blank=True)
    @models.permalink
    def get_absolute_url(self):
        return ('program_detail', [self.pk])
    def __unicode__(self):
        return self.name
admin.site.register(Program)

class Course(models.Model):
    program = models.ForeignKey(Program)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="program_images",null=True,blank=True)
    @models.permalink
    def get_absolute_url(self):
        return ('course_detail', [self.pk])
    def __unicode__(self):
        return str(self.program) + ": " + self.name
admin.site.register(Course)
