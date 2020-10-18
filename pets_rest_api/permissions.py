from rest_framework import  permissions


class CreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool('pets.add_pet' in request.user.get_user_permissions())


class UpdatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool('pets.change_pet' in request.user.get_user_permissions())


class DeletePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool('pets.delete_pet' in request.user.get_user_permissions())
