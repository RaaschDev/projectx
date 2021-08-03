from django_filters.rest_framework import DjangoFilterBackend

from perfil_empresa.models import PerfilEmpresa
from rest_framework.viewsets import ModelViewSet
from .serializers import PerfilEmpresaSerializer


class PerfilEmpresaViewSet(ModelViewSet):
    queryset = PerfilEmpresa.objects.all()
    serializer_class = PerfilEmpresaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['empresa',]