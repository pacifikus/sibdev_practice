from rest_framework import viewsets
from url_filter.integrations.drf import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings

from apps.eats.models import Institution
from apps.eats.serializers import InstitutionSerializer
from apps.main.permissions.institution import InstitutionPermission


class InstitutionViewSet(viewsets.ModelViewSet):
    """
    Список заведений

    create:
    Создание нового заведения (доступно только авторизованному пользователю)

    retrieve:
    Получение информации о конкретном заведении

    update:
    Изменение данных заведения (доступно только содателю заведения)

    partial_update:
    Обновление отдельных полей заведения (доступно только содателю заведения)

    destroy:
    Удаление заведения
    """
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()
    permission_classes = (InstitutionPermission, )
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('owner', )

    @method_decorator(cache_page(settings.CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super(InstitutionViewSet, self).dispatch(*args, **kwargs)
