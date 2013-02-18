from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib import messages

def profile(request,username=None):
    if not username:
        if request.user.is_authenticated():
            p = request.user.get_profile()
            return render_to_response("profiles/profile.html",{"profile":p},context_instance=RequestContext(request))
        else:
            messages.error("You need to login first.")
            return HttpResponseRedirect(reverse("home"))
    else:
        p = get_object_or_404(User,username=username).get_profile()
        return render_to_response("profiles/profile.html",{"profile":p},context_instance=RequestContext(request))
