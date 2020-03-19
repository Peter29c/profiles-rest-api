from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    # Allow user to edit their own profile

    def has_object_permission(self, request, view, obj):
        # Check user is trying to edit their own profile
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Check if the user request is the same that the one that are trying to modify
        return obj.id == request.user.id