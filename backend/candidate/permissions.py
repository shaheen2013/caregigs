from rest_framework import permissions
from accounts.models import CustomUser

class IsCandidateOwner(permissions.BasePermission):
    def has_permission(self, request, view):
       if not request.user.is_authenticated:
          return False
       if request.user.is_superuser:
           return True
       if request.method in permissions.SAFE_METHODS:
           return True
       return False

    def has_object_permission(self, request, view, obj):
        return obj.candidate.user == request.user