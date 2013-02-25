#standard model stuff
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

from django_extensions.db.fields import AutoSlugField

class InfoImage(models.Model):
    image = models.ImageField(upload_to="about_images")

class AboutPage(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name")
    images = models.ManyToManyField(InfoImage)
    description = models.TextField()

    @models.permalink
    def get_absolute_url(self):
        return ('about', [self.pk])
