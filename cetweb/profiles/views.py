from django.shortcuts import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import simplejson

from forms import ProfileForm
from company.models import Company, Mentor, Investor



# def signup(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             email = form.cleaned_data['email']
#             user = User.objects.create_user(first_name, last_name, email)
#             p = user.get_profile()
#             p.stakeholder = form.cleaned_data['stakeholder']
#             if p.stakeholder == "founder":
#                 p.startup_name = form.cleaned_data['startup_name'];
#                 p.startup_url = form.cleaned_data['startup_url'];
#                 p.role = form.cleaned_data['role']
#             elif p.stakeholder == "mentor":
#                 p.industries = form.cleaned_data['industries'];
#             elif p.stakeholder == "faculty":
#                 p.department = form.cleaned_data['department'];
#             p.save()
#             # return HttpResponseRedirect(reverse('/thanks'), {'first_name':first_name, 'last_name':last_name, email:'email'})
#     else:
#         form = ProfileForm() # An unbound form
#     return render_to_response('profiles/signup.html', {'form': form}, context_instance=RequestContext(request))



def signup_helper(request):
    results = {'success':False}
    if (request.method == 'POST'):
        POST = request.POST
        first_name = POST['first_name']
        last_name = POST['last_name']
        email = POST['email']
        user = User.objects.create_user(first_name, last_name, email)
        p = user.get_profile()
        p.stakeholder = POST['stakeholder']
        if p.stakeholder == "founder":
            name = POST['name'];
            url = POST['url'];
            p.role = POST['role']
            c = Company.objects.create(name=name, url=url)
            c.founders.add(p.user)
            p.company = c
        elif p.stakeholder == "mentor":
            p.industries = POST['industries'];
        elif p.stakeholder == "faculty":
            p.department = POST['department'];
        p.save()
        results['success'] = True
    json_results = simplejson.dumps(results)
    return HttpResponse(json_results, mimetype='application/json')


def signup(request):
    form = ProfileForm()
    print form
    if request.method=="POST":
        print request.POST
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            print form.errors
    return render_to_response('profiles/signup.html', {'form': form}, context_instance=RequestContext(request))


#@login_required
def dashboard(request):
    context = {
        "mentors": Mentor.objects.all(),
        "investors": Investor.objects.all(),
    }
    return render_to_response('profiles/dashboard.html', context, context_instance=RequestContext(request))






