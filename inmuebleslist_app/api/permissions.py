from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    """Permiso para leer datos y/o modificar."""
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        
        staff_permission = bool(request.user and request.user.is_staff)
        return staff_permission
    
    
class ComentarioUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.comentario_user == request.user