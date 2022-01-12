from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class AuthenticatedUserChangeDeleteReviewPermission(permissions.BasePermission):
    """
    Custom permission that checks if the review belongs to the authenticated user. If it does
    not belong to the user, then a PermissionDenied exception is thrown.

    Inherits: BasePermission.
    """
    CHANGE_DELETE_METHODS = ('PUT', 'PATCH', 'DELETE',)

    def has_object_permission(self, request, view, obj):
        if request.method in self.CHANGE_DELETE_METHODS:
            if obj.user != request.user:
                raise PermissionDenied(
                    'You do not have permission. The review does not belong to you.')

        return super().has_object_permission(request, view, obj)
