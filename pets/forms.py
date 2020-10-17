from django import forms
from pets.models import Pet


class PetForm(forms.Form):
    class Meta:
        model = Pet
        fields = '__all__'
