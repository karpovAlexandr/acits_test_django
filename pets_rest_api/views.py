from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from pets_rest_api import permissions, serializers

from pets.models import Pet


class ListPets(generics.ListAPIView):
    """Вывод списка животных"""
    queryset = Pet.objects.all()
    serializer_class = serializers.PetListSerializer
    permission_classes = (IsAuthenticated,)


class DetailPet(generics.RetrieveAPIView):
    """Вью для просмотра животного"""
    queryset = Pet.objects.all()
    serializer_class = serializers.PetDetailSerializer
    permission_classes = (IsAuthenticated,)


class CreatePet(generics.CreateAPIView):
    """Вью для добавления животного"""
    queryset = Pet.objects.all()
    serializer_class = serializers.PetCreateSerializer
    permission_classes = (IsAuthenticated, permissions.PetCreatePermission,)


class UpdatePet(generics.UpdateAPIView):
    """Вью для редактирования животного"""
    queryset = Pet.objects.all()
    serializer_class = serializers.PetUpdateSerializer
    permission_classes = (IsAuthenticated, permissions.PetUpdatePermission,)


class DeletePet(generics.DestroyAPIView):
    """Вью для удаления животного"""
    queryset = Pet.objects.all()
    serializer_class = serializers.PetDeleteSerializer
    permission_classes = (IsAuthenticated, permissions.PetDeletePermission,)
