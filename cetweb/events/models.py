#standard model stuff
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=100,default="CET Berkeley")
    image = models.ImageField(upload_to="event_images",null=True,blank=True)
    cet = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name
    def google_date_range(self):
        def convert_datetime(dt):
            d = dt.date()
            d_s = d.strftime("%Y%m%d")
            t = dt.time()
            t_s = t.strftime("%H%M%S")
            return d_s + "T" + t_s + "Z" 
        return convert_datetime(self.start_time) + "/" + convert_datetime(self.end_time)
    class Meta:
        ordering = ['-start_time']

admin.site.register(Event)
