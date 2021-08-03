from empresa.models import EmpresaModel
from rest_framework import serializers


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaModel
        fields = '__all__'
