from rest_framework.permissions import BasePermission, SAFE_METHODS

from users.models import User


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff


class IsAdminOrLibrarianOrSubmitOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.method == 'DELETE':
            return True
        else:
            return request.user.role == User.Roles.ADMIN or request.user.role == User.Roles.LIBRARIAN


class IsAdminOrLibrarianOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.role == User.Roles.ADMIN or request.user.role == User.Roles.LIBRARIAN


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `user`.
        return obj.user == request.user
