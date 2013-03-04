from django.shortcuts import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages

from forms import ProfileForm
import simplejson


# Basic form handling
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
            p.startup_name = POST['startup_name'];
            p.startup_url = POST['startup_url'];
            p.role = POST['role']
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
    return render_to_response('profiles/signup.html', {'form': form}, context_instance=RequestContext(request))







# def thanks(request, first_name, last_name, email):
#     return render_to_response('profiles/thanks.html', {'first_name': first_name}, context_instance=RequestContext(request))



# def profile(request,username=None):
#     if not username:
#         if request.user.is_authenticated():
#             p = request.user.get_profile()
#             return render_to_response("profiles/profile.html",{"profile":p},context_instance=RequestContext(request))
#         else:
#             messages.error("You need to login first.")
#             return HttpResponseRedirect(reverse("home"))
#     else:
#         p = get_object_or_404(User,username=username).get_profile()
#         return render_to_response("profiles/profile.html",{"profile":p},context_instance=RequestContext(request))
