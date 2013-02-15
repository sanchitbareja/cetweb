from django.shortcuts import *
from django.contrib.auth.models import User

def profile(request,username):
    p = get_object_or_404(User,username=username).get_profile()
    return render_to_response("profiles/profile.html",{"profile":p},context_instance=RequestContext(request))
