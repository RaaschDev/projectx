from bares.models import BarModel
from rest_framework import serializers


class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarModel
        fields = '__all__'
