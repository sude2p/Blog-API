from rest_framework import permissions

#Like/permissions.py

class IsLikeOwner(permissions.BasePermission):
    

    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, and OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Check if the user is the owner 
        return obj.user == request.user and request.method in ['PUT', 'DELETE']