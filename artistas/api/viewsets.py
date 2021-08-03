from django_filters.rest_framework import DjangoFilterBackend

from artistas.models import ArtistaModel, EventoArtistaModel
from rest_framework.viewsets import ModelViewSet
from .serializers import ArtistaSerializer, EventoArtistaSerializer


class ArtistaViewSet(ModelViewSet):
    queryset = ArtistaModel.objects.all()
    serializer_class = ArtistaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['evento',]


class EventoArtistaViewSet(ModelViewSet):
    queryset = EventoArtistaModel.objects.all()
    serializer_class = EventoArtistaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['evento',]