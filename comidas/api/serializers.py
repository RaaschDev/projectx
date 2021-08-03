from comidas.models import ComidaModel
from rest_framework import serializers


class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComidaModel
        fields = '__all__'
