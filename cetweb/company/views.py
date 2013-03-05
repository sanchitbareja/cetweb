#standard django stuff
from django.shortcuts import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#project
from company.models import Company, Job
from company.forms import CompanyForm, JobForm

def profile(request,pk):
    """
        Displays a company profile page.
    """
    c = get_object_or_404(Company,pk=pk)
    return render_to_response("company/profile.html",{"company":c},context_instance=RequestContext(request))

def job_listing(request,pk):
    """
        Displays a job listing.
    """
    j = get_object_or_404(Job,pk=pk)
    return render_to_response("company/job_listing.html",{"job":j},context_instance=RequestContext(request))

def job_listing_list(request):
    """
        Displays all job listings.
    """
    jobs = Job.objects.all()
    return render_to_response("company/job_listing_list.html",{"jobs":jobs},context_instance=RequestContext(request))

#form views

@login_required
def create_company(request):
    """
        Creates a company profile.
    """
    form = CompanyForm()
    if request.method == "POST":
        form = CompanyForm(request.POST,request.FILES)
        if form.is_valid():
            company = form.save()
            return HttpResponseRedirect(reverse("company_profile",args=(company.pk,)))
    return render_to_response("company/company_form.html",{"form":form},context_instance=RequestContext(request))

@login_required
def create_job(request,company_pk=None):
    """
        Creates a job listing.
    """
    form = JobForm()
    
    if company_pk:
        company = get_object_or_404(Company,pk=company_pk)
        form.initial['company'] = company

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            #check that this person is a founder of the company
            if request.user not in form.instance.company.founders.all():
                messages.error(request,"Cannot create job listings for a company that you are not part of.")
                return render_to_response("company/job_form.html",{"form":form},context_instance=RequestContext(request))
            job = form.save()
            return HttpResponseRedirect(reverse("job_listing",args=(job.pk,)))
    return render_to_response("company/job_form.html",{"form":form},context_instance=RequestContext(request))
