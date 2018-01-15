from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import permissions

User = get_user_model()


class IsSelf(permissions.BasePermission):
    def has_permission(self, request, view):
        requested_user = get_object_or_404(User, pk=view.kwargs.get('pk'))
        return request.user and (request.user.id == requested_user.id)


class IsAdminOrSelf(permissions.BasePermission):
    def has_permission(self, request, view):
        return IsSelf().has_permission(request, view) or request.user.is_staff
