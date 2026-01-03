from rest_framework import permissions


class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow staff users to perform write operations (POST, PUT, DELETE).
    Read operations (GET) are allowed for all users (including anonymous).
    """

    def has_permission(self, request, view):
        # SAFE_METHODS (GET, HEAD, OPTIONS) are always allowed for anyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to staff users
        # request.user.is_staff is set when the user logs in and the is_staff field is True
        return request.user and request.user.is_staff
