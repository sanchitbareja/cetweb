#standard django stuff
from django.shortcuts import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#project
from events.models import Event

def home(request):
    """
        Displays the job listings.
    """
    events = Event.objects.all()
    return render_to_response("home.html",{"events":events},context_instance=RequestContext(request))