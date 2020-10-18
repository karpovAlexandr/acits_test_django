from rest_framework import permissions


class PetBasePermission(permissions.BasePermission):
    """Базовый класс для доступов к api"""
    permission = 'pets.read_pet'

    def has_permission(self, request, view):
        return bool(self.permission in request.user.get_user_permissions())


class PetCreatePermission(PetBasePermission):
    permission = 'pets.add_pet'


class PetUpdatePermission(PetBasePermission):
    permission = 'pets.change_pet'


class PetDeletePermission(PetBasePermission):
    permission = 'pets.delete_pet'
