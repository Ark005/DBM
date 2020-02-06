from django import forms
from .models import *

class Registration (forms.ModelForm):  
    class Meta:
        model = Person
        fields = ['login','password','name','email']
class AuthForms(forms.ModelForm):
     class Meta:
         model = Person
         fields = ['login','password']

