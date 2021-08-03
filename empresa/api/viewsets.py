

from empresa.models import EmpresaModel
from rest_framework.viewsets import ModelViewSet
from .serializers import EmpresaSerializer


class EmpresaViewSet(ModelViewSet):
    queryset = EmpresaModel.objects.all()
    serializer_class = EmpresaSerializer