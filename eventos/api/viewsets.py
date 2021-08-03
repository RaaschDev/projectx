from eventos.models import EventoModel
from rest_framework.viewsets import ModelViewSet
from .serializers import EventoSerializer


class EventoViewSet(ModelViewSet):
    queryset = EventoModel.objects.all()
    serializer_class = EventoSerializer