#standard django stuff
from django.shortcuts import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#project
from events.models import Event
from info.models import Testimonial

def home(request):
    """
        Displays the job listings.
    """
    context = {
        "events": Event.objects.all(),
        "testimonials": Testimonial.objects.all()
    }
    return render_to_response("home.html",context,context_instance=RequestContext(request))
