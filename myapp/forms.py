from django import forms
from .models import *


class signupform(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'

class updateform(forms.ModelForm):
    class Meta:
        model=userSignup
        fields=['firstname','lastname','username','password','mobile']

class notesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'

class contactForm(forms.ModelForm):
    class Meta:
        model=contactus
        fields='__all__'