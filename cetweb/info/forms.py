from django.forms import ModelForm
from django import forms

from info.models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
