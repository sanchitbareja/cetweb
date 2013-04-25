from django.forms import ModelForm
from django import forms

from program.models import CertificateApplication
from program.certificate import verify_transcript

class CertificateApplicationForm(ModelForm):
    class Meta:
        model = CertificateApplication
