from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = ['user']
        widgets = {'profile_image': forms.FileInput(
                            attrs={'multiple': False})}
