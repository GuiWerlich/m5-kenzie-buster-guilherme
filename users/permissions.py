from rest_framework import permissions
    
class IsOwnerOrEmployee(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj == request.user or request.user.is_employee
        return False
