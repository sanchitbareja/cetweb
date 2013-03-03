#standard model stuff
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="event_images",null=True,blank=True)
    def __unicode__(self):
        return self.name

admin.site.register(Event)
