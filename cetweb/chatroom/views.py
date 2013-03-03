#standard django stuff
from django.shortcuts import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def chatroom_wall(request):
    return render_to_response("chatroom/chatroom_wall.html",{},context_instance=RequestContext(request))
