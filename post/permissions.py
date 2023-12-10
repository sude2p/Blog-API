from rest_framework import permissions
from rest_framework.permissions import BasePermission

# blog/permissions.py


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only permissions for any request
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Allow modification only if the user is the author and is not modifying the 'author' field
        return obj.author == request.user 

