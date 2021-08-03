from django_filters.rest_framework import DjangoFilterBackend

from comidas.models import ComidaModel
from rest_framework.viewsets import ModelViewSet
from .serializers import ComidaSerializer


class ComidaViewSet(ModelViewSet):
    queryset = ComidaModel.objects.all()
    serializer_class = ComidaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['evento',]