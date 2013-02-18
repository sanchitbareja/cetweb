#standard django stuff
from django.shortcuts import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#project
from program.models import Program, Course

def program_list(request):
    programs = Program.objects.all()
    return render_to_response("program/programs.html",{"programs":programs},context_instance=RequestContext(request))

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
