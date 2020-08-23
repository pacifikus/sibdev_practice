from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from url_filter.integrations.drf import DjangoFilterBackend

from apps.eats.models import Ingredient
from apps.eats.serializers import IngredientSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Список ингредиентов для создания блюд

    retrieve:
    Получение информации о конкретном ингредиенте
    """
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('dish', )
