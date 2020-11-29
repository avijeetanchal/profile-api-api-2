from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True     ## if the request is safe then it gonna allow reuqest

        return obj.id == request.user.id
