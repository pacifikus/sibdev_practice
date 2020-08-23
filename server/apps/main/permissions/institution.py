from rest_framework.permissions import BasePermission


class InstitutionPermission(BasePermission):

    def has_permission(self, request, view):
        if view.action in ('list', 'retrieve'):
            return True
        elif view.action in ('create', 'update', 'partial_update', 'destroy'):
            return request.user.is_authenticated
        else:
            return False

    def has_object_permission(self, request, view, institution):
        if view.action == 'retrieve':
            return True
        if view.action in ('update', 'partial_update', 'destroy'):
            return request.user == institution.owner
        else:
            return False
