from artistas.models import ArtistaModel, EventoArtistaModel
from rest_framework import serializers


class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistaModel
        fields = '__all__'


class EventoArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoArtistaModel
        fields = '__all__'