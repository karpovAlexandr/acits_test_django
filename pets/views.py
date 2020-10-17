from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import (
    CreateView, DeleteView,
    DetailView, ListView,
    UpdateView
)

from pets.models import Pet


class PetListView(ListView):
    """Вью для всех животных"""
    model = Pet
    context_object_name = 'pets'


class PetDetailView(DetailView):
    """Вью для животного"""
    model = Pet
    context_object_name = 'pet'


class PetCreateView(LoginRequiredMixin, CreateView):
    """Вью создания животного"""
    model = Pet
    fields = '__all__'


class PetUpdateView(LoginRequiredMixin, UpdateView):
    """Вью для редактирования живтного"""
    model = Pet
    fields = '__all__'


class PetDeleteView(LoginRequiredMixin, DeleteView):
    """Вью удяления живтного"""
    model = Pet
    context_object_name = 'pet'

    def get_success_url(self):
        return reverse('pets:home')

