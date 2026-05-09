from django import forms
from .models import Resume
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ['user']


class LoginForm(AuthenticationForm):
    captcha = CaptchaField()