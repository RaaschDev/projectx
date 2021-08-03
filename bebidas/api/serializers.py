from bebidas.models import BebidaModel
from rest_framework import serializers


class BebidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BebidaModel
        fields = '__all__'
