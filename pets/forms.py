from django import forms
from django.contrib.auth.forms import AuthenticationForm

from pets.models import Pet


class PetForm(forms.Form):
    class Meta:
        model = Pet
        fields = '__all__'


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль')
