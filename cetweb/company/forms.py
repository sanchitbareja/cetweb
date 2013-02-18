from django.forms import ModelForm

from company.models import Company, Job

class CompanyForm(ModelForm):
    class Meta:
        model = Company

class JobForm(ModelForm):
    class Meta:
        model = Job 
        exclude = ('requests',)
