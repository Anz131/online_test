from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import Test



class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput())


class QusCreationForm(ModelForm):
    class Meta:
        model=Test
        fields="__all__"
        widgets = {
            "questions": forms.TextInput(attrs={"class": "form-control"}),
            "a": forms.TextInput(attrs={"class": "form-control"}),
            "b": forms.TextInput(attrs={"class": "form-control"}),
            "c": forms.TextInput(attrs={"class": "form-control"}),
            "d": forms.TextInput(attrs={"class": "form-control"}),

        }

class QusUpdationForm(ModelForm):
    class Meta:
        model=Test
        fields="__all__"
        widgets = {
            "questions": forms.TextInput(attrs={"class": "form-control"}),
            "a": forms.TextInput(attrs={"class": "form-control"}),
            "b": forms.TextInput(attrs={"class": "form-control"}),
            "c": forms.TextInput(attrs={"class": "form-control"}),
            "d": forms.TextInput(attrs={"class": "form-control"}),

        }


