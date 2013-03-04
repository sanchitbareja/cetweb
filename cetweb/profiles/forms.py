from django import forms
from profiles.models import Profile


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    #For founders only:
    startup_name = forms.CharField()
    startup_url = forms.CharField() # startup url (or some kind of proof)
    role = forms.CharField()
    # For mentors only:
    industries = forms.CharField()
    # # For faculty only:
    department = forms.CharField()



# from django.forms import ModelForm
# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile