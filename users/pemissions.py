from rest_framework import permissions



class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_superuser


class UserEmployeeVerify(permissions.BasePermission):
    def has_object_permission(self, req, view, user) -> bool:

        if req.user.is_authenticated and (
            req.user.is_employee or req.user.id == user.id
        ):
            return True
