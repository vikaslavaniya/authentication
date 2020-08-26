from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    phone = forms.IntegerField()
    class Meta:
        model = User
        fields = ['phone','email','password1','password2']
