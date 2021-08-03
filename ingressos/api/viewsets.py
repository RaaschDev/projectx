from django_filters.rest_framework import DjangoFilterBackend

from ingressos.models import IngressoModel
from rest_framework.viewsets import ModelViewSet
from .serializers import IngressoSerializer


class IngressoViewSet(ModelViewSet):
    queryset = IngressoModel.objects.all()
    serializer_class = IngressoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['evento',]
