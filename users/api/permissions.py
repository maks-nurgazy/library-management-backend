from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
