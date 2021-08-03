from django_filters.rest_framework import DjangoFilterBackend

from bares.models import BarModel
from rest_framework.viewsets import ModelViewSet
from .serializers import BarSerializer


class BarViewSet(ModelViewSet):
    queryset = BarModel.objects.all()
    serializer_class = BarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['evento',]