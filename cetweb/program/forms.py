from django.forms import ModelForm

from program.models import CertificateApplication

class CertificateApplicationForm(ModelForm):
    class Meta:
        model = CertificateApplication
