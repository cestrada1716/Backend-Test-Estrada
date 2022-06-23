# import rest_framework models
from rest_framework.permissions import BasePermission


class RoleUserPermission(BasePermission):
    """
    This class validates if the user is an admin.
    """

    def has_permission(self, request, view) -> bool:
        if "user_type" in request.session:
            if request.session["user_type"] == "admin":
                return True
            else:
                return False
        else:
            return False


class CreateOrderPermission(BasePermission):
    """
    This class validates if the user is an admin or employee.
    """

    def has_permission(self, request, view) -> bool:
        if "user_type" in request.session:
            if (
                request.session["user_type"] == "admin"
                or request.session["user_type"] == "employee"
            ):
                return True
            else:
                return False
        else:
            return False
