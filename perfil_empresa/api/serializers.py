from perfil_empresa.models import PerfilEmpresa
from rest_framework import serializers


class PerfilEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilEmpresa
        fields = '__all__'
