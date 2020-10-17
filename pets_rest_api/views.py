from rest_framework import generics

from pets.models import Pet
from pets_rest_api.serializers import (
    PetCreateSerializer,
    PetDeleteSerializer,
    PetDetailSerializer,
    PetListSerializer,
    PetUpdateSerializer,
)


class ListPets(generics.ListAPIView):
    """Вывод списка животных"""
    queryset = Pet.objects.all()
    serializer_class = PetListSerializer


class DetailPet(generics.RetrieveAPIView):
    """Вью для просмотра животного"""
    queryset = Pet.objects.all()
    serializer_class = PetDetailSerializer


class CreatePet(generics.CreateAPIView):
    """Вью для добавления животного"""
    queryset = Pet.objects.all()
    serializer_class = PetCreateSerializer


class UpdatePet(generics.UpdateAPIView):
    """Вью для редактирования животного"""
    queryset = Pet.objects.all()
    serializer_class = PetUpdateSerializer


class DeletePet(generics.DestroyAPIView):
    """Вью для удаления животного"""
    queryset = Pet.objects.all()
    serializer_class = PetDeleteSerializer
