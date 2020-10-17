from rest_framework import generics

from pets.models import Pet
from pets_rest_api import serializers


class ListPets(generics.ListAPIView):
    """Вывод списка животных"""
    queryset = Pet.objects.all()
    serializer_class = serializers.PetListSerializer


class DetailPet(generics.RetrieveAPIView):
    """Вью для просмотра животного"""
    queryset = Pet.objects.all()
    serializer_class = serializers.PetDetailSerializer


class CreatePet(generics.CreateAPIView):
    """Вью для добавления животного"""
    queryset = Pet.objects.all()
    serializer_class = serializers.PetCreateSerializer


class UpdatePet(generics.UpdateAPIView):
    """Вью для редактирования животного"""
    queryset = Pet.objects.all()
    serializer_class = serializers.PetUpdateSerializer


class DeletePet(generics.DestroyAPIView):
    """Вью для удаления животного"""
    queryset = Pet.objects.all()
    serializer_class = serializers.PetDeleteSerializer
