from distutils.command.install import install

from rest_framework.permissions import BasePermission
from apps.eats.models.institution import Institution


class DishPermission(BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        if view.action == 'create':
            institution_id = request.data['institution']
            user = request.user
            return user.is_authenticated and user.id == Institution.objects.get(id=institution_id).owner_id
        if view.action in ('create', 'update', 'partial_update', 'destroy'):
            return request.user.is_authenticated
        else:
            return False

    def has_object_permission(self, request, view, dish):
        if view.action in ('update', 'partial_update', 'destroy'):
            return request.user == dish.institution.owner
        else:
            return False
