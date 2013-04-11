#standard django stuff
from django.shortcuts import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from info.forms import TestimonialForm
from info.models import Testimonial

def testimonial_create(request):
    form = TestimonialForm()
    if request.POST:
        form = TestimonialForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    context = {
        "form": form
    }
    return render_to_response("info/testimonial_create.html",context,context_instance=RequestContext(request))
