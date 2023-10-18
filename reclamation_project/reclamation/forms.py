from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Reclamation, CustomUser


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = ['Titre', 'Description']


class ReclamationDechiffrerForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = ['Titre', 'Description']


class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'PosteOccupe', 'Grade', 'email', 'password1', 'password2']


class AuthenticationUserForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
