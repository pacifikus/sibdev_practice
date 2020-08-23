from rest_framework import viewsets
from url_filter.integrations.drf import DjangoFilterBackend

from apps.eats.models import Dish
from apps.eats.serializers import DishSerializer
from apps.main.permissions.dish import DishPermission


class DishViewSet(viewsets.ModelViewSet):
    """
    Список блюд, доступных для заказа в заведении

    create:
    Создание нового блюда (доступно только содателю заведения)

    retrieve:
    Получение информации о конкретном блюде

    update:
    Изменение блюда (доступно только содателю заведения)

    partial_update:
    Обновление отдельных полей блюда (доступно только содателю заведения)
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (DishPermission, )
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('institution', 'ingredients', )
