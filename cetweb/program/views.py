#python
import json

#standard django stuff
from django.shortcuts import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

#project
from program.models import Program, Course
from program.forms import CertificateApplicationForm

def program_list(request):
    programs = Program.objects.all()
    certificate_form = CertificateApplicationForm()
    context = {
        "programs":programs,
        "certificate_form":certificate_form,
    }
    return render_to_response("staticpages/programs.html",context,context_instance=RequestContext(request))

def program_detail(request,pk):
    """
        Displays a course page.
    """
    p = get_object_or_404(Program,pk=pk)
    return render_to_response("program/program.html",{"program":p},context_instance=RequestContext(request))

def course_detail(request,pk):
    """
        Displays a course page.
    """
    c = get_object_or_404(Course,pk=pk)
    return render_to_response("program/course.html",{"course":c},context_instance=RequestContext(request))

@csrf_exempt
def program_certificate_apply(request):
    data = {"success": False,"message":"Please completely fill out the form."}
    if request.is_ajax():
        if request.method=="POST":
            form = CertificateApplicationForm(request.POST)
            if form.is_valid():
                form.save()
                data['success'] = True
                data['message'] = "Thanks! We will get back to you shortly."
            else:
                data['message'] = "Please correctly fill out the form."
    return HttpResponse(json.dumps(data), mimetype="application/json")
