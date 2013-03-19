from django.forms import ModelForm

from splash.models import SplashEmail

class SplashEmailForm(ModelForm):
    class Meta:
        model = SplashEmail
