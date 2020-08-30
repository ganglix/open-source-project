from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# inherit from user form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # add email to the form

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']