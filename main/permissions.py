from rest_framework.permissions import BasePermission


class IsPostAuthor(BasePermission):
    def has_oblect_permission(self, request, view, obj):
            return request.user.is_authenticated and request.user == obj.author




