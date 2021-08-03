from eventos.models import EventoModel
from rest_framework import serializers


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoModel
        fields = '__all__'
