from bebidas.models import BebidaModel
from rest_framework.viewsets import ModelViewSet
from .serializers import BebidaSerializer
from django_filters.rest_framework import DjangoFilterBackend


class BebidaViewSet(ModelViewSet):
    queryset = BebidaModel.objects.all()
    serializer_class = BebidaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['evento',]