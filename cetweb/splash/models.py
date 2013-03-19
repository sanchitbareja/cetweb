from django.db import models
from django.contrib import admin

from django_extensions.db.fields import CreationDateTimeField

class SplashEmail(models.Model):
    email = models.EmailField()
    datetime = CreationDateTimeField()
    def __unicode__(self):
        return self.email

admin.site.register(SplashEmail)
