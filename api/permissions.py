#/
from rest_framework.permissions import BasePermission

class IsSecretaria(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'secretaria'

class IsTBC(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'tbc'

class IsTurista(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'turista'

