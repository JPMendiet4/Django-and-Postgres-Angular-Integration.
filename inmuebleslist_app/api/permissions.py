from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    """Permiso para leer datos y/o modificar."""
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        
        staff_permission = bool(request.user and request.user.is_staff)
        return staff_permission