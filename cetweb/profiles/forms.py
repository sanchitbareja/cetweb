from django import forms
from profiles.models import Profile
from django.contrib.auth.models import User

from django.forms import ModelForm

import random
import string

class ProfileForm(ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    def save(self,commit=True):
        instance = super(ProfileForm,self).save(commit=commit)
        u = User()
        u.has_profile = True
        u.username = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(20))
        u.first_name = self.cleaned_data['first_name']
        u.last_name = self.cleaned_data['last_name']
        u.email = self.cleaned_data['email']
        u.save()
        for p in Profile.objects.filter(user=u):
            p.delete()
        instance.user = u
        instance.save()
        return instance
    class Meta:
        model = Profile
        exclude = ("user","steakholder","activated")
