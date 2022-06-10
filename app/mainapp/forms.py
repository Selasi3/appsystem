from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models  import User
from django import  forms

from mainapp.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__" 
