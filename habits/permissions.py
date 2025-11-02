from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):
    """Пермишн разрешающий просмотр объекта привычки только владельцам"""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
