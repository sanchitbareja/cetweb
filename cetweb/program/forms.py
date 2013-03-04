from django.forms import ModelForm
from django import forms

from program.models import CertificateApplication
from program.certificate import verify_transcript

class CertificateApplicationForm(ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    def save(self,commit=True):
        instance = super(CertificateApplicationForm, self).save(commit=False)
        (gpa,courses) = verify_transcript(self.cleaned_data['username'],self.cleaned_data['password'])
        instance.GPA = gpa
        if commit:
            instance.save()
            for course in courses:
                instance.courses.add(course)
            instance.save()
        return instance
    class Meta:
        model = CertificateApplication
        exclude = ("courses","GPA")
