#standard django stuff
from django.shortcuts import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#messages
from django.contrib import messages

from splash.models import SplashEmail
from splash.forms import SplashEmailForm

def add_email(request):
    form = SplashEmailForm()
    if request.method == "POST":
        form = SplashEmailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("thanks"))
        else:
            messages.add_message(request, messages.ERROR, 'Please enter a valid email.')
    return HttpResponseRedirect(reverse("splash"))
        
