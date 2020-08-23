from rest_framework import routers

from apps.test.viewsets import TestViewSet
from apps.users.viewsets import UserViewSet
from apps.eats.viewsets import InstitutionViewSet, IngredientViewSet, DishViewSet


router = routers.DefaultRouter()
router.register('test', TestViewSet, basename='test')
router.register('users', UserViewSet, basename='users')
router.register('eats', InstitutionViewSet, basename='eats')
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('dishes', DishViewSet, basename='dishes')
