#standard django stuff
from django.shortcuts import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from splash.models import SplashEmail
from splash.forms import SplashEmailForm

def add_email(request):
    if request.method == "POST":
       form = SplashEmailForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse("thanks"))
    return HttpResponseRedirect(reverse("splash"))
        
