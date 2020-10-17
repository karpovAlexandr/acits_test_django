from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views import generic

from pets.forms import UserLoginForm
from pets.models import Pet


class PetListView(generic.ListView):
    """Вью для всех животных"""
    model = Pet
    context_object_name = 'pets'


class PetDetailView(generic.DetailView):
    """Вью для животного"""
    model = Pet
    context_object_name = 'pet'


class PetCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    """Вью создания животного"""
    model = Pet
    fields = '__all__'
    permission_required = 'pets.add_pet'


class PetUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    """Вью для редактирования животного"""
    model = Pet
    fields = '__all__'
    permission_required = 'pets.change_pet'


class PetDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    """Вью удаления животного"""
    model = Pet
    context_object_name = 'pet'
    permission_required = 'pets.delete_pet'

    def get_success_url(self):
        return reverse('pets:home')


class UserLoginView(LoginView):
    """Вью для логина пользователя"""
    form_class = UserLoginForm
    template_name = 'pets/login.html'

    def get_success_url(self):
        return reverse('pets:home')


class UserLogOutView(LogoutView):
    pass
