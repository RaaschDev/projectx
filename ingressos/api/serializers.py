from ingressos.models import IngressoModel
from rest_framework import serializers


class IngressoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngressoModel
        fields = '__all__'
