#standard django stuff
from django.shortcuts import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#project
from events.models import Event
from events.forms import EventForm

def event_list(request):
    """
        Displays the job listings.
    """
    events = Event.objects.all()
    return render_to_response("events/event_list.html",{"events":events},context_instance=RequestContext(request))

def event(request,pk):
    """
        Displays a job listing.
    """
    e = get_object_or_404(Event,pk=pk)
    return render_to_response("events/event.html",{"event":e},context_instance=RequestContext(request))

@login_required
def create_event(request):
    """
        Creates an event.
    """
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            event = form.save()
            return HttpResponseRedirect(reverse("event",args=(event.pk,)))
    return render_to_response("events/event_form.html",{"form":form},context_instance=RequestContext(request))
