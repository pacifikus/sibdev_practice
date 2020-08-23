from rest_framework import mixins, viewsets

from apps.test.models import Test
from apps.test.serializers import TestSerializer


class TestViewSet(viewsets.ReadOnlyModelViewSet, mixins.CreateModelMixin):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
