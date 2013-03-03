#standard model stuff
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

#signals
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User)
    stakeholder = models.CharField(max_length=50,choices=settings.STAKEHOLDERS,default=settings.STAKEHOLDER_DEFAULT)
    image = models.ImageField(upload_to="profile_images",null=True,blank=True)

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    """
        Creates a Profile model for each User that is created.

        This function is called on the post_save signal from User.
    """
    if created:
        p = Profile.objects.create(user=instance)
admin.site.register(Profile)
