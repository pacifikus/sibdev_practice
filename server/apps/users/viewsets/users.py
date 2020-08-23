from rest_framework import mixins, viewsets

from apps.users.serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    Список пользователей / создателей заведений

    create:
    Создание нового пользователя / создателя заведения
    """
    serializer_class = UserSerializer
