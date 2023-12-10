# comments/permissions.py

from rest_framework import permissions

class IsCommentOwner(permissions.BasePermission):
    """
    Custom permission to only allow the owner of a comment to delete or update it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, and OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Check if the user is the owner of the comment
        return obj.user == request.user